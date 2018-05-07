"""
Room

Rooms are simple containers that has no location of their own.

"""

import random
import datetime

from evennia import CmdSet, Command
from evennia import create_object
from evennia import DefaultRoom
from evennia import DefaultExit
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
        "  |WWelcome to The Park!|n",
        "  |WBy participating in rides and attractions you can earn Park Points!|n",
        "  |WSpend your Park Points at any gift shop to get wonderful prizes!|n",
        )
    cur_message_index = 0

    def at_object_creation(self):
        super(WalkwayRoom, self).at_object_creation()

        self.db.interval = 8 # Every X seconds it updates the room

        TICKER_HANDLER.add(interval=self.db.interval, callback=self.update_intercom, idstring="the_ride")

    def update_intercom(self, *args, **kwargs):
        
        #self.msg_contents(self.contents) # This is a list of all things in the room
        
        message = "|y> Intercom: auto-advance\n"
        message += self.messages[self.cur_message_index]

        self.cur_message_index = (self.cur_message_index + 1) % len(self.messages)

        self.msg_contents(message)


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
            caller.msg("Hot Dog Vendor: \"Gee, I'd love to give you a hot dog but you don't have the $2!\nAnd I gotta make a living here.\"")
        else:
            caller_msg = ""
            caller_msg += "(2 points were deducted from your account)\n"
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
        #self.msg_contents("Seconds elapsed: %s" % seconds_elapsed)

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
        caller.location.msg_contents("Someone made a suggestion", exclude=caller)


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
                        rider.move_to(new_exit_room)

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

class ChimeraExitRoom(DefaultRoom):
    def at_object_creation(self):
        super(ChimeraExitRoom, self).at_object_creation()

        desc = ""
        desc += "Thank you for riding!\n"
        desc += "If you check your |ginventory|n you will see the photo that was taken."
        desc += "You have also all been given 2 points for riding with us today!"

        # Set up an exit in the room that they can take
        # DALE: This needs to match the current database you are running on
        gift_shop_room = "#228" #self.search("ChimeraGiftShop")

        typeclass = "typeclasses.exits.Exit"
        exit_obj = create_object(typeclass, "gift shop", self, aliases=["gift","shop"], destination=gift_shop_room)
        exit_obj.db.desc = "The way to the gift shop."

        self.db.desc = desc

    # TODO: Destroy this room when the last person leaves


