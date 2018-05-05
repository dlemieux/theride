"""
Room

Rooms are simple containers that has no location of their own.

"""

import random
import datetime

from evennia import DefaultRoom
from evennia import TICKER_HANDLER

class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    pass


class WalkwayRoom(DefaultRoom):
    """
    This is the walkway from the Entrance to the Courtyard.
    It has an intercom that gives players a personalized intro into the park while
    they travel along an automated walkway.
    """

    messages = (
        "  |WIntercom: Welcome to The Park!|n",
        "  |WIntercom: By participating in rides and attractions you can earn Park Points!|n",
        "  |WIntercom: Spend your Park Points at any gift shop to get wonderful prizes!|n",
        )
    cur_message_index = 0

    def at_object_creation(self):
        super(WalkwayRoom, self).at_object_creation()

        self.db.interval = 8 # Every X seconds it updates the room

        TICKER_HANDLER.add(interval=self.db.interval, callback=self.update_intercom, idstring="the_ride")

    def update_intercom(self, *args, **kwargs):
        
        #self.msg_contents(self.contents) # This is a list of all things in the room
        
        message = self.messages[self.cur_message_index]
        self.cur_message_index = (self.cur_message_index + 1) % len(self.messages)

        self.msg_contents(message)


class ChimeraLineRoom(DefaultRoom):

    # Room state
    # 0 = waiting for car to return
    # 1 = accepting people for current car

    between_cars_delay = 60 # Value in seconds
    boarding_time_delay = 30 # Seconds to board the current car

    def at_object_creation(self):
        #self.msg_contents("ChimeraLineRoom: creation")

        self.db.next_ticket_number = 1

        self.db.room_state = 0

        return super(ChimeraLineRoom, self).at_object_creation()

    def at_object_leave(self, moved_obj, target_location, **kwargs):
        self.msg_contents("ChimeraLineRoom: object leave")
        return super(ChimeraLineRoom, self).at_object_leave(moved_obj, target_location, **kwargs)

    def at_object_receive(self, moved_obj, source_location, **kwargs):
        #self.msg_contents("ChimeraLineRoom: object receive")

        moved_obj.db.chimera_line_index = self.db.next_ticket_number
        self.db.next_ticket_number = self.db.next_ticket_number + 1

        return super(ChimeraLineRoom, self).at_object_receive(moved_obj, source_location, **kwargs)

    def at_heard_say(self, message, speaker):
        self.msg_contents("ChimeraLineRoom: at_say")

    def at_object_creation(self):
        super(ChimeraLineRoom, self).at_object_creation()

        self.db.interval = 5 # Every X seconds it updates the room

        TICKER_HANDLER.add(interval=self.db.interval, callback=self.update_loop, idstring="the_ride")

    def update_loop(self, *args, **kwargs):
        now = datetime.datetime.utcnow()

        # See if this is the first ever time
        if not hasattr(self, "last_ride_time"):
            self.last_ride_time = now

        time_elapsed = now - self.last_ride_time
        seconds_elapsed = time_elapsed.seconds

        # Determine whether we are waiting for ride to return or waiting for people to board, or sending off the people after time out
        if self.db.room_state == 0:
            # See if you should keep waiting or advance to state 1
            if seconds_elapsed > self.between_cars_delay:
                # Announce that a new car has arrived

                self.db.room_state = 1 # Advance to boarding phase
                self.last_ride_time = now # Update to current time

                self.msg_contents("The next car has arrived! Please |cboard|n if you are next in line!")

        elif self.db.room_state == 1:
            # See if you should keep waiting, or move the car on and wait again in state 0
            if seconds_elapsed > self.boarding_time_delay:
                # Announce that the car is leaving
                self.msg_contents("The car has left the station! Please wait for the next car to arrive.")

                self.db.room_state = 0 # Switch back to the waiting state
                self.db.last_ride_time = now # Update to current time

        #self.msg_contents(self.contents) # This is a list of all things in the room
        
        # Iterate over all items in contents and assemble name/ticket number pairs
        max_index_allowed = -1
        player_name = "<none>"
        for item in self.contents:
            if (hasattr(item, "db") and hasattr(item.db, "chimera_line_index") and item.db.chimera_line_index > 0):
                if max_index_allowed == -1 or item.db.chimera_line_index < max_index_allowed:
                    max_index_allowed = item.db.chimera_line_index
                    player_name = item.name

        # Sort the list


        # Take the bottom n entries and announce that they can board

        self.db.max_index_allowed = max_index_allowed
        message = "Now boarding |c%s|n (%s)" % (player_name, self.db.max_index_allowed)

        #self.msg_contents(message)


class ChimeraBoardingZone(DefaultRoom):
    pass
        