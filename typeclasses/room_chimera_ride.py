import random
import datetime

from evennia import CmdSet, Command
from evennia import create_object
from evennia import DefaultRoom
from evennia import DefaultExit
from evennia import TICKER_HANDLER

from typeclasses.room_chimera_exit import ChimeraExitRoom


# Thanks for joining us on the ride today. Now, according to my notes, you're a group of [roles]? Wow! Well remember to [special command] when the time is right.
DATA_ROLES = [
    { "msg": "Thieves",             "command_name": "steal", },
    { "msg": "Pirates",             "command_name": "loot", },
    { "msg": "Scientists",          "command_name": "research", },
    { "msg": "Tourists",            "command_name": "tour", },
    { "msg": "Space Cadets",        "command_name": "trek", },
    { "msg": "Coal Miners",         "command_name": "mine", },
    { "msg": "Rock Band Musicians", "command_name": "rock", },
    { "msg": "Test Subjects",       "command_name": "endure", },
    { "msg": "Animal Trainers",     "command_name": "", },
    { "msg": "Wizards",             "command_name": "conjure", },
    { "msg": "Athletes",            "command_name": "train", },
    { "msg": "Students",            "command_name": "study", },
    { "msg": "Concert Goers",       "command_name": "listen", },
    { "msg": "Game Developers",     "command_name": "debug", },
    { "msg": "Writers",             "command_name": "write", },
    { "msg": "Teachers",            "command_name": "teach", },
    { "msg": "Car Mechanics",       "command_name": "fix", },
    { "msg": "Billionaires",        "command_name": "invest", },
    { "msg": "Actors",              "command_name": "act", },
    { "msg": "New Hires",           "command_name": "work", },
    { "msg": "Pilots",              "command_name": "fly", },
    { "msg": "Settlers",            "command_name": "settle", },
]

# You came to the park at a really special time. [main problem]. And hey, we could really use your help! But it seems like we're having some trouble for some reason.
DATA_MAIN_PROBLEMS = [
    { "msg": "Our Chimera is sick!", },
    { "msg": "Our Chimera needs exercise!", },
    { "msg": "Our Chimera is hungry!", },
    { "msg": "Our Chimera wants to take a nap but it has insomnia!", },
    { "msg": "Our Chimera lost its memory!", },
    { "msg": "A new ride is malfunctioning!", },
    { "msg": "Someone hacked the park security network!", },
    { "msg": "There's a bad storm coming!", },
    { "msg": "The park is running out of money!", },
    { "msg": "Someone's been trying to kidnap the Chimera!", },
    { "msg": "Booby traps have been placed around the park!", },
    { "msg": "An artifact has been stolen!", },
    { "msg": "We've lost communication with a far off base!", },
    { "msg": "We have to rescue something!", },
    { "msg": "We're scouting out a new territory!", },
    { "msg": "We found a treasure map, but don't know how to decipher it!", },
]

DATA_VILLAIN = [
    { "msg": "a mad scientist", },
    { "msg": "a sentient robot", },
    { "msg": "an angry ancient god", },
    { "msg": "an alien", },
    { "msg": "a vampire King", },
    { "msg": "a mummy", },
    { "msg": "a ghost", },
    { "msg": "a company executive", },
    { "msg": "a psychic child", },
    { "msg": "a time traveler", },
    { "msg": "an overachieving college student", }, # I've gotta maintain my magna cum laude status. I'll definitely get into grad school with this thesis
    { "msg": "another Chimera", },
    { "msg": "a pirate captain", },
    { "msg": "a cursed object", },
]


# Events need: setup, interactive bit, ending, transition out


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
        delay = 5
        
        if index == 0:
            return delay # Slight delay with no text for people to enter
        elif index == 1:

            ride_role = random.choice(DATA_ROLES)
            ride_problem = random.choice(DATA_MAIN_PROBLEMS)
            ride_villain = random.choice(DATA_VILLAIN)

            msg = ""
            msg += "|y> auto-advance|n" + "\n"

            msg += "Thanks for joining us on the ride today. Now, according to my notes, you're a group of %s? Wow!\n" % (ride_role['msg'])
            msg += "Well remember to %s when the time is right.\n" % (ride_role['command_name'])

            msg += "You came to the park at a really special time. %s And hey, we could really use your help! But it seems like we're having some trouble for some reason.\n" % (ride_problem['msg'])

            msg += "Also, the villain is %s!\n" % (ride_villain['msg'])

            self.msg_contents(msg)

            return delay
        elif index == 2:
            msg = ""
            msg += "|y> auto-advance|n" + "\n"
            msg += "Second ride event"

            self.msg_contents(msg)

            return delay
        elif index == 3:
            msg = ""
            msg += "|y> auto-advance|n" + "\n"
            msg += "Third ride event"

            self.msg_contents(msg)

            return delay

        return -1