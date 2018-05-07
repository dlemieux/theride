import random
import datetime

from evennia import CmdSet, Command
from evennia import create_object
from evennia import DefaultRoom
from evennia import DefaultExit
from evennia import TICKER_HANDLER

from typeclasses.room_chimera_ride import ChimeraRideRoom

class CmdSuggestRideTopic(Command):
    """
    Command to suggest a topic for the ride.

    suggest <suggestion>
    """
    key = "suggest"
    #aliases = ["h", "?"]
    locks = "cmd:all()"
    help_category = "The Ride"

    def func(self):
        """Implements the command."""
        
        caller = self.caller

        if not self.args:
            caller.msg("suggest <suggestion>")
            return

        caller.msg("You suggest%s" % self.args)
        caller.location.msg_contents("  |CSomeone made a suggestion", exclude=caller)


class CmdSetBoardingZone(CmdSet):
    """This groups the commands for people in the boarding zone"""
    key = "Line Room Commands"
    priority = 1  # this gives it precedence over the normal look/help commands.

    def at_cmdset_creation(self):
        """Called at first cmdset creation"""
        self.add(CmdSuggestRideTopic())


class ChimeraBoardingZone(DefaultRoom):
    task_messages = [
        "You may talk amongst yourselves while I verify the integrity of your restraints...",
        "Please entertain each other and pay no mind to the loose bolts I'll be fixing with this wrench...",
        "Be careful as you move about the car. Any human remains...I mean belongings...will be removed shortly...",
        ]

    def at_object_creation(self):
        super(ChimeraBoardingZone, self).at_object_creation()

        desc = ""
        desc += "You are in a dark room that has the ride car in the middle.\n"
        desc += "The ride will begin shortly.\nYou can use |gsuggest <feature>|n to encourage\n"
        desc += "different events to happen during your ride, IF the attendant feels like helping you out."
        self.db.desc = desc

        self.cmdset.add_default(CmdSetBoardingZone)

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
                    new_ride_room = create_object(ChimeraRideRoom, key="Chimera Ride Room")

                    # Move all players into the ride room
                    for rider in self.contents:
                        rider.move_to(new_ride_room)

                # Destroy this room
                self.delete()


    # Returns the number of seconds to wait until the next event
    def send_message(self, index):
        if index == 0:
            return 9 # Slight delay with no text for people to enter
        elif index == 1:
            msg = ""
            msg += "|y> auto-advance|n" + "\n"
            msg += "Welcome to the boarding zone!" + "\n"
            msg += "Just get in your seats and the ride will begin shortly." + "\n"

            msg += random.choice(self.task_messages)

            self.msg_contents(msg)
            return 9
        elif index == 2:
            msg = ""
            msg += "|y> auto-advance|n" + "\n"
            msg += "A massive chimera approaches from beneath the cart and you feel the entire thing raise up!"

            self.msg_contents(msg)

            return 9
        elif index == 3:
            msg = ""
            msg += "|y> auto-advance|n" + "\n"
            msg += "As the chimera flexes its legs, you are tossed about easily like toy." + "\n"
            msg += "Suddenly...the chimera leaps forward! And you're off!"

            self.msg_contents(msg)

            return 9

        return -1