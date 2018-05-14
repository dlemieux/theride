"""
Commands

Commands describe the input the account can do to the game.

"""

import random
import datetime

from evennia import CmdSet
from evennia import Command as BaseCommand

from typeclasses.config_all import *

# from evennia import default_cmds

class Command(BaseCommand):
    """
    Inherit from this if you want to create your own command styles
    from scratch.  Note that Evennia's default commands inherits from
    MuxCommand instead.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_cmd(): If this returns True, execution is aborted.
        - parse(): Should perform any extra parsing needed on self.args
            and store the result on self.
        - func(): Performs the actual work.
        - at_post_cmd(): Extra actions, often things done after
            every command, like prompts.

    """
    pass

# -------------------------------------------------------------
#
# The default commands inherit from
#
#   evennia.commands.default.muxcommand.MuxCommand.
#
# If you want to make sweeping changes to default commands you can
# uncomment this copy of the MuxCommand parent and add
#
#   COMMAND_DEFAULT_CLASS = "commands.command.MuxCommand"
#
# to your settings file. Be warned that the default commands expect
# the functionality implemented in the parse() method, so be
# careful with what you change.
#
# -------------------------------------------------------------

# from evennia.utils import utils
#
#
# class MuxCommand(Command):
#     """
#     This sets up the basis for a MUX command. The idea
#     is that most other Mux-related commands should just
#     inherit from this and don't have to implement much
#     parsing of their own unless they do something particularly
#     advanced.
#
#     Note that the class's __doc__ string (this text) is
#     used by Evennia to create the automatic help entry for
#     the command, so make sure to document consistently here.
#     """
#     def has_perm(self, srcobj):
#         """
#         This is called by the cmdhandler to determine
#         if srcobj is allowed to execute this command.
#         We just show it here for completeness - we
#         are satisfied using the default check in Command.
#         """
#         return super(MuxCommand, self).has_perm(srcobj)
#
#     def at_pre_cmd(self):
#         """
#         This hook is called before self.parse() on all commands
#         """
#         pass
#
#     def at_post_cmd(self):
#         """
#         This hook is called after the command has finished executing
#         (after self.func()).
#         """
#         pass
#
#     def parse(self):
#         """
#         This method is called by the cmdhandler once the command name
#         has been identified. It creates a new set of member variables
#         that can be later accessed from self.func() (see below)
#
#         The following variables are available for our use when entering this
#         method (from the command definition, and assigned on the fly by the
#         cmdhandler):
#            self.key - the name of this command ('look')
#            self.aliases - the aliases of this cmd ('l')
#            self.permissions - permission string for this command
#            self.help_category - overall category of command
#
#            self.caller - the object calling this command
#            self.cmdstring - the actual command name used to call this
#                             (this allows you to know which alias was used,
#                              for example)
#            self.args - the raw input; everything following self.cmdstring.
#            self.cmdset - the cmdset from which this command was picked. Not
#                          often used (useful for commands like 'help' or to
#                          list all available commands etc)
#            self.obj - the object on which this command was defined. It is often
#                          the same as self.caller.
#
#         A MUX command has the following possible syntax:
#
#           name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#         The 'name[ with several words]' part is already dealt with by the
#         cmdhandler at this point, and stored in self.cmdname (we don't use
#         it here). The rest of the command is stored in self.args, which can
#         start with the switch indicator /.
#
#         This parser breaks self.args into its constituents and stores them in the
#         following variables:
#           self.switches = [list of /switches (without the /)]
#           self.raw = This is the raw argument input, including switches
#           self.args = This is re-defined to be everything *except* the switches
#           self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#                      no = is found, this is identical to self.args.
#           self.rhs: Everything to the right of = (rhs:'right-hand side').
#                     If no '=' is found, this is None.
#           self.lhslist - [self.lhs split into a list by comma]
#           self.rhslist - [list of self.rhs split into a list by comma]
#           self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#           All args and list members are stripped of excess whitespace around the
#           strings, but case is preserved.
#         """
#         raw = self.args
#         args = raw.strip()
#
#         # split out switches
#         switches = []
#         if args and len(args) > 1 and args[0] == "/":
#             # we have a switch, or a set of switches. These end with a space.
#             switches = args[1:].split(None, 1)
#             if len(switches) > 1:
#                 switches, args = switches
#                 switches = switches.split('/')
#             else:
#                 args = ""
#                 switches = switches[0].split('/')
#         arglist = [arg.strip() for arg in args.split()]
#
#         # check for arg1, arg2, ... = argA, argB, ... constructs
#         lhs, rhs = args, None
#         lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#         if args and '=' in args:
#             lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#             lhslist = [arg.strip() for arg in lhs.split(',')]
#             rhslist = [arg.strip() for arg in rhs.split(',')]
#
#         # save to object properties:
#         self.raw = raw
#         self.switches = switches
#         self.args = args.strip()
#         self.arglist = arglist
#         self.lhs = lhs
#         self.lhslist = lhslist
#         self.rhs = rhs
#         self.rhslist = rhslist
#
#         # if the class has the account_caller property set on itself, we make
#         # sure that self.caller is always the account if possible. We also create
#         # a special property "character" for the puppeted object, if any. This
#         # is convenient for commands defined on the Account only.
#         if hasattr(self, "account_caller") and self.account_caller:
#             if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#                 # caller is an Object/Character
#                 self.character = self.caller
#                 self.caller = self.caller.account
#             elif utils.inherits_from(self.caller, "evennia.accounts.accounts.DefaultAccount"):
#                 # caller was already an Account
#                 self.character = self.caller.get_puppet(self.session)
#             else:
#                 self.character = None
        
class CmdConsider(Command):
    """
    Consider another target.

    Usage:
      consider <target>

    Observes your target and gives an estimation of their abilities in a fight.
    """
    key = "consider"
    aliases = ["cons"]
    locks = "cmd:all()"
    help_category = "General"
    arg_regex = r"\s|$"

    def func(self):
        """
        Handle the consider.
        """
        caller = self.caller
        if not self.args:
            caller.msg("consider <target>")
            return
        else:
            target = caller.search(self.args)
            if not target:
                return

        # Do the action
        if target.db.consider_msg:
            caller.msg(target.db.consider_msg)
        else:
            caller.msg("It could go either way.")


class CmdTalkTo(Command):
    """
    Talk to a target.

    Usage:
      talk to <target>

    Talk to a target person.
    """
    key = "talk to"
    aliases = ["talk"]
    locks = "cmd:all()"
    help_category = "General"
    arg_regex = r"\s|$"

    def func(self):
        """
        Talk to the target.
        """
        caller = self.caller
        if not self.args:
            caller.msg("talk to <target>")
            return
        else:
            target = caller.search(self.args)
            if not target:
                return

        # Do the action
        if target.db.talk_to_msg:
            caller.msg(target.db.talk_to_msg)
        elif target.db.is_player:
            caller.msg("This is another human player. Use [|gsay <message>|n] or [|gwhisper <person> = <message>|n] to send a message.")
        else:
            caller.msg("They have nothing to say.")


class CmdAttack(Command):
    """
    Attack a target.

    Usage:
      attack <target>

    Attack a target.
    """    
    key = "attack"
    aliases = ["cast", "kill"]
    help_category = "General"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        cmdstring = self.cmdstring

        if not self.args:
            if cmdstring == 'attack':
                caller.msg("attack <target>")
            elif cmdstring == 'cast':
                caller.msg("cast <spell> at <target>")
            elif cmdstring == 'kill':
                caller.msg("kill <target>")
            return

        # They used the command
        if cmdstring == 'attack':
            caller.msg("Security Guard: \"Excuuuuse me! We'll have none of that!\"")
        elif cmdstring == 'cast':
            caller.msg("*The security guard taps you on the shoulder*\nSecurity Guard: \"And just what do you think you're doing?\"")
        elif cmdstring == 'kill':
            caller.msg("Security Guard: \"Did you really think you'd get away with that?\"")


class CmdHelpNewbie(Command):
    """
    Display help for new players.

    Usage:
      help newbie

    Display help for new players.
    """    
    key = "help newbie"
    aliases = ["help new", "newbie"]
    #priority = 1
    help_category = GAME_HELP_CATEGORY
    locks = "cmd:all()"

    def func(self):
        caller = self.caller

        string = ""
        string += "\n"
        string += "Welcome to %s!\n" % (GAME_TITLE)
        string += "You're going to do great! Have fun looking around the theme park and riding the |rChimera|n!\n"
        string += "\n"
        string += "Commands:\n"
        string += "  |glook|n, |glook <object>|n:  See the descriptions on people, places, and things.\n"
        string += "  |ginventory|n, |gi|n:         View your inventory.\n"
        string += "  |g<exit name>|n:          Type the name of an exit to use it and enter another room.\n"
        string += "  |gtalk to <character>|n:  Talk to a non-human character in the room.\n"
        string += "\n"
        string += "  |gsay|n:                  Share a message with all human players in the room.\n"
        string += "  |gwhisper <name> = <message>|n: Send a message to one specific human player.\n"
        string += "  |gemote|n, |gpose|n:          Share an emote or pose with all human players in the room.\n"
        string += "                        Ex: |gemote claps wildly!|n\n"
        string += "\n"
        string += "  |gfeedback <your feedback>|n: Send us a message with feedback about the game (bugs, issues, or suggestions) so we can keep making it better!\n"
        string += "\n"
        string += "  |ghelp|n, |ghelp <command>|n: See general help or help for a specific command.\n"
        #string += "  |g|n: \n"

        caller.msg(string)


class CmdExits(Command):
    """
    List the exits.

    Usage:
      exits

    List the exits from this location.
    """    
    key = "exits"
    help_category = "General"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller

        impl = 2
        if impl == 1:
            caller.execute_cmd("look") # The look command will list the exits
        elif impl == 2:
            # Get the look command output and parse it
            lookOutput = caller.location.return_appearance(caller)
            #caller.msg(lookOutput)

            exitsToken = "|wExits:|n" # This needs to make the output of return_appearance implementation
            exitsIndex = lookOutput.find(exitsToken)
            
            if exitsIndex == -1:
                caller.msg("There are no exits.")
            else:
                # Remove everything before the 'Exits:' part
                lookOutput = lookOutput[exitsIndex:]

                # Find the next \n and remove everything after it
                newLineIndex = lookOutput.find("\n")

                if newLineIndex >= 0:
                    lookOutput = lookOutput[:newLineIndex]

                # Display the result
                caller.msg(lookOutput)


class CmdReadPass(Command):
    """
    Read your park pass.

    Usage:
      read pass

    Displays the details associated with your park pass.
    """    
    key = "read pass"
    help_category = GAME_HELP_CATEGORY
    locks = "cmd:all()"

    def func(self):
        caller = self.caller

        if not caller.db.has_season_pass:
            caller.msg("You don't have a park pass yet.\nTry asking the Clerk if you can |gbuy pass|n from them?")
            return

        maxNameLength = 40
        callerName = caller.name
        if len(callerName) > maxNameLength:
            callerName = callerName[:maxNameLength]

        nameRow = "Name: |c%s|n" % callerName
        townRow = "Town: |c%s|n" % caller.db.pass_town
        dateRow = "Create date: |c%s (UTC)|n" % caller.db.pass_create_date
        pointsRow = "Park Points: |c%s|n" % caller.db.pass_points

        maxRowSize = max(len(nameRow), len(townRow), len(dateRow), len(pointsRow))

        details = ""
        details += "|m" # Set a custom font color
        details += "==%s==\n" % ("=".ljust(maxRowSize - 4, '='))
        details += "| |w%s|m |\n" % ("|gPark Pass|n".ljust(maxRowSize))
        details += "| |w%s|m |\n" % (nameRow.ljust(maxRowSize))
        details += "| |w%s|m |\n" % (townRow.ljust(maxRowSize))
        details += "| |w%s|m |\n" % (dateRow.ljust(maxRowSize))
        details += "| |w%s|m |\n" % (pointsRow.ljust(maxRowSize))
        details += "==%s==" % ("=".ljust(maxRowSize - 4, '='))
        details += "|n" # Return to normal color

        caller.msg(details)


class CmdFeedback(Command):
    """
    Give feedback about the game.

    Usage:
      feedback <your feedback>

    Submit feedback to the game creators so they can make the game even better!
    """    
    key = "feedback"
    help_category = GAME_HELP_CATEGORY
    locks = "cmd:all()"

    def func(self):
        caller = self.caller

        if not self.args:
            caller.msg("feedback <your feedback>")
            return

        try:
            self.save_feedback(caller, self.args)
            caller.msg("Thank you %s for submitting your feedback!" % (caller.name))
        except Exception:
            caller.msg("Failed to submit feedback due to technical difficulties.")

    def save_feedback(self, caller, msg):

        if not msg:
            return # Nothing to log

        msg = msg.strip()
        if len(msg) == 0:
            return # Nothing to log

        time_str = datetime.datetime.utcnow().strftime("%B %d, %Y %I:%M %p (UTC)")

        location_name = 'None'
        if caller.location:
            location_name = caller.location.name

        log_msg = "%s\t%s\t%s\t%s\n" % (time_str, caller.name, location_name, msg)
        #caller.msg(log_msg)

        file = open(GAME_FEEDBACK_LOG_FILE_PATH, 'a')
        file.write(log_msg)
        file.close()

