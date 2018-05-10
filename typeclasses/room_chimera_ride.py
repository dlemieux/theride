import random
import datetime

from evennia import CmdSet, Command
from evennia import create_object
from evennia import DefaultRoom
from evennia import DefaultExit
from evennia import TICKER_HANDLER

from typeclasses.room_chimera_exit import ChimeraExitRoom


DEFAULT_EVENT_DELAY = 1
ADD_EVENT_NAME_PREFIX = True

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
    { "msg": "Animal Trainers",     "command_name": "train", },
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

# And you'll never believe it, but our efforts keep being thwarted by [villain]!
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

DATA_RIDE_EVENT_SECTIONS = [
    # This list will be all the sections that must to occur in the ride.
    {
        'section_name': 'trapped somewhere',
        'options': [
            # The options list will have 1 item selected in it to represent the section.
            {
                'option_name': 'jail',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'inside a giant animal',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'spider web',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'deep pit',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'quicksand',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'a puzzle room',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'underwater cavern',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'dragon\'s treasure chamber',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'shrunk tiny',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'shuttle to space',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'inside of a computer',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'in mud',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'a cave-in',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'time loop',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'haunted house',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'in a cage',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
        ],
    }, # Trapped somewhere
    {
        'section_name': 'escape from trap',
        'options': [
            # The options list will have 1 item selected in it to represent the section.
            {
                'option_name': 'ride a rainbow to safety',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'follow a white rabbit',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'wolves scent their way out',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'red string of fate',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'circus',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'head towards a bright light',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'sledding',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'taken out with a trash heap',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
        ],
    }, # Escape from trap
    {
        'section_name': 'villain challenge',
        'options': [
            # The options list will have 1 item selected in it to represent the section.
            {
                'option_name': 'colosseum',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'triathlon',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'game of poker',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'race',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'battle of wits',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'dance battle',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'lip sync contest',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'paintball',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'arm wrestling',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'staring contest',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'riddle',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'strength contest',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'first to laugh contest',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'archery',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'writing contest',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'ugly sweater contest',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
        ],
    }, # Villain challenge
    {
        'section_name': 'after challenge',
        'options': [
            # The options list will have 1 item selected in it to represent the section.
            {
                'option_name': 'adoring crowd',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'press conference',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'tropical vacation',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'stunt show',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'parade',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'park entrance',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'party',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'desert',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'top of a mountain',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'dungeons and dragons night',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'inside a pixellated video game',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
        ],
    }, # After challenge
    {
        'section_name': 'disaster',
        'options': [
            # The options list will have 1 item selected in it to represent the section.
            {
                'option_name': 'tornado',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'typhoon',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'earthquake',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'volcanic eruption',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'stock market crash',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'dust storm',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'asteroid shower',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'stampede of wild animals',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'runaway train',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'flash flood',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'power outage',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'blizzard/avalanche',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'tidal wave',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'fire',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'killer bees',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
        ],
    }, # Disaster
    {
        'section_name': 'crisis',
        'options': [
            # The options list will have 1 item selected in it to represent the section.
            {
                'option_name': 'invasion from space',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'black hole',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'time rift',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'plague',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'solar eclipse',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'drought',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'plants die from locusts',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
        ],
    }, # Crisis
    {
        'section_name': 'photo opportunity',
        'options': [
            # The options list will have 1 item selected in it to represent the section.
            {
                'option_name': 'paparazzi',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'old time photographer',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'red carpet',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'documentary film crew',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'motion capture studio',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'artist speed painting',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'selfie stick',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'investigative reporter',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'security camera',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
        ],
    }, # Photo opportunity
    {
        'section_name': 'villain battle',
        'options': [
            # The options list will have 1 item selected in it to represent the section.
            {
                'option_name': 'sheer strength',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'ingenuity',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'archery',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Explain the setup.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "An ending.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A transition out.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                ],
            },
        ],
    }, # Villain battle
]

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
            return DEFAULT_EVENT_DELAY # Slight delay with no text for people to enter
        elif index == 1: # Plot setup

            # Determine the initial plot
            self.ride_role = random.choice(DATA_ROLES)
            self.ride_problem = random.choice(DATA_MAIN_PROBLEMS)
            self.ride_villain = random.choice(DATA_VILLAIN)

            # Determine all the other events that will happen
            self.ride_events = []

            # Set up all the sections
            for section_info in DATA_RIDE_EVENT_SECTIONS:
                # Choose the random scenario within the section options
                section_option = random.choice(section_info['options'])

                # All events in this section need to be added
                for single_event in section_option['events']:
                    
                    if ADD_EVENT_NAME_PREFIX:
                        single_event['msg'] = "(%s->%s) %s" % (section_info['section_name'], section_option['option_name'], single_event['msg'])

                    self.ride_events.append(single_event)

            # Display the premise
            msg = ""
            msg += "|y> auto-advance|n" + "\n"

            msg += "Thanks for joining us on the ride today. Now, according to my notes, you're a group of %s? Wow!\n" % (self.ride_role['msg'])
            msg += "Well remember to %s when the time is right.\n" % (self.ride_role['command_name'])

            msg += "You came to the park at a really special time. %s And hey, we could really use your help! But it seems like we're having some trouble for some reason.\n" % (self.ride_problem['msg'])

            msg += "And you'll never believe it, but our efforts keep being thwarted by %s!\n" % (self.ride_villain['msg'])

            self.msg_contents(msg)

            return DEFAULT_EVENT_DELAY
        else: # Running the events

            # See if we are out of events
            if len(self.ride_events) == 0:
                return -1

            # We have more events
            cur_event = self.ride_events[0]
            self.ride_events = self.ride_events[1:] # Remove the front element

            msg = ""
            msg += "|y> auto-advance|n" + "\n"
            
            msg += "%s" % (cur_event['msg'])

            self.msg_contents(msg)

            return cur_event['delay']

