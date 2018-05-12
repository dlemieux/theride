"""
Object

The Object is the "naked" base class for things in the game world.

Note that the default Character, Room and Exit does not inherit from
this Object, but from their respective default implementations in the
evennia library. If you want to use this class as a parent to change
the other types, you can do so by adding this as a multiple
inheritance.

"""

import datetime
import random

from evennia import CmdSet
from evennia import Command
from evennia import create_object
from evennia import DefaultObject

from typeclasses.config_all import *

class Object(DefaultObject):
    """
    This is the root typeclass object, implementing an in-game Evennia
    game object, such as having a location, being able to be
    manipulated or looked at, etc. If you create a new typeclass, it
    must always inherit from this object (or any of the other objects
    in this file, since they all actually inherit from BaseObject, as
    seen in src.object.objects).

    The BaseObject class implements several hooks tying into the game
    engine. By re-implementing these hooks you can control the
    system. You should never need to re-implement special Python
    methods, such as __init__ and especially never __getattribute__ and
    __setattr__ since these are used heavily by the typeclass system
    of Evennia and messing with them might well break things for you.


    * Base properties defined/available on all Objects

     key (string) - name of object
     name (string)- same as key
     aliases (list of strings) - aliases to the object. Will be saved to
                           database as AliasDB entries but returned as strings.
     dbref (int, read-only) - unique #id-number. Also "id" can be used.
                                  back to this class
     date_created (string) - time stamp of object creation
     permissions (list of strings) - list of permission strings

     account (Account) - controlling account (if any, only set together with
                       sessid below)
     sessid (int, read-only) - session id (if any, only set together with
                       account above). Use `sessions` handler to get the
                       Sessions directly.
     location (Object) - current location. Is None if this is a room
     home (Object) - safety start-location
     sessions (list of Sessions, read-only) - returns all sessions connected
                       to this object
     has_account (bool, read-only)- will only return *connected* accounts
     contents (list of Objects, read-only) - returns all objects inside this
                       object (including exits)
     exits (list of Objects, read-only) - returns all exits from this
                       object, if any
     destination (Object) - only set if this object is an exit.
     is_superuser (bool, read-only) - True/False if this user is a superuser

    * Handlers available

     locks - lock-handler: use locks.add() to add new lock strings
     db - attribute-handler: store/retrieve database attributes on this
                             self.db.myattr=val, val=self.db.myattr
     ndb - non-persistent attribute handler: same as db but does not create
                             a database entry when storing data
     scripts - script-handler. Add new scripts to object with scripts.add()
     cmdset - cmdset-handler. Use cmdset.add() to add new cmdsets to object
     nicks - nick-handler. New nicks with nicks.add().
     sessions - sessions-handler. Get Sessions connected to this
                object with sessions.get()

    * Helper methods (see src.objects.objects.py for full headers)

     search(ostring, global_search=False, attribute_name=None,
             use_nicks=False, location=None, ignore_errors=False, account=False)
     execute_cmd(raw_string)
     msg(text=None, **kwargs)
     msg_contents(message, exclude=None, from_obj=None, **kwargs)
     move_to(destination, quiet=False, emit_to_obj=None, use_destination=True)
     copy(new_key=None)
     delete()
     is_typeclass(typeclass, exact=False)
     swap_typeclass(new_typeclass, clean_attributes=False, no_default=True)
     access(accessing_obj, access_type='read', default=False)
     check_permstring(permstring)

    * Hooks (these are class methods, so args should start with self):

     basetype_setup()     - only called once, used for behind-the-scenes
                            setup. Normally not modified.
     basetype_posthook_setup() - customization in basetype, after the object
                            has been created; Normally not modified.

     at_object_creation() - only called once, when object is first created.
                            Object customizations go here.
     at_object_delete() - called just before deleting an object. If returning
                            False, deletion is aborted. Note that all objects
                            inside a deleted object are automatically moved
                            to their <home>, they don't need to be removed here.

     at_init()            - called whenever typeclass is cached from memory,
                            at least once every server restart/reload
     at_cmdset_get(**kwargs) - this is called just before the command handler
                            requests a cmdset from this object. The kwargs are
                            not normally used unless the cmdset is created
                            dynamically (see e.g. Exits).
     at_pre_puppet(account)- (account-controlled objects only) called just
                            before puppeting
     at_post_puppet()     - (account-controlled objects only) called just
                            after completing connection account<->object
     at_pre_unpuppet()    - (account-controlled objects only) called just
                            before un-puppeting
     at_post_unpuppet(account) - (account-controlled objects only) called just
                            after disconnecting account<->object link
     at_server_reload()   - called before server is reloaded
     at_server_shutdown() - called just before server is fully shut down

     at_access(result, accessing_obj, access_type) - called with the result
                            of a lock access check on this object. Return value
                            does not affect check result.

     at_before_move(destination)             - called just before moving object
                        to the destination. If returns False, move is cancelled.
     announce_move_from(destination)         - called in old location, just
                        before move, if obj.move_to() has quiet=False
     announce_move_to(source_location)       - called in new location, just
                        after move, if obj.move_to() has quiet=False
     at_after_move(source_location)          - always called after a move has
                        been successfully performed.
     at_object_leave(obj, target_location)   - called when an object leaves
                        this object in any fashion
     at_object_receive(obj, source_location) - called when this object receives
                        another object

     at_traverse(traversing_object, source_loc) - (exit-objects only)
                              handles all moving across the exit, including
                              calling the other exit hooks. Use super() to retain
                              the default functionality.
     at_after_traverse(traversing_object, source_location) - (exit-objects only)
                              called just after a traversal has happened.
     at_failed_traverse(traversing_object)      - (exit-objects only) called if
                       traversal fails and property err_traverse is not defined.

     at_msg_receive(self, msg, from_obj=None, **kwargs) - called when a message
                             (via self.msg()) is sent to this obj.
                             If returns false, aborts send.
     at_msg_send(self, msg, to_obj=None, **kwargs) - called when this objects
                             sends a message to someone via self.msg().

     return_appearance(looker) - describes this object. Used by "look"
                                 command by default
     at_desc(looker=None)      - called by 'look' whenever the
                                 appearance is requested.
     at_get(getter)            - called after object has been picked up.
                                 Does not stop pickup.
     at_drop(dropper)          - called when this object has been dropped.
     at_say(speaker, message)  - by default, called if an object inside this
                                 object speaks

     """
    pass
    
    
class Heavy(DefaultObject):
    "Heavy object"
    def at_object_creation(self):
        "Called whenever a new object is created"
        
        # lock the object down by default
        self.locks.add("get:false()")
        
        # the default "get" command looks for this Attribute in order
        # to return a customized error message (we just happen to know
        # this, you'd have to look at the code of the 'get' command to
        # find out).
        self.db.get_err_msg = "This is too heavy to pick up."


class ParkAttendant(DefaultObject):
    "Park Attendant"
    def at_object_creation(self):
        "Called whenever a new object is created"
        
        # lock the object down by default
        self.locks.add("get:false()")
        
        self.db.desc = "They are standing there smiling."
        self.db.get_err_msg = "No touching!"
        self.db.talk_to_msg = "Hello!"
        self.db.consider_msg = "This person is much stronger than you."

class ConstructionFence(DefaultObject):
    "Fence"
    def at_desc(self, looker=None):
        if looker:
            looker.db.look_fence = True


class LineLengthSign(DefaultObject):
    "Line Length Sign"

    def at_object_creation(self):
        self.locks.add("get:false()")
        self.db.get_err_msg = "This is too heavy to pick up."

    def return_appearance(self, looker, **kwargs):
        # Get the real value from the other room
        line_room = self.search("Waiting in Line", global_search=True) # Room 213
        val = line_room.get_line_length()

        if val == 1:
            return "The sign says: \"There is |c1|n person in line for the |rChimera|n.\""
        else:
            return "The sign says: \"There are |c%s|n people in line for the |rChimera|n.\"" % (val)


class ParkPass(DefaultObject):
    """
    This implements a user's park pass.
    """

    def at_object_creation(self):
        """Called when object is first created."""
        super(ParkPass, self).at_object_creation()
        
        # Set system properties
        self.db.desc = "Your very own park pass! Use [|gread pass|n] to see the details!"
        self.db.drop_err_msg = "The Park Pass is the most important item you own! Don't be so careless!"
        # Make sure they can't drop the pass
        self.locks.add("drop:false()")
        
        # Set custom properties to store for the user
        #self.db.park_points = 0
        now = datetime.datetime.now()
        self.db.creation_date = str(now)


class CmdBuyPass(Command):
    """
    Usage:
        buy pass
        
    This will let you try to buy a pass for the park.
    """
    key = "buy pass"
    aliases = ["buy season pass", "buy a pass", "buy a park pass", "buy park pass", "buy"]
    locks = "cmd:all()"
    help_category = "The Ride"
    
    def func(self):
        """
        Gets a pass from the agent.
        """
        #self.caller.msg("enter CmdBuyPass")
        #self.caller.msg("one")
        #yield 2
        #self.caller.msg("two")
        
        # Option 1: Call method on the clerk to give the pass
        #self.obj.produce_pass(self.caller)
        
        # Option 2 to allow the use of yield statements
        caller = self.caller
        if caller.db.has_season_pass:
            caller.msg("Pass Sales Clerk: Oh hey! How's that pass working out for ya?")
            caller.msg("                  You won't ever need another one. That's a lifetime guarantee!")
            caller.msg("                  (You can use [|gi|n] to view your inventory)")
        else:
            # give the player a pass
            caller.msg("Clerk: Alright! We'll have you all set up in a jiffy!")
            caller.msg("       The pass itself costs |r$9999|n. I'm sure you have that right?")
            caller.msg("       Just a few details to collect first...")
            caller.msg("       *The clerk rummages around*")
            
            yield 3
            

            homeLocation = yield("       Okay, question one. What town are you from?")

            # Loop until the give a valid answer
            while len(homeLocation.strip()) == 0:
                homeLocation = yield("       Pardon? What town are you from?")
            
            # Trim the name of the home location in case it is too long
            maxHomeLength = 40
            if len(homeLocation) > maxHomeLength:
                homeLocation = homeLocation[:maxHomeLength]

            caller.msg("       %s eh... wait... what did you say?" % (homeLocation))
            caller.msg("       Are you THE |g%s from %s|n! I'm your biggest fan!" % (caller.name, homeLocation))
            caller.msg("       Please take this pass for free and enjoy the park! It's an honor!")
            caller.msg("       *The Clerk shouts into the crowd*")
            caller.msg("       Hey everyone! Make way for |g%s from %s|n!" % (caller.name, homeLocation))
            caller.msg("       Here you go! *hands you a pass*")
            caller.msg("       (You can use [|gi|n] to view your inventory)")

            # Set the properties for the pass
            caller.db.has_season_pass = True # maybe store the date they became a pass holder
            caller.db.pass_town = homeLocation
            utcNow = datetime.datetime.utcnow()
            caller.db.pass_create_date = utcNow.strftime("%B %d, %Y") # Ex: October 3, 2018
            caller.db.pass_points = 5

            create_object(ParkPass, key="Park Pass", location=caller)
            #caller.msg("Finished buy pass")


class CmdDestroyPass(Command):
    """
    Usage:
        destroy pass
        
    This is a test command which gets rid of your pass
    """
    key = "destroy pass"
    locks = "cmd:perm(Developer)"
    help_category = "The Ride"
    
    def func(self):
        self.obj.destroy_pass(self.caller)


class CmdSitOnBench(Command):
    """
    Usage:
        sit on bench
        
    This is a test command which gets rid of your pass
    """
    key = "sit on bench"
    aliases = ["sit"]
    locks = "cmd:all()"
    help_category = "The Ride"
    
    def func(self):
        caller = self.caller
        location = self.caller.location

        caller.msg("Don't tell me you're tired already! You just got here!")
        #location.msg_contents("|C%s|n sits on the bench." % (caller.name), exclude=[caller])


class CmdSetPassSalesClerk(CmdSet):
    """
    The cmdset for the pass sales clerk.
    """
    key = "passsales_cmdset"

    def at_cmdset_creation(self):
        """Called at first creation of cmdset"""
        self.add(CmdBuyPass())
        self.add(CmdDestroyPass())
        self.add(CmdSitOnBench()) # TODO: Ideally move this to be a command on a bench object, or on the Entrance room itself

        
class PassSalesClerk(DefaultObject):
    """
    This object represents a pass sales clerk. When people use the
    "buy pass" command on this sales clerk, it will produce one
    pass. This will also set a property on the character
    to make sure they can't get more than one at a time.
    """

    def at_object_creation(self):
        """
        called at creation
        """
        self.locks.add("get:false()")
        self.locks.add("ic:false()")
        
        self.cmdset.add_default(CmdSetPassSalesClerk, permanent=True)
        # these are prototype names from the prototype
        # dictionary above.
        #self.db.get_weapon_msg = "you find |c%s|n."
        self.db.only_one_pass_msg = "Pass Sales Clerk: Oh hey! How's that pass working out for ya?\n                  You won't ever need another one. That's a lifetime guarantee!"
        #self.db.available_weapons = ["knife", "dagger",
        #                             "sword", "club"]

    def destroy_pass(self, caller):
        if caller.db.has_season_pass:
            caller.db.has_season_pass = False
            caller.search("pass", location=caller).delete()
            caller.msg("The pass sales clerk rips up your pass.")
        else:
            caller.msg("You don't have a pass to drop.")
            
     