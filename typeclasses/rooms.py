"""
Room

Rooms are simple containers that has no location of their own.

"""

import random

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
        "|WIntercom: Welcome to The Park!|n",
        "|WIntercom: By participating in rides and attractions you can earn Park Points!|n",
        "|WIntercom: Spend your Park Points at any gift shop to get wonderful prizes!|n",
        )
    cur_message_index = 0

    def at_object_creation(self):
        super(WalkwayRoom, self).at_object_creation()

        self.db.interval = 5 # Every 10 seconds it updates the room

        TICKER_HANDLER.add(interval=self.db.interval, callback=self.update_intercom, idstring="the_ride")

    def update_intercom(self, *args, **kwargs):
        
        #self.msg_contents(self.contents) # This is a list of all things in the room
        
        message = self.messages[self.cur_message_index]
        self.cur_message_index = (self.cur_message_index + 1) % len(self.messages)

        self.msg_contents(message)
