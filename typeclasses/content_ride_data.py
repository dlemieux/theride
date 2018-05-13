

from typeclasses.config_all import *
from typeclasses.content_art import *


# Thanks for joining us on the ride today. Now, according to my notes, you're a group of [roles]? Wow! Well remember to [special command] when the time is right.
# command_name: Be sure to ______ when the time is right!
# action_msg: '<person> <action_msg>!' Example: A player types 'listen' as a Concert Goer and we show 'Stacy listens!'
DATA_ROLES = [
    { "msg": "thieves",                 "command_name": "steal",          "action_msg": "steals", },
    { "msg": "pirates",                 "command_name": "loot",           "action_msg": "loots", },
    { "msg": "scientists",              "command_name": "research",       "action_msg": "researches", },
    { "msg": "tourists",                "command_name": "tour",           "action_msg": "tours", },
    { "msg": "space cadets",            "command_name": "trek",           "action_msg": "treks", },
    { "msg": "coal miners",             "command_name": "mine",           "action_msg": "mines", },
    { "msg": "rock band musicians",     "command_name": "rock",           "action_msg": "rocks out", },
    { "msg": "test subjects",           "command_name": "endure",         "action_msg": "endures", },
    { "msg": "animal trainers",         "command_name": "train",          "action_msg": "trains", },
    { "msg": "wizards",                 "command_name": "conjure",        "action_msg": "conjures", },
    { "msg": "athletes",                "command_name": "train",          "action_msg": "trains", },
    { "msg": "students",                "command_name": "study",          "action_msg": "studies", },
    { "msg": "concert goers",           "command_name": "listen",         "action_msg": "listens", },
    { "msg": "game developers",         "command_name": "debug",          "action_msg": "debugs", },
    { "msg": "writers",                 "command_name": "write",          "action_msg": "writes", },
    { "msg": "teachers",                "command_name": "teach",          "action_msg": "teaches", },
    { "msg": "car mechanics",           "command_name": "fix",            "action_msg": "fixes", },
    { "msg": "billionaires",            "command_name": "invest",         "action_msg": "invests", },
    { "msg": "actors",                  "command_name": "act",            "action_msg": "acts", },
    { "msg": "new hires",               "command_name": "work",           "action_msg": "works", },
    { "msg": "pilots",                  "command_name": "fly",            "action_msg": "flies", },
    { "msg": "settlers",                "command_name": "settle",         "action_msg": "settles", },
]

# You came to the park at a really special time. [main problem]. And hey, we could really use your help! But it seems like we're having some trouble for some reason.
DATA_MAIN_PROBLEMS = [
    {
        "msg": "The Chimera may be catching a cold!",
        "end_line": "A veternarian enters carrying a person-sized syringe labeled ANTIBIOTICS. The Chimera eyes it suspiciously, but allows itself to be injected.",
    },
    {
        "msg": "The Chimera needs exercise!",
        "end_line": "The Chimera lets out the most exaggerated yawn you've ever heard, completely wiped from your adventures.",
    },
    {
        "msg": "Our Chimera is hungry!",
        "end_line": "Suddenly, a giant piece of Chimera food dropped from the heavens! The now ravenous Chimera swiped it from the air and started chowing down on that sweet meat.\nThe slurping and tearing sounds clearly indicated the Chimera was pleased with this outcome.",
    },
    {
        "msg": "Our Chimera wants to take a nap but it has insomnia!",
        "end_line": "The Chimera seems to have become so tired from all the action that its actually starting to fall asleep. Normally this would be exactly what we want, but the passengers are still in a cart strapped to the Chimera|r's|n back.",
    },
    {
        "msg": "Our Chimera lost its memory!",
        "end_line": "The Chimera, still confused from having lost its memory, started heading into a secret cave nearby but forgot to duck its head and smashed it against the rocks!\nRocks and tiny debris were falling down, but the Chimera seemed relieved. That must have jolted back all of its memories! Huzzah!",
    },
    {
        "msg": "A new ride is malfunctioning!",
        "end_line": "The malfunctioning ride we've been trying to fix was now even more rickety! And as a cart ran along its tracks the final screws came loose and the cart went soaring into the air, untethered, full of screaming passengers!\nThe Chimera leaps up and wrapped the ride cart in its tail, landing softly and lowering the cart.",
    },
    {
        "msg": "Someone hacked the park security network!",
        "end_line": "The security network seemed completely lost. It was still hacked and no one could do anything about it! The Chimera suddenly had an idea, and ran over to pull out the mainframe cord. Holding the cord in its teeth for a few seconds, it then plugged it back in. The reboot worked! The hacker was kicked out! And never heard from again.",
    },
    {
        "msg": "There's a bad storm coming!",
        "end_line": "The Chimera ran all over the park and the riders warned everyone of the incoming storm, and they were all able to prepare adequately. The park was saved!",
    },
    {
        "msg": "The park is running out of money!",
        "end_line": "Luckily, this amazing journey was being documented the whole time, and a famous film company wants to buy the rights so they can make a movie! The park will earn all the money it needs to keep operating!",
    },
    {
        "msg": "Someone's been trying to kidnap the Chimera!",
        "end_line": "The Chimera Kidnapper suddenly appeared and lunged at the Chimera with a large brown sack to steal it away! Unfortunately, they grossly underestimated the size of a Chimera and the sack merely covered its front paw. The very paw that proceeded to smack the kidnapper up into the sky, soaring away. Looks like the Chimera Kidnapper is blasting off agaaaaiiiiin!",
    },
    {
        "msg": "Booby traps have been placed around the park!",
        "end_line": "As it turns out, the booby traps placed around the park were just trial versions, and disabled themselves after the 30-minute free period! The park was saved!",
    },
    {
        "msg": "An artifact has been stolen!",
        "end_line": "The stolen artifact was still on everyone's mind, and they did some research into where a thief may try to sell the rare artifact. The group put in a WANT ad in the park newsletter and immediately caught the thief.",
    },
    {
        "msg": "We've lost communication with a remote base!",
        "end_line": "The Chimera leapt high into the air and was knocked around by high winds! When it landed, it hit an antenna on the communications building, which amazingly fixed the signal coming from the remote base! Communications were restored!",
    },
    {
        "msg": "We have to rescue a cat up a tree!",
        "end_line": "Everyone remembers that the cat is still stuck in the tree and start calling out to the cat to reassure it that they'll rescue the cat soon. The cat yawns, and leaps down out of the tree and onto the ground unharmed, because obviously it was a cat and being in a tree isn't a problem.",
    },
    {
        "msg": "We're scouting out a new territory!",
        "end_line": "After all that adventuring, it looks like we've managed to map out the whole territory. Great work everyone!",
    },
    {
        "msg": "We found a treasure map, but don't know how to decipher it!",
        "end_line": "Suddenly, the meaning of the treasure map was all so obvious. All the clues, Xs, riddles, and compass marks became one, and then, became nothing. There was no treasure this group could not find. And with this knowledge, there was no need to dig up the treasure, because the real treasure, was friendship.",
    },
]

# And you'll never believe it, but our efforts keep being thwarted by [villain]!
DATA_VILLAIN = [
    {
        "msg": "a mad scientist",
        "picture": PICTURE_GENERIC,
        "defeat_events": [
            {
                "msg": "Something tells me that you won't have to worry about VILLAIN for a long time.",
                "delay": CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            }
        ],
    },
    {
        "msg": "a sentient robot",
        "picture": PICTURE_GENERIC,
        "defeat_events": [
            {
                "msg": "Something tells me that you won't have to worry about VILLAIN for a long time.",
                "delay": CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            }
        ],
    },
    {
        "msg": "an angry ancient god",
        "picture": PICTURE_GENERIC,
        "defeat_events": [
            {
                "msg": "Something tells me that you won't have to worry about VILLAIN for a long time.",
                "delay": CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            }
        ],
    },
    {
        "msg": "an alien",
        "picture": PICTURE_GENERIC,
        "defeat_events": [
            {
                "msg": "Something tells me that you won't have to worry about VILLAIN for a long time.",
                "delay": CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            }
        ],
    },
    {
        "msg": "a vampire king",
        "picture": PICTURE_GENERIC,
        "defeat_events": [
            {
                "msg": "Something tells me that you won't have to worry about VILLAIN for a long time.",
                "delay": CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            }
        ],
    },
    {
        "msg": "a mummy",
        "picture": PICTURE_GENERIC,
        "defeat_events": [
            {
                "msg": "Something tells me that you won't have to worry about VILLAIN for a long time.",
                "delay": CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            }
        ],
    },
    {
        "msg": "a ghost",
        "picture": PICTURE_GENERIC,
        "defeat_events": [
            {
                "msg": "Something tells me that you won't have to worry about VILLAIN for a long time.",
                "delay": CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            }
        ],
    },
    {
        "msg": "a company executive",
        "picture": PICTURE_GENERIC,
        "defeat_events": [
            {
                "msg": "Something tells me that you won't have to worry about VILLAIN for a long time.",
                "delay": CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            }
        ],
    },
    {
        "msg": "a psychic child",
        "picture": PICTURE_GENERIC,
        "defeat_events": [
            {
                "msg": "Something tells me that you won't have to worry about VILLAIN for a long time.",
                "delay": CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            }
        ],
    },
    {
        "msg": "a time traveler",
        "picture": PICTURE_GENERIC,
        "defeat_events": [
            {
                "msg": "Something tells me that you won't have to worry about VILLAIN for a long time.",
                "delay": CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            }
        ],
    },
    {
        # I've gotta maintain my magna cum laude status. I'll definitely get into grad school with this thesis
        "msg": "an overachieving college student",
        "picture": PICTURE_GENERIC,
        "defeat_events": [
            {
                "msg": "Something tells me that you won't have to worry about VILLAIN for a long time.",
                "delay": CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            }
        ],
    }, 
    {
        "msg": "a knockoff brand 'Kaimera'",
        "picture": PICTURE_GENERIC,
        "defeat_events": [
            {
                "msg": "Something tells me that you won't have to worry about VILLAIN for a long time.",
                "delay": CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            }
        ],
    },
    {
        "msg": "a pirate captain",
        "picture": PICTURE_GENERIC,
        "defeat_events": [
            {
                "msg": "Something tells me that you won't have to worry about VILLAIN for a long time.",
                "delay": CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            }
        ],
    },
    {
        "msg": "a cursed object",
        "picture": PICTURE_GENERIC,
        "defeat_events": [
            {
                "msg": "Something tells me that you won't have to worry about VILLAIN for a long time.",
                "delay": CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            }
        ],
    },
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
                        'msg': "Suddenly, a massive jail cube builds itself around the group and you become trapped! It must have been one of those easy setup jails!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "And not only are you trapped, but the bars seems to be getting smaller and smaller over time. You'll be crushed for sure!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The ride attendant acts quickly, and pulls out a laser which burns holes through the pipes.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The laser does just enough damage that the Chimera is able to leap up and push through the remaining jail pieces!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'inside a giant animal',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Suddenly, the ground rumbles, and you realize that the Chimera is actually standing on the tongue of a giant monster! And the mouth of this monster is closing fast!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The ride attendant acts quickly, and pours lemon juice on the tongue of the monster! The group is spit out of its mouth with blazing speed!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The Chimera is finally able to get its bearings and does a controlled landing.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'spider web',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "The Chimera was sauntering along at a quick pace, and then stopped suddenly! Its paws were stuck in some kind of webbing substance. Surely there couldn't be a spider large enough to trap a Chimera!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The ride attendant acts quickly, pulling out a giant pair of scissors. Like the ones you'd find at a ribbon cutting ceremony! These giant scissors are cutting away all the webs, but the giant spider is rushing towards the group fast!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "At the last minute the line attendant cuts the final thread, and the Chimera breaks free. The scissors were left behind, but at least the group is out of there!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'deep pit',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Suddenly, the Chimera falls through the fake carpet it was walking on and falls into a deep pit! How could this happen, you think. It's the oldest trick in the book!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The ride attendant acts quickly, and throws down a large spring. *BOOOOIIINNGGG* The Chimera pops right out of the trap!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "On the way out, however, the spring got entangled in its tail. You continue onward with an extra bounce to each step.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'quicksand',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Suddenly, you realize the Chimera has been standing in quicksand! And it's already up to your waist!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Ever since you were a kid, you just KNEW quicksand would be the end of you! And you've been so diligent about avoiding quicksand your whole life!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The ride attendant acts quickly, and screams for help at the top of their lungs!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A group of construction workers show up and quickly excavate all the sand around you. Apparently, they were planning to make a sand pit in the children's section anyways.\nFinally, you are free!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            #{
            #    'option_name': 'a puzzle room',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Suddenly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "The line attendant acts quickly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'underwater cavern',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Suddenly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "The line attendant acts quickly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'dragon\'s treasure chamber',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Suddenly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "The line attendant acts quickly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'shrunk tiny',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Suddenly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "The line attendant acts quickly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'shuttle to space',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Suddenly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "The line attendant acts quickly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'inside of a computer',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Suddenly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "The line attendant acts quickly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'in mud',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Suddenly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "The line attendant acts quickly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "\"Save us!\"' the line attendant yells ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'a cave-in',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Suddenly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "The line attendant acts quickly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "\"Save us!\"' the line attendant yells ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'time loop',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Suddenly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "The line attendant acts quickly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "\"Save us!\"' the line attendant yells ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'haunted house',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Suddenly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "The line attendant acts quickly, ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "\"Save us!\"' the line attendant yells ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            {
                'option_name': 'in a cage',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Suddenly, the bars of a cage wrap around you and the Chimera. A chain lifts your new cell high above the ground!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The ride attendant acts quickly, pulling on the bottom of the chain until you swing like a pendulum, right through the roof!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "\"Save us!\"' the line attendant yells as you land, shattering the cage and earning your freedom!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
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
                        'msg': "The Chimera tries to show off by running even faster.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "With its magical powers, it summons a bright and shiny rainbow!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "With a single leap, the Chimera leaps onto the rainbow and gallops towards the heavens!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            #{
            #    'option_name': 'follow a white rabbit',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "The Chimera has anticipated this type of danger!",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "With its magical powers, it summons ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'wolves scent their way out',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "The Chimera has anticipated this type of danger!",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "With its magical powers, it summons ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'red string of fate',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "The Chimera has anticipated this type of danger!",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "With its magical powers, it summons ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'circus',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "The Chimera has anticipated this type of danger!",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "With its magical powers, it summons ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'head towards a bright light',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "The Chimera has anticipated this type of danger!",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "With its magical powers, it summons ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'sledding',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "The Chimera has anticipated this type of danger!",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "With its magical powers, it summons ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'taken out with a trash heap',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "The Chimera has anticipated this type of danger!",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "With its magical powers, it summons ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a pistol duel!\"",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You fire at each other and the bullets keep colliding in the air! You gain the upper hand and fire 3 shots directly at your target!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "\"Wow!\" you think, \"I've never seen VILLAIN do a Matrix dodge before!\" You agree to a truce for now and are allowed to leave.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            #{
            #    'option_name': 'triathlon',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a triathlon!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'game of poker',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a game of poker!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'race',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a foot race!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'battle of wits',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a battle of wits!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'dance battle',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a dance battle!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'lip sync contest',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a lip sync contest!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'paintball',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a paintball contest!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'arm wrestling',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at an arm wrestling contest!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'staring contest',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a staring contest!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'riddle',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a contest of riddles!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'strength contest',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a strength contest!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'first to laugh contest',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a first to laugh contest!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'archery',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at an archery contest!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'writing contest',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a writing contest!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'ugly sweater contest',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A challenge rings out in the air: \"Let's see if you can best me... at an ugly sweater contest!\"",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
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
                        'msg': "The challenge is finally over. An adoring crowd rushes over, impressed with your magnificent skills!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You sign autographs until your hands grow sore!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The Chimera finally makes its way through to the other side. Although, it is missing a few tufts of hair thanks to the some especially passionate fans.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            #{
            #    'option_name': 'press conference',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "The challenge is finally over. ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'tropical vacation',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "The challenge is finally over. ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'stunt show',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "The challenge is finally over. ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'parade',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "The challenge is finally over. The Chimera slows down to a trot and walks down the park's Main Street.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': 'A parade spontaneously erupts around you, complete with musicians, ',
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            {
                'option_name': 'park entrance',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "The challenge is finally over. Suddenly, you're in the park entrance! How did you get out here?",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': 'The park security guard shakes their head disapprovingly, and starts writing you up a ticket for theft of park property.\n"No park equipment, or Chimera|rs|n, are permitted to leave the park without permission!" the guard says. "I\'m putting you away for a loooong time."',
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "This can\'t be happening! No, really, it\'s just an illusion! You focus your thoughts, and the world around you starts to dissolve.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The Chimera snorts with disdain and saunters through the evaporating mist.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'flash mob',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "The challenge is finally over. The Chimera slows down to a trot and weaves through a group of mild-mannered adults gathered in the courtyard.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': 'Suddenly, the Chimera stops moving, and everything around you freezes still! All time appears to has stopped as people are frozen mid-stride, and the murmuring of voices has completely disappeared.',
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You hear a song faintly being played over speakers, and then it fades in louder and louder as the group around you begins doing choreographed dancing and singing. You've been caught in the middle of a flash mob! And the Chimera knows the moves too!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "After the song finishes the dancers return to their normal activities as if nothing happened, and the Chimera saunters on.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            #{
            #    'option_name': 'party',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "The challenge is finally over. ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'desert',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "The challenge is finally over. ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'top of a mountain',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "The challenge is finally over. The mist clears... you find yourself at the pinnacle of a mountain!",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            {
                'option_name': 'dungeons and dragons night',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "The challenge is finally over. The Chimera lumbers away and crashes into the side of a suburban home. ",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Within, the startled inhabitants leap to their feet, knocking over a board covered in dice and miniatures. You've interrupted a night of Caverns and Chimera|rs|n!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The owner of the house puts on his robe and wizard hat. He attempts to make you pay for the damages. Alas, he rolls a one.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Bored, the Chimera breaks a few more pieces of furniture as it ventures back out to the street.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'inside a pixelated video game',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "The challenge is finally over. You suddenly realize the sky is curved...",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "It's the inside of a giant monitor! Wait, why is everything blocky? You're in a video game!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The only way out is to lose your virtual lives! Spotting a tall cliff, the Chimera launches itself off into a free fall!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You feel the cells of your body de-pixelating as you return to the physical plane.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
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
                        'msg': "But the worst is yet to come. At the horizon, you spot the silhouette of a tornado coming straight at you!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': 'The Chimera dives to the left. Dives to the right. Pulls a rope-a-dope against the side of a barn and jukes around the tornado unscathed!',
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Now that you are thoroughly nauseated, the Chimera saunters away proudly.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            #{
            #    'option_name': 'typhoon',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "But the worst is yet to come. ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'earthquake',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "But the worst is yet to come. ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            {
                'option_name': 'volcanic eruption',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "But the worst is yet to come. The volcano on the park grounds is erupting boiling hot lava!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The Chimera thinks quickly, and diverts all the faucets in the bathrooms towards the mouth of the volcano. All you can hear is the sizzling of steam as water meets lava!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "With the volcano thoroughly doused, you are able to continue on.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'stock market crash',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "But the worst is yet to come. For at this very moment, the stock market is crashing to its lowest point in 30 years!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "None of you were prepared for this! Adults around the park begin sobbing at the news. The Chimera urges everyone not to sell, as it will only make things worse!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A voice over the park's loudspeaker clarifies that this was only a disaster preparedness test and people may resume what they were doing. Whew! Disaster averted for another day!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            #{
            #    'option_name': 'dust storm',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "But the worst is yet to come. ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'asteroid shower',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "But the worst is yet to come. ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'stampede of wild animals',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "But the worst is yet to come. ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'runaway train',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "But the worst is yet to come. ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'flash flood',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "But the worst is yet to come. ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'power outage',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "But the worst is yet to come. ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'blizzard/avalanche',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "But the worst is yet to come. ",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            {
                'option_name': 'tidal wave',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "But the worst is yet to come. A meteorite has crashed into the wave pool in the park, and caused a massive tidal wave to thrash over the park!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Everyone held on tight to the Chimera so they wouldn't be tossed around, and the Chimera held on to the stone Chimera statue in front of the ride entrance.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The tidal wave passed, and was actually a lot more fun than anticipated. With smiles on your faces, the Chimera leaps on!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'fire',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "But the worst is yet to come. The temperature around you feels to be rising fast, and you realize that several fires have surrounded you and the Chimera!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You and the Chimera take a deep breath....and blow your air at the fires straight ahead of you! Your breath has no effect, but the Chimera is able to squelch the fire!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You escape before the fire has a chance to return to its former size and strength.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'killer bees',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "But the worst is yet to come. An ominous hum overwhelms your ears as the air fills with thousands upon thousands of bees!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The Chimera hisses as the bees attack, but their stingers are no match for its legendary scales!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "After several minutes, the vicious swarm recedes, allowing you to escape!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
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
                        'msg': "You can never trust VILLAIN! There's one more obstacle between you and them!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': 'And this time, it\'s aliens! The sky darkens as hundreds of UFOs descend, bent on wiping out all life on Earth!',
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The Chimera clears its throat loudly and gestures towards a nearby wall. A notice posted there states that intergalactic highways, restaurants, and wars are forbidden without the proper permits.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "With the type of unison only a collective hive mind can muster, the aliens bow their spaceships in disappointment and warp away.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            #{
            #    'option_name': 'black hole',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "You can never trust VILLAIN! There's one more obstacle between you and them!",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            {
                'option_name': 'time rift',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "You can never trust VILLAIN! There's one more obstacle between you and them!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': 'The sky rips open as a rift in time appears. Objects from past and future centuries begin to spew out, turning the landscape into the world\'s biggest yard sale.',
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Just when all hope appears lost, the Chimera dashes forward and picks up a glittering piece of metal in its mouth. a long thread dangles from one end, but it looks like it\'s made out of light!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You bounce back and forth violently as the Chimera expertly sews the fabric of time back together.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'plague',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "You can never trust VILLAIN! There's one more obstacle between you and them!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': 'A horde of the undead emerges from all directions. A plague must have infected the entire human population!',
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "As they come within biting distance, you recoil in horror. But you notice something odd. Up close, their green skin looks a bit splotchy?",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "What you feared was the end of humanity was simply a local zombie run for charity! Relieved, you wave to them as the Chimera continues its journey.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            #{
            #    'option_name': 'solar eclipse',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "You can never trust VILLAIN! There's one more obstacle between you and them!",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            #{
            #    'option_name': 'drought',
            #    'events': [
            #        # The events list is all the events that will be shown in order.
            #        # Typically 4 messages long.
            #        {
            #            'msg': "You can never trust VILLAIN! There's one more obstacle between you and them!",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "An ending.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #        {
            #            'msg': "A transition out.",
            #            'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
            #        },
            #    ],
            #},
            {
                'option_name': 'plants die from locusts',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "You can never trust VILLAIN! There's one more obstacle between you and them!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': 'The nearby trees begin to shake, then collapse as millions of locusts eat them alive in seconds!',
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You aren\'t exactly relieved when the Chimera licks its fangs and plunges you all into the thick of the locust swarm.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "It turns out locusts are a delicious Chimera snack. A fact you wish you didn't know, as you brush insect legs from your clothes...",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
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
                        'msg': "Delighted that the danger is over, a pack of paparazzi approaches!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "It seems that your adventure is coming to an end.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'old time photographer',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Delighted that the danger is over, an old-time photographer hobbles over and sets up an antique camera.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "It seems that your adventure is coming to an end.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'red carpet',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Delighted that the danger is over, the Chimera runs toward the station, but ends up caught in the middle of a red carpet event!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "It seems that your adventure is coming to an end.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'documentary film crew',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Delighted that the danger is over, a documentary film crew rushes out to interview everyone involved.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "It seems that your adventure is coming to an end.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'motion capture studio',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Delighted that the danger is over, a swarm of special effects artists approaches, setting up equipment and green screens on all sides of you.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "It seems that your adventure is coming to an end.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'artist speed painting',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Delighted that the danger is over, a troupe of artists arrive and begin furiously mixing watercolor paints together.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of...paint!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "It seems that your adventure is coming to an end.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'selfie stick',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Delighted that the danger is over, the Chimera pulls out a selfie stick and poses with you.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "It seems that your adventure is coming to an end.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'investigative reporter',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Delighted that the danger is over, an investigative reporter leans out from behind a bush and presses a hidden button on their eyeglasses.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "It seems that your adventure is coming to an end.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                ],
            },
            {
                'option_name': 'security camera',
                'events': [
                    # The events list is all the events that will be shown in order.
                    # Typically 4 messages long.
                    {
                        'msg': "Delighted that the danger is over, all the security cameras in the park rotate to face you and the Chimera.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "It seems that your adventure is coming to an end.",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
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
                        'msg': "Or is it? A puff of smoke appears in front of you, and as it dissipates you see VILLAIN!",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "VILLAIN_PICTURE",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "\"You fools! You're just a bunch of ROLE. What are you going to do, ACTION me to death?\"",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "\"MWA HA HA HA HA!\"",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Hmmm...that's not a bad idea...",
                        'delay': CHIMERA_RIDE_DEFAULT_EVENT_DELAY,
                        'type': 'start_villain_battle',
                    },
                ],
            },
        ],
    }, # Villain battle
]
