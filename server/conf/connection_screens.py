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
 Welcome to |g{}|n!

 This game was created as a submission for the |gEnter the (Multi-User) Dungeon|n gamejam.

 If you have an existing account, connect to it by typing:
      |yconnect <username> <password>|n
 If you need to create an account, type (without the <>'s):
      |ycreate <username> <password>|n

 If you have spaces in your username, enclose it in quotes.
 Enter |ghelp|n for more info. |glook|n will re-show this screen.

 Enjoy!
|b==============================================================|n""" \
    .format(settings.SERVERNAME, utils.get_evennia_version())
