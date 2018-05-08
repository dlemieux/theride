import random
import datetime

from evennia import CmdSet, Command
from evennia import create_object
from evennia import DefaultRoom
from evennia import DefaultExit
from evennia import TICKER_HANDLER

from typeclasses.room_chimera_boarding_zone import ChimeraBoardingZone


class CmdLineLength(Command):
    """
    Command to display your position in line.
    """
    key = "line length"
    aliases = ["line", "length"]
    locks = "cmd:all()"
    help_category = "The Ride"

    def func(self):
        caller = self.caller
        location = caller.location

        # TODO: Iterate on location contents to determine your position in line


class CmdBuyHotDog(Command):
    """
    Command to buy a hot dog
    """
    key = "buy hot dog"
    aliases = ["buy dog","buy hot"]
    locks = "cmd:all()"
    help_category = "The Ride"

    def func(self):
        hot_dog_price = 2

        caller = self.caller;
        location = caller.location

        # Check if the user has enough money
        player_points = caller.db.pass_points
        
        if player_points < hot_dog_price:
            caller.msg("Hot Dog Vendor: \"Gee, I'd love to give you a hot dog but you don't have the %s points!\nAnd I gotta make a living here.\"" % (hot_dog_price))
        else:
            caller_msg = ""
            caller_msg += "(%s points were deducted from your account)\n" % (hot_dog_price)
            caller_msg += "You eat the hot dog and exclaim loudly about how that was the best hot dog you've ever had!"

            room_msg = "  |C%s ate a hot dog. So tasty!|n" % (caller.name)

            caller.db.pass_points = player_points - hot_dog_price # Subtract the money from their account
            caller.msg(caller_msg) # Message the player
            location.msg_contents(room_msg , exclude=(caller)) # Message everyone else in the room


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
        self.add(CmdBuyHotDog())


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

        log_enabled = False
        if hasattr(self, 'db') and hasattr(self.db, 'log_enabled') and self.db.log_enabled:
            log_enabled = True

        if log_enabled:
            self.msg_contents("Seconds elapsed: %s" % seconds_elapsed)

        # Determine whether we are waiting for ride to return or waiting for people to board, or sending off the people after time out
        if self.db.room_state == 0:
            # See if you should keep waiting or advance to state 1
            if seconds_elapsed >= self.db.between_cars_delay:
                # Announce that a new car has arrived

                self.last_ride_time = now # Update to current time

                msg = "|y> Line Attendant: auto-message|n\n"
                msg += "  The next car has arrived! Please [|gboard|n] if you are next in line!"
                self.msg_contents(msg)

                # Make a whitelist for the people who can board
                create_room = self.build_rider_list()

                if create_room:
                    self.create_new_boarding_zone()

                self.db.room_state = 1 # Advance to boarding phase

        elif self.db.room_state == 1:
            # See if you should keep waiting, or move the car on and wait again in state 0
            if seconds_elapsed >= self.db.boarding_time_delay:
                # Announce that the car is leaving
                msg = "|y> Line Attendant: auto-message|n\n"
                msg += "  The car has left the station! Please wait for the next car to arrive."
                self.msg_contents(msg)

                self.last_ride_time = now # Update to current time

                # Anyone who missed their chance is moved to the back of the line
                self.reset_lazy_riders()

                self.db.room_state = 0 # Switch back to the waiting state

        #self.msg_contents(self.contents) # This is a list of all things in the room
    
    def create_new_boarding_zone(self):
        new_boarding_zone = create_object(ChimeraBoardingZone, key="Boarding Zone")
        # Save room info somewhere so board command can move people there
        self.cur_boarding_zone = new_boarding_zone
        #self.msg_contents("Created new boarding zone: %s" % new_boarding_zone.id)
        
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
            # Only take people with a park pass
            if hasattr(item, "db"):
                if item.db.has_season_pass == True:
                    # Only take people in line
                    if (hasattr(item.db, "chimera_line_index") and item.db.chimera_line_index > 0):
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
        message = "  That would be... %s!" % (", ".join(x['name'] for x in whitelist_riders))

        self.msg_contents(message)

        return len(whitelist_riders) > 0

    def reset_lazy_riders(self):
        # Reset the boarding number for the people who missed their chance to ride
        if hasattr(self, 'whitelist_riders'):
            for rider in self.whitelist_riders:
                # Note: This will be done to those who boarded AND didn't board
                # For the boarders, it's okay because when they return they are given a new ticket number
                # that will clobber this one
                rider['obj'].db.chimera_line_index = self.db.next_ticket_number
                self.db.next_ticket_number = self.db.next_ticket_number + 1
        