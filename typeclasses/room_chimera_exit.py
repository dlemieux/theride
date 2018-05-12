import random
import datetime

from evennia import CmdSet, Command
from evennia import create_object
from evennia import DefaultRoom, DefaultObject
from evennia import DefaultExit
from evennia import TICKER_HANDLER

from typeclasses.config_all import *


class CmdReadAlbum(Command):
    """
    Read your photo album.

    Usage:
      read album
    """
    key = "read album"
    aliases = ["read photos", "read photo", "view album", "view photos", "view photo"]
    help_category = "The Ride"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        photo_list = caller.db.photo_list

        photo_string_list = []
        for photo_info in photo_list:
            photo_string = self.build_photo_string(photo_info)
            photo_string_list.append(photo_string)

        msg = "\n".join(photo_string_list)
        caller.msg(msg)

    def build_photo_string(self, photo_info):
        date_string = "|mDate:|n " + photo_info['created_date']

        rider_names = "|mRiders:|n " + ", ".join(photo_info['rider_list'])

        max_name_length = 200
        if len(rider_names) > max_name_length:
            rider_names = rider_names[:max_name_length]

        maxRowSize = max(len(rider_names), len(date_string))

        msg = "|c" # Set the color
        msg += "==%s==\n" % ("=".ljust(maxRowSize, '='))
        msg += "| |w%s|c |\n" % (date_string.ljust(maxRowSize + 4))
        msg += "| |w%s|c |\n" % (rider_names.ljust(maxRowSize + 4))
        msg += "==%s==\n" % ("=".ljust(maxRowSize, '='))
        msg += "|n" # Return to normal color

        return msg


class CmdBuyPhoto(Command):
    """
    Buy the picture of you riding the |rChimera|n.

    Usage:
      buy photo
    """
    key = "buy photo"
    help_category = "The Ride"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        location = caller.location
        location.buy_photo(caller)


class CmdSetPhotoAlbum(CmdSet):
    """This groups the commands"""
    key = "Photo Album Commands"
    priority = 1  # this gives it precedence over the normal look/help commands.

    def at_cmdset_creation(self):
        """Called at first cmdset creation"""
        self.add(CmdReadAlbum())


class CmdSetChimeraExit(CmdSet):
    """This groups the commands"""
    key = "Chimera Exit Commands"
    priority = 1  # this gives it precedence over the normal look/help commands.

    def at_cmdset_creation(self):
        """Called at first cmdset creation"""
        self.add(CmdBuyPhoto())


class PhotoAlbum(DefaultObject):
    """
    This implements a user's photo album.
    """

    def at_object_creation(self):
        """Called when object is first created."""
        super(PhotoAlbum, self).at_object_creation()
        
        # Set system properties
        self.db.desc = "A photo album to store your treasured memories in the park! Use [|gread album|n] to see the details!"
        self.db.drop_err_msg = "You wouldn't want to drop that!"
        self.db.is_photo_album = True # Used to detect albums in another command

        self.locks.add("drop:false()")
        # Add command set for people who hold an album
        self.cmdset.add_default(CmdSetPhotoAlbum)


class ChimeraExitRoom(DefaultRoom):
    cur_photo_info = None
    
    def at_object_creation(self):
        super(ChimeraExitRoom, self).at_object_creation()

        desc = ""
        desc += "Thank you for riding!"

        self.cmdset.add_default(CmdSetChimeraExit)

        # Set up an exit in the room that they can take
        gift_shop_room = self.search("Chimera Gift Shop", global_search=True) # Fetch dynamically

        typeclass = "typeclasses.exits.Exit"
        exit_obj = create_object(typeclass, "gift shop", self, aliases=["gift","shop","g"], destination=gift_shop_room)
        exit_obj.db.desc = "The way to the gift shop."

        self.db.desc = desc
        self.db.players_arrived = False

        self.db.interval = 10 # Every X seconds it updates the room
        TICKER_HANDLER.add(interval=self.db.interval, callback=self.update_loop, idstring="the_ride")


    def players_arrived(self):
        points_per_ride = 10

        # Build a rider list for the photo
        rider_list = []
        for person in self.contents:
            if hasattr(person, "db"):
                if (hasattr(person.db, "has_season_pass") and person.db.has_season_pass == True):
                    rider_list.append(person.name)

        cur_photo_info = self.build_photo_info(rider_list)
        self.cur_photo_info = cur_photo_info

        for person in self.contents:
            if hasattr(person, "db"):
                if (hasattr(person.db, "has_season_pass") and person.db.has_season_pass == True):
                    # Give them points
                    person.db.pass_points = person.db.pass_points + points_per_ride
                    person.msg("You were awarded |c%s|n points for surviving the |rChimera|n!\nPlease ride again soon!" % points_per_ride)

                    # Do the album logic
                    if not self.player_has_album(person):
                        person.msg("Since this is your first time, we'll give you a |mphoto album|n for free!\nAnd I'll even throw in the photo from your ride today!\nNext time, you'll have to pay on your own!\nYou can view your photo album in your [|ginventory|n].")
                        self.give_player_album(person)
                        self.give_player_photo(person, cur_photo_info)
                    else:
                        person.msg("If you would like to purchase your ride photo for |c%s|n points, don't forget to use [|gbuy photo|n] before you leave the room!" % (PHOTO_PRICE))

        self.db.players_arrived = True

    def player_has_album(self, player):
        # Search player inventory and determine if they have an album
        for item in player.contents:
            if item.db.is_photo_album:
                return True

        return False

    def buy_photo(self, player):

        # Don't let them buy if people are still arriving
        if not self.db.players_arrived:
            return

        # Check if they have enough money
        if player.db.pass_points > PHOTO_PRICE:
            player.db.pass_points = player.db.pass_points - PHOTO_PRICE
            self.give_player_photo(player, self.cur_photo_info)

            player.msg("Here you go! Use [|gread album|n] to check it out!")
        else:
            player.msg("You cannot afford the photo!")

    def give_player_album(self, player):
        create_object(PhotoAlbum, key="Photo Album", location=player)

    def build_photo_info(self, rider_list):
        ride_time = datetime.datetime.utcnow()
        stringDate = ride_time.strftime("%B %d, %Y %I:%M %p (UTC)") # Ex: October 3, 2018 6:03 pm (UTC)

        photoInfo = {
            'created_date': stringDate,
            'rider_list': rider_list
            }

        return photoInfo

    def give_player_photo(self, player, photoInfo):
        if not player.db.photo_list:
            player.db.photo_list = []

        player.db.photo_list.append(photoInfo)

    def does_contain_players(self):
        # See if any people are left who have a season pass
        players_remaining = 0
        for person in self.contents:
            if hasattr(person, "db"):
                if (hasattr(person.db, "has_season_pass") and person.db.has_season_pass == True):
                    players_remaining += 1

        return players_remaining > 0

    def update_loop(self):
        # Destroy this room when it is no longer needed
        if self.db.players_arrived:
            contains_players = self.does_contain_players()
            if not contains_players:
                self.delete()

