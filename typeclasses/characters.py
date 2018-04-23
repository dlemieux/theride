"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter


class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """
    
    def at_object_creation(self):
        #self.db.has_id_card = False
        pass


class ParkPassCreator(Character):
    """
    An NPC character to help the player make their park pass
    """
    
    def at_heard_say(self, message, from_obj):
        """
        Echos what they heard
        """
        
        # message will be of the form `<Person> says, "say_text"`
        message = message.split('says, ')[1].strip(' "');
        
        return "%s said: '%s'" % (from_obj, message)
    
    
    def msg(self, text=None, from_obj=None, **kwargs):
        "Custom msg() method reacting to say."

        if from_obj != self:
            # make sure to not repeat what we ourselves said or we'll create a loop
            try:
                # if text comes from a say, `text` is `('say_text', {'type': 'say'})`
                say_text, is_say = text[0], text[1]['type'] == 'say'
            except Exception:
                is_say = False
                
            if is_say:
                # First get the response (if any)
                response = self.at_heard_say(say_text, from_obj)
                
                # If there is a response
                if response != None:
                    # speak ourselves, using the return
                    self.execute_cmd("say %s" % response) # This responds like a real character so others can react appropriately
    
        # this is needed if anyone ever puppets this NPC - without it you would never
        # get any feedback from the server (not even the results of look)
        super(ParkPassCreator, self).msg(text=text, from_obj=from_obj, **kwargs)