import random
import datetime

from evennia import CmdSet, Command
from evennia import create_object
from evennia import DefaultRoom
from evennia import DefaultExit
from evennia import TICKER_HANDLER


class ChimeraExitRoom(DefaultRoom):
    def at_object_creation(self):
        super(ChimeraExitRoom, self).at_object_creation()

        desc = ""
        desc += "Thank you for riding!"

        # Set up an exit in the room that they can take
        # DALE: This needs to match the current database you are running on
        gift_shop_room = "#228" #self.search("ChimeraGiftShop")

        typeclass = "typeclasses.exits.Exit"
        exit_obj = create_object(typeclass, "gift shop", self, aliases=["gift","shop"], destination=gift_shop_room)
        exit_obj.db.desc = "The way to the gift shop."

        self.db.desc = desc
        self.db.players_arrived = False

        self.db.interval = 10 # Every X seconds it updates the room
        TICKER_HANDLER.add(interval=self.db.interval, callback=self.update_loop, idstring="the_ride")


    def players_arrived(self):
        points_per_ride = 10

        for person in self.contents:
            if hasattr(person, "db"):
                if (hasattr(person.db, "has_season_pass") and person.db.has_season_pass == True):
                    # Give them points
                    person.db.pass_points = person.db.pass_points + points_per_ride
                    person.msg("You were awarded %s points for surviving the |rChimera|n!\nPlease ride again soon!" % points_per_ride)

                    # Do the album logic

        self.db.players_arrived = True

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


