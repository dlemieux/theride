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
    help_category = GAME_HELP_CATEGORY
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
        # Guard against None objects
        if not photo_info:
            return ""

        rider_list = photo_info['rider_list']
        if not rider_list or len(rider_list) == 0:
            return "" # Should not happen with 0 riders. Ignore invalid photo.

        # Build date string
        date_string = "|mDate:|n " + photo_info['created_date']
        date_string_len = len(date_string) - 4 # Remove formatting characters

        # Trim all the rider names
        trimmed_names = []
        for rider_name in rider_list:
            if len(rider_name) > PHOTO_ALBUM_MAX_NAME_LENGTH:
                trimmed_names.append(rider_name[:PHOTO_ALBUM_MAX_NAME_LENGTH])
            else:
                trimmed_names.append(rider_name)
        rider_list = trimmed_names

        # Build first rider string
        riders_string = "|mRiders:|n %s" % (rider_list[0])
        riders_string_len = len(riders_string) - 4 # Remove formatting characters

        # Build the other rider strings
        other_rider_strings_list = []
        for rider_name in rider_list[1:]:
            other_rider_strings_list.append("        %s" % (rider_name))
        
        # Determine max among the single lines
        maxRowSize = max(date_string_len, riders_string_len)
        for other_rider in other_rider_strings_list:
            maxRowSize = max(maxRowSize, len(other_rider))

        msg = "|c" # Set the color
        msg += ("==%s==" % ("=".ljust(maxRowSize, '='))) + "\n"
        msg += ("| |w%s|c |" % (date_string.ljust(maxRowSize + 4))) + "\n" # Date line
        msg += ("| |w%s|c |" % (riders_string.ljust(maxRowSize + 4))) + "\n" # First rider

        for other_rider in other_rider_strings_list:
            msg += ("| |w%s|c |" % (other_rider.ljust(maxRowSize))) + "\n" # Other riders

        msg += ("==%s==" % ("=".ljust(maxRowSize, '='))) + "\n"
        msg += "|n" # Return to normal color

        return msg


class CmdBuyPhoto(Command):
    """
    Buy the picture of you riding the |rChimera|n.

    Usage:
      buy photo
    """
    key = "buy photo"
    help_category = GAME_HELP_CATEGORY
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
        self.locks.add("give:false()")

        # Add command set for people who hold an album
        self.cmdset.add_default(CmdSetPhotoAlbum)


class PhotoClerk(DefaultObject):
    "Photo Clerk"
    def at_object_creation(self):
        "Called whenever a new object is created"
        
        # lock the object down by default
        self.locks.add("get:false()")
        
        self.db.desc = "The photo clerk has a degree in photojournalism and once was in the same room as a Pulitzer Prize winner. But you don't care about that. To you, this is only the person that sells you photos."
        self.db.talk_to_msg = "Photo Clerk: \"Don't you want to remember this ride forever? For only |c%s|n points, you can! Just tell me you want to [|gbuy photo|n] and I'll get you one!\"" % (PHOTO_PRICE)

        self.db.get_err_msg = "No touching!"
        self.db.consider_msg = "You wouldn't stand a chance."

    def at_before_move(self, destination, **kwargs):
        self.delete() # Doesn't need to live if the room is changed


class ChimeraExitRoom(DefaultRoom):
    cur_photo_info = None
    
    def at_object_creation(self):
        super(ChimeraExitRoom, self).at_object_creation()

        desc = ""
        desc += "The exit zone looks very similar to the boarding zone: a dark, featureless room with a structure set up to support your ride cart. By the time you've stepped down from the platform, the |rChimera|n has already retreated back to its home. There, it will relax until the next time it wants to go for a ride."

        self.cmdset.add_default(CmdSetChimeraExit)

        # Set up an exit in the room that they can take
        gift_shop_room = self.search(MAP_GIFT_SHOP_OBJECT_NAME, global_search=True) # Fetch dynamically

        typeclass = "typeclasses.exits.Exit"
        exit_obj = create_object(typeclass, "gift shop", self, aliases=["gift","shop","g"], destination=gift_shop_room)
        exit_obj.db.desc = "The way to the gift shop."

        self.db.desc = desc
        self.db.players_arrived = False

        # Create the photo clerk in the room
        create_object(PhotoClerk, key="Photo Clerk", aliases=["clerk"], location=self)

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

        # Might be None if server reloaded
        if not self.cur_photo_info:
            player.msg("Photo Clerk: \"Sorry, the photo didn't turn out due to a technical difficulty. Try again next time and it should be cleared up!\"")
            return

        # Check if they have enough money
        if player.db.pass_points > PHOTO_PRICE:
            player.db.pass_points = player.db.pass_points - PHOTO_PRICE
            self.give_player_photo(player, self.cur_photo_info)

            player.msg("Photo Clerk: \"Here you go! Use [|gread album|n] to check it out!\"")
        else:
            player.msg("Photo Clerk: \"You cannot afford the photo!\"")

    def give_player_album(self, player):
        create_object(PhotoAlbum, key="Photo Album", location=player)

    def build_photo_info(self, rider_list):
        ride_time = datetime.datetime.utcnow()
        stringDate = ride_time.strftime("%B %d, %Y %I:%M %p (UTC)") # Ex: October 3, 2018 6:03 pm (UTC)

        photoInfo = {
            'created_date': stringDate,
            'rider_list': rider_list,
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

