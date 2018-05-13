# -*- coding: utf-8 -*-
"""
Connection screen

Texts in this module will be shown to the user at login-time.

Evennia will look at global string variables (variables defined
at the "outermost" scope of this module and use it as the
connection screen. If there are more than one, Evennia will
randomize which one it displays.

The commands available to the user when the connection screen is shown
are defined in commands.default_cmdsets. UnloggedinCmdSet and the
screen is read and displayed by the unlogged-in "look" command.

"""

from django.conf import settings
from evennia import utils

CONNECTION_SCREEN = """
|b==============================================================|n
                          _   _                _ 
              /\/\  _   _|| ||_|| ||__   __ _ _ __(_)
             /    \|| || || || __|| '_ \ / _` || '__|| ||
            / /\/\ \ ||_|| || ||_|| || || || (_|| || ||  || ||
            \/    \/\__, ||\__||_|| ||_||\__,_||_||  ||_||
                    ||___/                        
                      ___           _    
                     / _ \__ _ _ __|| || __
                    / /_)/ _` || '__|| ||/ /
                   / ___/ (_|| || ||  ||   < 
                   \/    \__,_||_||  ||_||\_\\

 Welcome to |g{}|n!

 This game was created as a submission for the |gEnter the (Multi-User) Dungeon|n game jam.
 To play, you will need to type commands in the prompt area at the bottom of the screen.

 If you haven't visited the park before, you need to create an account.
 Type the following (without the <>'s):
       |ycreate <username> <password>|n

If you have visited before, welcome back! You can join again by typing (again without the <>'s):
       |yconnect <username> <password>|n

If you have spaces in your username, you can enclose it in quotes.

For further information about us, visit |chttps://www.prettysmartgames.com/|n
You can also follow us at twitter |c@PrettySmartNews|n
Or check out the code at |chttps://github.com/dlemieux/theride|n

Type |yhelp|n for more info. Or |ylook|n to read this info once more.
|b==============================================================|n""" \
    .format(settings.SERVERNAME, utils.get_evennia_version())
