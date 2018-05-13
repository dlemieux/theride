import random
import datetime

from evennia import CmdSet, Command
from evennia import create_object
from evennia import DefaultRoom, DefaultObject
from evennia import DefaultExit
from evennia import TICKER_HANDLER

from typeclasses.config_all import *

class WalkwayRoom(DefaultRoom):
    """
    This is the walkway from the Entrance to the Courtyard.
    It has an intercom that gives players a personalized intro into the park while
    they travel along an automated walkway.
    """

    messages = (
        "Intercom: \"Welcome to The Park!\"",
        "Intercom: \"By participating in rides and attractions you can earn Park Points!\"",
        "Intercom: \"Spend your Park Points at any gift shop to get wonderful prizes!\"",
        )
    cur_message_index = 0

    def at_object_creation(self):
        super(WalkwayRoom, self).at_object_creation()

        self.db.interval = 8 # Every X seconds it updates the room

        TICKER_HANDLER.add(interval=self.db.interval, callback=self.update_intercom, idstring="the_ride")

    def update_intercom(self, *args, **kwargs):
        
        #self.msg_contents(self.contents) # This is a list of all things in the room
        
        message = "|y>|n\n"
        message += self.messages[self.cur_message_index]

        self.cur_message_index = (self.cur_message_index + 1) % len(self.messages)

        self.msg_contents(message)


class WalkwayTv(DefaultObject):
    messages = (
        "Smiling people gather at the gate. \"Mythari Park is the world's best mythical creature safari and theme park!\"",
        "A park trainer pours kibble into a trough as several three-headed dogs gather. \"Our staff works tirelessly around the clock to ensure our creatures are happy and healthy.\"",
        "A group of school children looks on in awe as a dragon snorts out smoke rings. \"Our legendary animals have willingly chosen to find sanctuary here due to their love of humans!\"",
        "A beast made of scales, fur and feathers is being fitted with a cart full of seats. \"Visit our most popular ride: the |rChimera|n! A shapeshifting adventure on a shapeshifting creature!\"",
        "A screen full of flames. \"Coming Soon... The Temple of the Phoenix!\"",
        )
    
    def at_object_creation(self):
        self.locks.add("get:false()")

    def return_appearance(self, looker, **kwargs):
        string = random.choice(self.messages)
        looker.msg(string)