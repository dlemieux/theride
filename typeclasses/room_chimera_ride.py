import random
import datetime

from evennia import CmdSet, Command
from evennia import create_object
from evennia import DefaultRoom
from evennia import DefaultExit
from evennia import TICKER_HANDLER

from typeclasses.room_chimera_exit import ChimeraExitRoom

from typeclasses.content_ride_data import DATA_ROLES
from typeclasses.content_ride_data import DATA_MAIN_PROBLEMS
from typeclasses.content_ride_data import DATA_VILLAIN
from typeclasses.content_ride_data import DATA_RIDE_EVENT_SECTIONS
from typeclasses.content_ride_data import DEFAULT_EVENT_DELAY


ADD_EVENT_NAME_PREFIX = True


class CmdRiderParticipate(Command):
    """
    Command to participate in the ride.
    """
    key = "participate"
    aliases = list(x['command_name'] for x in DATA_ROLES)
    locks = "cmd:all()"
    help_category = "The Ride"

    def func(self):
        """Implements the command."""
        
        caller = self.caller
        location = caller.location

        # If it's too early, then ignore commands
        if not hasattr(location, 'ride_role'):
            return

        # Determine if they used the correct word
        user_command = self.cmdstring.strip().lower()
        expected_command = location.ride_role['command_name'].strip().lower()

        if not user_command == expected_command:
            caller.msg("That command is not appropriate at this time. Use [|g%s|n] instead." % (expected_command))
            return

        # Commented out old implementation that would allow multiple types of commands at once
        # Determine the exact alias they wrote that triggered the command, and look up the appropriate text
        #cmd_options = filter(lambda x: x['command_name'].strip().lower() == user_command, DATA_ROLES)
        #if len(cmd_options) == 0:
        #    caller.msg("Unknown command: '%s'" % (user_command))
        # Use the first result
        #role_info = cmd_options[0]

        action_msg = location.ride_role['action_msg']
        
        msg = "  |c%s|n %s!" % (caller.name, action_msg)

        location.msg_contents(msg)

class CmdSetChimeraRide(CmdSet):
    """This groups the commands for people."""
    key = "Chimera Ride Commands"

    def at_cmdset_creation(self):
        """Called at first cmdset creation"""
        self.add(CmdRiderParticipate())

class ChimeraRideRoom(DefaultRoom):
    def at_object_creation(self):
        super(ChimeraRideRoom, self).at_object_creation()

        desc = ""
        desc += "You are now on the ride."
        self.db.desc = desc

        self.cmdset.add_default(CmdSetChimeraRide)

        self.build_plot_events()

        self.db.interval = 1 # Every X seconds it updates the room
        TICKER_HANDLER.add(interval=self.db.interval, callback=self.update_loop, idstring="the_ride")

    def build_plot_events(self):
        """
        This method fills properties on this location object with the details of the rider's experience.
        """

        # Determine the initial plot
        self.ride_role = random.choice(DATA_ROLES)
        self.ride_problem = random.choice(DATA_MAIN_PROBLEMS)
        self.ride_villain = random.choice(DATA_VILLAIN)

        # All the events that will happen
        self.ride_events = []

        # Set up the initial story setup
        self.ride_events.append({
            'msg': "Thanks for joining us on the ride today. Now, according to my notes, you're a group of ROLE? Wow!",
            'delay': DEFAULT_EVENT_DELAY,
        })

        self.ride_events.append({
            'msg': "Well remember to ACTION when the time is right.",
            'delay': DEFAULT_EVENT_DELAY,
        })

        self.ride_events.append({
            'msg': "You came to the park at a really special time. PROBLEM And hey, we could really use your help! But it seems like we're having some trouble for some reason.",
            'delay': DEFAULT_EVENT_DELAY,
        })

        self.ride_events.append({
            'msg': "And you'll never believe it, but our efforts keep being thwarted by VILLAIN!",
            'delay': DEFAULT_EVENT_DELAY,
        })

        # Set up all the sections
        for section_info in DATA_RIDE_EVENT_SECTIONS:
            # Choose the random scenario within the section options
            section_option = random.choice(section_info['options'])

            # All events in this section need to be added
            for single_event in section_option['events']:
                    
                if ADD_EVENT_NAME_PREFIX:
                    single_event['msg'] = "(%s->%s) %s" % (section_info['section_name'], section_option['option_name'], single_event['msg'])

                self.ride_events.append(single_event)

        self.ride_events.append({
            'msg': "The line attendant appears before you. You did it! We no longer have to worry about VILLAIN, and it's all thanks to you!",
            'delay': DEFAULT_EVENT_DELAY,
        })

        self.ride_events.append({
            'msg': self.ride_problem['end_line'],
            'delay': DEFAULT_EVENT_DELAY,
        })

        self.ride_events.append({
            'msg': "Everything is finally as it should be again. The Chimera brings you to the ride platform and grunts in thanks.\nThe line attendant beams with pride. \"Who knew a group of ROLE would save the day! See you next time.\" She waves happily as the shoulder harnesses lift and you are free to exit the ride.",
            'delay': DEFAULT_EVENT_DELAY,
        })

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

            return DEFAULT_EVENT_DELAY # Slight delay with no text for people to enter
        else: # Running the events

            # See if we are out of events
            if len(self.ride_events) == 0:
                return -1

            # We have more events
            cur_event = self.ride_events[0]
            self.ride_events = self.ride_events[1:] # Remove the front element

            msg = ""
            msg += "|y> auto-advance|n" + "\n"
            
            cur_event_msg = "%s" % (cur_event['msg'])
            cur_event_msg = self.apply_special_dialog_rules(cur_event_msg)

            msg += cur_event_msg

            self.msg_contents(msg)

            return cur_event['delay']

    def apply_special_dialog_rules(self, msg):

        villain_name = self.ride_villain['msg']
        role_name = self.ride_role['msg']
        action_name = self.ride_role['command_name']
        problem_desc = self.ride_problem['msg']

        # VILLAIN: Example 'a ghost'
        villain_replace = "|c%s|n" % (villain_name)
        msg = msg.replace('VILLAIN', villain_replace)

        # ROLE: Example 'Students'
        role_replace = "|c%s|n" % (role_name)
        msg = msg.replace('ROLE', role_replace)

        # ACTION: Example 'study'
        action_replace = "[|g%s|n]" % (action_name)
        msg = msg.replace('ACTION', action_replace)

        # PROBLEM: Example 'The Chimera has insomnia!'
        msg = msg.replace('PROBLEM', problem_desc)

        # Chimera
        msg = msg.replace('Chimera', '|rChimera|n')

        return msg


