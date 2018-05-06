"""
Room

Rooms are simple containers that has no location of their own.

"""

import random
import datetime

from evennia import CmdSet, Command
from evennia import create_object
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


class CmdBoardCar(Command):
    """
    Command to board the car
    """
    key = "board"
    #aliases = ["h", "?"]
    locks = "cmd:all()"
    help_category = "The Ride"

    def func(self):
        """Implements the command."""
        
        caller = self.caller

        location = caller.location
        room_state = location.db.room_state
        max_index_allowed = location.db.max_index_allowed

        boarding_zone = None
        if hasattr(location, 'cur_boarding_zone'):
            boarding_zone = location.cur_boarding_zone

        # If room state is 0, then we are still waiting for a car to arrive
        if room_state == 0:
            caller.msg("You cannot board because a car has not arrived on the track yet.")
        elif room_state == 1:
            if caller.db.chimera_line_index <= max_index_allowed:
                # Ready to board!
                caller.msg("You may now board. Enjoy!")

                if boarding_zone:
                    #caller.msg("Boarding zone: %s" % boarding_zone.id)
                    #caller.location = boarding_zone # This moves the player, but they don't get the next look command
                    caller.move_to(boarding_zone)
            else:
                caller.msg("It's not your turn yet!")


class CmdSetLineRoom(CmdSet):
    """This groups the commands for people in the line room"""
    key = "Line Room Commands"
    priority = 1  # this gives it precedence over the normal look/help commands.

    def at_cmdset_creation(self):
        """Called at first cmdset creation"""
        self.add(CmdBoardCar())


class ChimeraLineRoom(DefaultRoom):

    # Room state
    # 0 = waiting for car to return
    # 1 = accepting people for current car

    def at_object_creation(self):
        super(ChimeraLineRoom, self).at_object_creation()

        self.db.interval = 5 # Every X seconds it updates the room
        TICKER_HANDLER.add(interval=self.db.interval, callback=self.update_loop, idstring="the_ride")

        # Constants
        self.db.between_cars_delay = 60 # Value in seconds
        self.db.boarding_time_delay = 30 # Seconds to board the current car
        self.db.riders_per_car = 4

        self.db.next_ticket_number = 1
        self.db.room_state = 0

        self.cmdset.add_default(CmdSetLineRoom)

    #def at_object_leave(self, moved_obj, target_location, **kwargs):
        #self.msg_contents("ChimeraLineRoom: object leave")
        #return super(ChimeraLineRoom, self).at_object_leave(moved_obj, target_location, **kwargs)

    def at_object_receive(self, moved_obj, source_location, **kwargs):
        #self.msg_contents("ChimeraLineRoom: object receive")

        moved_obj.db.chimera_line_index = self.db.next_ticket_number
        self.db.next_ticket_number = self.db.next_ticket_number + 1

        return super(ChimeraLineRoom, self).at_object_receive(moved_obj, source_location, **kwargs)

    def update_loop(self, *args, **kwargs):
        now = datetime.datetime.utcnow()

        # See if this is the first ever time
        if not hasattr(self, "last_ride_time"):
            #self.msg_contents("Setting last ride time")
            self.last_ride_time = now
        #else:
            #self.msg_contents("Last ride time has value: " + self.last_ride_time)

        time_elapsed = now - self.last_ride_time
        seconds_elapsed = time_elapsed.seconds
        self.msg_contents("Seconds elapsed: %s" % seconds_elapsed)

        # Determine whether we are waiting for ride to return or waiting for people to board, or sending off the people after time out
        if self.db.room_state == 0:
            # See if you should keep waiting or advance to state 1
            if seconds_elapsed >= self.db.between_cars_delay:
                # Announce that a new car has arrived

                self.last_ride_time = now # Update to current time

                self.msg_contents("The next car has arrived! Please |gboard|n if you are next in line!")

                # Make a whitelist for the people who can board
                self.build_rider_list()
                self.create_new_boarding_zone()

                self.db.room_state = 1 # Advance to boarding phase

        elif self.db.room_state == 1:
            # See if you should keep waiting, or move the car on and wait again in state 0
            if seconds_elapsed >= self.db.boarding_time_delay:
                # Announce that the car is leaving
                self.msg_contents("The car has left the station! Please wait for the next car to arrive.")

                self.last_ride_time = now # Update to current time

                # Anyone who missed their chance is moved to the back of the line
                self.reset_lazy_riders()

                self.db.room_state = 0 # Switch back to the waiting state

        #self.msg_contents(self.contents) # This is a list of all things in the room
    
    def create_new_boarding_zone(self):
        new_boarding_zone = create_object(ChimeraBoardingZone, key="Boarding Zone")
        # Save room info somewhere so board command can move people there
        self.cur_boarding_zone = new_boarding_zone
        self.msg_contents("Created new boarding zone: %s" % new_boarding_zone.id)
        
    def build_rider_list(self):
        # Build the list of the top n people who can board
        # Save the value in a property for the board command to read from
        # TODO

        # Iterate over all items in contents and assemble name/ticket number pairs
        max_index_allowed = -1
        player_name = "<none>"

        # Build a list of all riders in the room
        rider_list = []
        for item in self.contents:
            if (hasattr(item, "db") and hasattr(item.db, "chimera_line_index") and item.db.chimera_line_index > 0):
                rider_info = {}
                rider_info['name'] = "|c%s|n" % (item.name)
                rider_info['index'] = item.db.chimera_line_index
                rider_info['obj'] = item

                rider_list.append(rider_info)

        # Sort the list
        sorted_riders = sorted(rider_list, key=lambda rider: rider['index'])

        # TEST DATA
        #a = {'name':'A','index':4}
        #b = {'name':'B','index':8}
        #c = {'name':'C','index':3}
        #d = {'name':'D','index':1}
        #test_list = [a, b, c, d]
        #sorted(test_list, key=lambda rider: rider['index'])

        # Take the bottom n entries and announce that they can board
        whitelist_riders = sorted_riders[:self.db.riders_per_car]
        self.whitelist_riders = whitelist_riders # Save a reference of the rider list on the object itself

        # Set a property so the board command knows who to allow
        last_index = len(whitelist_riders) - 1
        last_rider = whitelist_riders[last_index]
        self.db.max_index_allowed = last_rider['index']
        message = "That would be... %s!" % (", ".join(x['name'] for x in whitelist_riders))

        self.msg_contents(message)

    def reset_lazy_riders(self):
        # Reset the boarding number for the people who missed their chance to ride
        if hasattr(self, 'whitelist_riders'):
            for rider in self.whitelist_riders:
                # Note: This will be done to those who boarded AND didn't board
                # For the boarders, it's okay because when they return they are given a new ticket number
                # that will clobber this one
                rider['obj'].db.chimera_line_index = self.db.next_ticket_number
                self.db.next_ticket_number = self.db.next_ticket_number + 1
        

class ChimeraBoardingZone(DefaultRoom):
    # Have the room destroy itself if no one ever shows up after 2 minutes, or if everyone leaves the room

    def at_object_creation(self):
        super(ChimeraBoardingZone, self).at_object_creation()

        #self.db.interval = 5 # Every X seconds it updates the room
        #TICKER_HANDLER.add(interval=self.db.interval, callback=self.update_loop, idstring="the_ride")

        # Constants
        self.db.no_show_timeout = 60 * 2 # Value in seconds
        

        #self.cmdset.add_default(CmdSetLineRoom)

    def at_object_receive(self, moved_obj, source_location, **kwargs):
        #self.msg_contents("ChimeraBoardingZone: object receive")

        #moved_obj.db.chimera_line_index = self.db.next_ticket_number
        #self.db.next_ticket_number = self.db.next_ticket_number + 1

        return super(ChimeraBoardingZone, self).at_object_receive(moved_obj, source_location, **kwargs)

    def update_loop(self):
        pass
        