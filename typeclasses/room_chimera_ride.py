import random
import datetime

from evennia import CmdSet, Command
from evennia import create_object
from evennia import DefaultRoom
from evennia import DefaultExit
from evennia import TICKER_HANDLER

from typeclasses.config_all import *
from typeclasses.room_chimera_exit import ChimeraExitRoom

from typeclasses.content_ride_data import DATA_ROLES
from typeclasses.content_ride_data import DATA_MAIN_PROBLEMS
from typeclasses.content_ride_data import DATA_VILLAIN
from typeclasses.content_ride_data import DATA_RIDE_EVENT_SECTIONS


class CmdRiderParticipate(Command):
    """
    Command to participate in the ride.
    """
    key = "participate"
    aliases = list(x['command_name'] for x in DATA_ROLES)
    locks = "cmd:all()"
    help_category = GAME_HELP_CATEGORY

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

        action_msg = location.ride_role['action_msg']
        
        # If no battle is taking place, simply show the command as normal
        if not hasattr(location, 'ride_villain_battle') or not location.ride_villain_battle:
            msg = "|c%s|n %s!" % (caller.name, action_msg)
            location.msg_contents(msg)
            return

        # Run the villain battle
        if location.ride_villain_battle['state'] == 'idle':
            location.ride_villain_battle['battle_start_time'] = datetime.datetime.utcnow()
            location.ride_villain_battle['state'] = 'battle'
            self.attack_villain(caller, location)

        elif location.ride_villain_battle['state'] == 'battle':
            max_health = location.ride_villain_battle['max_health']
            orig_health = location.ride_villain_battle['health']
            self.attack_villain(caller, location)
            new_health = location.ride_villain_battle['health']

            # Check for first strike
            if orig_health == max_health and new_health < max_health:
                location.msg_contents("\"Ow!\"")

            # Check for half way
            if orig_health > max_health * 0.5 and new_health <= max_health * 0.5:
                location.msg_contents("\"Hey! That's not fair!\"")

            # Check for 3/4
            if orig_health > max_health * 0.25 and new_health <= max_health * 0.25:
                location.msg_contents("\"It's not over yet!\"")

            # Check if killed
            if orig_health > 0 and new_health <= 0:
                location.ride_villain_battle['state'] = 'villain_killed'

        else:
            # Normal message
            msg = "  |c%s|n %s!" % (caller.name, action_msg)
            location.msg_contents(msg)

    def attack_villain(self, caller, location):
        action_msg = location.ride_role['action_msg']
        
        # Determine battle metrics
        is_crit = random.randint(1, 4) == 1
        hit_damage = 10
        if is_crit:
            hit_damage = 15

        msg = ""

        

        msg += "|c%s|n %s and deals |c%s|n points of damage!" % (caller.name, action_msg, hit_damage)

        if is_crit:
            msg += " Critical hit!"
        
        # There may be race condition issues with this and multiple players
        
        new_health = location.ride_villain_battle['health'] - hit_damage

        if new_health < 0:
            new_health = 0

        location.ride_villain_battle['health'] = new_health
        
        max_health = location.ride_villain_battle['max_health']

        # Add the villains health stats
        health_bar_msg = self.build_health_bar(new_health, max_health)

        msg += "\nHealth for |c%s|n: %s %s/%s HP" % (location.ride_villain['msg'], health_bar_msg, new_health, max_health)

        location.msg_contents(msg)

    def build_health_bar(self, new_health, max_health):
        # Determine health bars remaining
        num_bars_left = 0
        max_bars = 20

        if new_health > 0:
            num_bars_left = new_health * max_bars / max_health

        # Show the bars
        health_msg = ""
        health_msg += " ||" # Starting bar
        health_msg += "".ljust(num_bars_left, '-')
        health_msg += "".ljust(max_bars - num_bars_left, ' ')
        health_msg += "||" # Ending bar

        return health_msg


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
        desc += "You are strapped into a cart on the back of a mythical creature!"
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
            'msg': "Ride Attendant: \"Thanks for joining us on the ride today. Now, according to my notes, you're a group of ROLE? Wow!\"",
            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
        })

        self.ride_events.append({
            'msg': "Ride Attendant: \"Well remember to ACTION when the time is right.\"",
            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
        })

        self.ride_events.append({
            'msg': "Ride Attendant: \"You came to the park at an unusual time. PROBLEM And hey, we could really use your help! But it seems like we're having some trouble for some reason.\"",
            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
        })

        self.ride_events.append({
            'msg': "Ride Attendant: \"And you'll never believe it, but our efforts keep being thwarted by VILLAIN!\"",
            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
        })

        if CHIMERA_RIDE_TEST_BATTLE:
            # Skip the middle sections
            
            self.ride_events.append({
                'msg': "VILLAIN_PICTURE",
                'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            })
            self.ride_events.append({
                'msg': "TEST: START BATTLE: \"You fools! You're just a bunch of ROLE. What are you going to do, ACTION me to death?\"",
                'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                'type': 'start_villain_battle',
            })
        else:
            # Set up all the sections
            for section_info in DATA_RIDE_EVENT_SECTIONS:
                # Choose the random scenario within the section options
                section_option = random.choice(section_info['options'])

                # All events in this section need to be added
                add_event_name_first = True # Only add the debug info for the first event in an option
                for single_event in section_option['events']:
                    
                    if CHIMERA_RIDE_ADD_EVENT_NAME_PREFIX:
                        if add_event_name_first:
                            single_event['msg'] = "(%s->%s) %s" % (section_info['section_name'], section_option['option_name'], single_event['msg'])
                            add_event_name_first = False

                    self.ride_events.append(single_event)

        self.ride_end_events = []
        self.ride_end_events.append({
            'msg': "The ride attendant appears once more.\nRide Attendant: \"You did it! We no longer have to worry about VILLAIN, and it\'s all thanks to you! And I think we've even solved our problem from earlier.\"",
            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
        })

        self.ride_end_events.append({
            'msg': self.ride_problem['end_line'],
            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
        })

        self.ride_end_events.append({
            'msg': "Everything is finally as it should be. The Chimera lowers itself on the exit platform and grunts in appreciation.\nRide Attendant: \"Who knew a group of ROLE would save the day! Join us again some time.\"\nThey wave happily as the shoulder harnesses lift and you are finally free to exit.",
            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
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
                    new_exit_room = create_object(ChimeraExitRoom, key="Chimera Ride Exit")

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
            return CHIMERA_RIDE_DEFAULT_EVENT_DELAY # Slight delay with no text for people to enter
        else: # Running the events

            # Detect a server crash
            if not hasattr(self, 'ride_role'):
                self.msg_contents("Ride attendant: \"Sorry, we had to perform maintenance on the ride and need you to exit for now. We hope you get back in line to fully experience the wonders of the |rChimera|n!\"")
                return -1 # Trigger the end

            # If the villain battle has started, then all rules are different
            if hasattr(self, 'ride_villain_battle') and self.ride_villain_battle:
                return self.handle_villain_battle()

            # See if we are out of events
            if len(self.ride_events) == 0:
                # See if we still need to run through the ride end events
                if len(self.ride_end_events) > 0:
                    self.ride_events = self.ride_end_events
                    self.ride_end_events = []
                else:
                    return -1 # Finished

            # We have more events
            cur_event = self.ride_events[0]
            self.ride_events = self.ride_events[1:] # Remove the front element

            # See if we are starting the villain battle!
            if 'type' in cur_event and cur_event['type'] == 'start_villain_battle':
                self.ride_villain_battle = {
                    'start_time': datetime.datetime.utcnow(),
                    'battle_start_time': None, # This is set when the first attack hits
                    'max_health': 100,
                    'health': 100,
                    'state': 'idle',
                    'idle_warning_delay': 5,
                    'idle_warning_1': False,
                    'idle_warning_2': False,
                    'battle_length_seconds': 20,
                }

            # Build the appropriate message to show the room
            self.send_room_message(cur_event['msg'])

            return cur_event['delay']

    def handle_villain_battle(self):
        now = datetime.datetime.utcnow()

        # Scenario where no one is touching anything
        if self.ride_villain_battle['state'] == 'idle':
            elapsed_since_start = now - self.ride_villain_battle['start_time']
            elapsed_seconds = elapsed_since_start.seconds
            
            idle_warning_time = self.ride_villain_battle['idle_warning_delay']

            if elapsed_seconds >= idle_warning_time * 1 and not self.ride_villain_battle['idle_warning_1']:
                msg = "\"What? You're not even going to try and fight?\""
                self.ride_villain_battle['idle_warning_1'] = True
                self.send_room_message(msg)

            if elapsed_seconds >= idle_warning_time * 2 and not self.ride_villain_battle['idle_warning_2']:
                msg = "\"Are you waiting for me to foolishly explain my entire plot so you can escape and stop me or something?\""
                self.ride_villain_battle['idle_warning_2'] = True
                self.send_room_message(msg)

            if elapsed_seconds >= idle_warning_time * 3:
                msg = "Your pacifist response seems to have worked, as your nemesis dies of boredom in front of you."
                self.ride_villain_battle['idle_warning_3'] = True
                self.ride_villain_battle['state'] = 'did_not_fight'
                self.send_room_message(msg)
                return CHIMERA_RIDE_DEFAULT_EVENT_DELAY # Give them time to read

        elif self.ride_villain_battle['state'] == 'battle':
            elapsed = now - self.ride_villain_battle['battle_start_time']
            if elapsed.seconds >= self.ride_villain_battle['battle_length_seconds']:
                # They lost for taking too long
                self.ride_villain_battle['state'] = 'villain_left'
                msg = "\"I won't give you the satisfaction of beating me. I'm outta here!\""
                self.send_room_message(msg)

        elif self.ride_villain_battle['state'] == 'did_not_fight' or self.ride_villain_battle['state'] == 'villain_left':
            self.ride_villain_battle_results = self.ride_villain_battle
            self.ride_villain_battle = None # Return to normal execution

        elif self.ride_villain_battle['state'] == 'villain_killed':
            # Queue up messages to be played
            self.ride_events.append({
                'msg': "You've done it!",
                'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            })

            for single_event in self.ride_villain['defeat_events']:
                self.ride_events.append(single_event)

            # Clear the villain battle details so the messaging system resumes as normal
            self.ride_villain_battle_results = self.ride_villain_battle # Store it in case we need it later
            self.ride_villain_battle = None # Return to normal execution

        return 0 # No delay, just keep us updated

    def send_room_message(self, msg):
        room_msg = ""
        room_msg += "|y>|n" + "\n"

        msg = self.apply_special_dialog_rules(msg)
        room_msg += msg

        self.msg_contents(room_msg)

    def apply_special_dialog_rules(self, msg):

        villain_name = self.ride_villain['msg']
        role_name = self.ride_role['msg']
        action_name = self.ride_role['command_name']
        problem_desc = self.ride_problem['msg']

        villain_picture = self.ride_villain['picture']
        villain_picture = villain_picture.replace("\n", "", 1) # Strip the leading newline
        villain_picture = villain_picture.replace("|", "||") # Escape the | character

        # ROLE: Example 'Students'
        role_replace = "|c%s|n" % (role_name)
        msg = msg.replace('ROLE', role_replace)

        # ACTION: Example 'study'
        action_replace = "[|g%s|n]" % (action_name)
        msg = msg.replace('ACTION', action_replace)

        # PROBLEM: Example 'The Chimera has insomnia!'
        msg = msg.replace('PROBLEM', problem_desc)

        # VILLAIN_PICTURE
        msg = msg.replace('VILLAIN_PICTURE', villain_picture)

        # VILLAIN: Example 'a ghost'
        villain_replace = "|c%s|n" % (villain_name)
        msg = msg.replace('VILLAIN', villain_replace)

        # Chimera
        msg = msg.replace('Chimera', '|rChimera|n')

        return msg


