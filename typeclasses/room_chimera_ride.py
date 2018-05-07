import random
import datetime

from evennia import CmdSet, Command
from evennia import create_object
from evennia import DefaultRoom
from evennia import DefaultExit
from evennia import TICKER_HANDLER

from typeclasses.room_chimera_exit import ChimeraExitRoom

class ChimeraRideRoom(DefaultRoom):
    def at_object_creation(self):
        super(ChimeraRideRoom, self).at_object_creation()

        desc = ""
        desc += "You are now on the ride."
        self.db.desc = desc

        #self.cmdset.add_default(CmdSetBoardingZone)

        self.db.interval = 1 # Every X seconds it updates the room
        TICKER_HANDLER.add(interval=self.db.interval, callback=self.update_loop, idstring="the_ride")


    def update_loop(self):
        now = datetime.datetime.utcnow()

        if not hasattr(self, 'last_event_time'):
            self.last_event_time = now

        if not hasattr(self, 'msg_index'):
            self.msg_index = -1

        if not hasattr(self, 'msg_delay'):
            self.msg_delay = 0

        elapsed = now - self.last_event_time
        if elapsed.seconds > self.msg_delay:
            self.msg_index = self.msg_index + 1 # Advance to the next index

            next_delay = self.send_message(self.msg_index)
            if next_delay >= 0:
                self.msg_delay = next_delay
                self.last_event_time = now
            else: # Nothing left to do in here
                if len(self.contents) > 0:
                    # Create a room for the exit
                    new_exit_room = create_object(ChimeraExitRoom, key="Chimera Ride Exit Room")

                    # TODO: Create a photo item for everyone and add it to their inventory
                    # Make sure the description lists who was in the photo

                    # Move all players into the ride room
                    for rider in self.contents:
                        if hasattr(rider, "db"):
                            if (hasattr(rider.db, "has_season_pass") and rider.db.has_season_pass == True):
                                rider.move_to(new_exit_room)

                    new_exit_room.players_arrived()

                # Destroy this room
                self.delete()


    # Returns the number of seconds to wait until the next event
    def send_message(self, index):
        if index == 0:
            return 9 # Slight delay with no text for people to enter
        elif index == 1:
            msg = ""
            msg += "|y> auto-advance|n" + "\n"
            msg += "First ride event"

            self.msg_contents(msg)

            return 9
        elif index == 2:
            msg = ""
            msg += "|y> auto-advance|n" + "\n"
            msg += "Second ride event"

            self.msg_contents(msg)

            return 9
        elif index == 3:
            msg = ""
            msg += "|y> auto-advance|n" + "\n"
            msg += "Third ride event"

            self.msg_contents(msg)

            return 9

        return -1