import random
import datetime

from evennia import CmdSet, Command
from evennia import create_object
from evennia import DefaultRoom
from evennia import DefaultExit
from evennia import TICKER_HANDLER

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