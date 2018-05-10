
# Config
DEFAULT_EVENT_DELAY = 1

# Thanks for joining us on the ride today. Now, according to my notes, you're a group of [roles]? Wow! Well remember to [special command] when the time is right.
# command_name: Be sure to ______ when the time is right!
# action_msg: '<person> <action_msg>!' Example: A player types 'listen' as a Concert Goer and we show 'Stacy listens!'
DATA_ROLES = [
    { "msg": "thieves",                 "command_name": "steal",          "action_msg": "steals", },
    { "msg": "pirates",                 "command_name": "loot",           "action_msg": "loots", },
    { "msg": "scientists",              "command_name": "research",       "action_msg": "researched", },
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
        "msg": "Our Chimera is sick!",
        "end_line": "The Chimera coughed up a hairball and turned around to look at the group. Turns out there was nothing wrong with it the whole time!",
    },
    {
        "msg": "Our Chimera needs exercise!",
        "end_line": "The Chimera was finally tuckered out and had been sufficiently exercised.",
    },
    {
        "msg": "Our Chimera is hungry!",
        "end_line": "Suddenly, a giant piece of Chimera food dropped from the heavens! The now ravenous Chimera swiped it from the air and started chowing down on that sweet meat.\nThe slurping and tearing sounds clearly indicated the Chimera was pleased with this outcome.",
    },
    {
        "msg": "Our Chimera wants to take a nap but it has insomnia!",
        "end_line": "The Chimera seems to have become so tired from all the action that its actually starting to fall asleep. Normally this would be exactly what we want, but the passangers are still in a cart strapped to the Chimera's back.",
    },
    {
        "msg": "Our Chimera lost its memory!",
        "end_line": "The Chimera, still confused from having lost its memory, started heading into a secret cave nearby but forgot to duck its head and smashed it against the rocks!\nRocks and tiny debris were falling down, but the Chimera seemed relieved. That must have jolted back all of its memories! Huzzah!",
    },
    {
        "msg": "A new ride is malfunctioning!",
        "end_line": "The malfunctiong ride we've been trying to fix was now even more rickety! And as a cart ran along its tracks the final screws came loose and the cart went soaring into the air, untethered, full of screaming passengers!\nThe Chimera leaps up and wrapped the ride cart in its tail, landing softing and lowering the cart.",
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
        "end_line": "Luckily, this amazing journey was being documented the whole time, and a famour film company wants to buy the rights so they can make a movie! The park will earn all the money it needs to keep operating!",
    },
    {
        "msg": "Someone's been trying to kidnap the Chimera!",
        "end_line": "The Chimera Kidnapper suddenly appeared and lunged at the Chimera with a large brown sack to steal it away! Unfortunately, they grossly underestimated the size of a Chimera and the sack merely covered its front paw. The very paw that proceeded to smack the kidnapper up into the sky, soaring away. Looks like the Chimera Kidnapper is blasting off agaaaaiiiiin!",
    },
    {
        "msg": "Booby traps have been placed around the park!",
        "end_line": "As it turns out, the booby traps placed around the park were just trial versions, and disabled themselves after the 30 minute free period! The park was saved!",
    },
    {
        "msg": "An artifact has been stolen!",
        "end_line": "The stolen artifact was still on everyone's mind, and they did some research into where a theif may try to sell the rare artifact. The group put in a WANT ad in the park newsletter and immediately caught the thief.",
    },
    {
        "msg": "We've lost communication with a far off base!",
        "end_line": "The Chimera leapt high into the air and was knocked around by high winds! When it landed, it hit an antenna on the communications building, which amazingly fixed the signal coming from the far off base! Communications were restored!",
    },
    {
        "msg": "We have to rescue a cat up a tree!",
        "end_line": "Everyone remembers that the cat is still stuck in the tree and start calling out to the cat to reassure it that they'll resuce the cat soon. The cat yawns, and leaps down out of the tree and onto the ground unharmed, because obviously it was a cat and being in a tree isn't a problem.",
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
    { "msg": "a mad scientist", },
    { "msg": "a sentient robot", },
    { "msg": "an angry ancient god", },
    { "msg": "an alien", },
    { "msg": "a vampire king", },
    { "msg": "a mummy", },
    { "msg": "a ghost", },
    { "msg": "a company executive", },
    { "msg": "a psychic child", },
    { "msg": "a time traveler", },
    { "msg": "an overachieving college student", }, # I've gotta maintain my magna cum laude status. I'll definitely get into grad school with this thesis
    { "msg": "a knockoff brand 'Kaimera'", },
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
                        'msg': "Suddenly, a massive cage builds itself around the group and you become trapped! It must have been one of those easy setup cages!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "And not only are you trapped, but the cage seems to be getting smaller and smaller over time. You'll be crushed for sure!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, and pulls out a laser which burns holes through the pipes.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The laser does just enough damage that the Chimera is able to leap up and push through the remaining cage pieces!",
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
                        'msg': "Suddenly, the ground rumbles, and you realize that the Chimera is actually standing on the tongue of a giant monster! And the mouth of this monster is closing fast!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, and pours lemon juice on the tongue of the monster! The group is spit out of its mouth with blazing speed!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The Chimera is finally able to get its barings and does a controlled landing.",
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
                        'msg': "The Chimera was sauntering along at a quick pace, and then stopped suddenly! Its paws were stuck in some kind of webbing substance. Surely there couldn't be a spider large enough to trap a Chimera!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, and pulled out a giant pair of scissors, like you'd find at a giant ribbon cutting ceremony. These giant scissors are cutting away all the webs, but the giant spider is rushing towards the group fast!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "At the last minute the line attendant cuts the final thread, and the Chimera breaks free. The scissors were left behind, but at least the group is out of there!",
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
                        'msg': "Suddenly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, ",
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
                        'msg': "Suddenly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, ",
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
                        'msg': "Suddenly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, ",
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
                        'msg': "Suddenly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, ",
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
                        'msg': "Suddenly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, ",
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
                        'msg': "Suddenly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, ",
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
                        'msg': "Suddenly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, ",
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
                        'msg': "Suddenly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, ",
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
                        'msg': "Suddenly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "\"Save us!\"' the line attendant yells ",
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
                        'msg': "Suddenly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "\"Save us!\"' the line attendant yells ",
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
                        'msg': "Suddenly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "\"Save us!\"' the line attendant yells ",
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
                        'msg': "Suddenly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "\"Save us!\"' the line attendant yells ",
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
                        'msg': "Suddenly, the bars of a cage wrap around you and the Chimera. A chain lifts your new cell high above the ground!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The line attendant acts quickly, pulling on the bottom of the chain until you swing like a pendulum, right through the roof!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "\"Save us!\"' the line attendant yells as you land, shattering the cage and earning your freedom!",
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
                        'msg': "The Chimera has anticipated this type of danger!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "With its magical powers, it summons a bright and shiny rainbow!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "With a single leap, the Chimera leaps onto the rainbow and gallops towards the heavens!",
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
                        'msg': "The Chimera has anticipated this type of danger!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "With its magical powers, it summons ",
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
                        'msg': "The Chimera has anticipated this type of danger!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "With its magical powers, it summons ",
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
                        'msg': "The Chimera has anticipated this type of danger!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "With its magical powers, it summons ",
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
                        'msg': "The Chimera has anticipated this type of danger!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "With its magical powers, it summons ",
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
                        'msg': "The Chimera has anticipated this type of danger!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "With its magical powers, it summons ",
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
                        'msg': "The Chimera has anticipated this type of danger!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "With its magical powers, it summons ",
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
                        'msg': "The Chimera has anticipated this type of danger!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "With its magical powers, it summons ",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a pistol duel!\"",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a triathlon!\"",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a game of poker!\"",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': " ",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a foot race!\"",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': " ",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a battle of wits!\"",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a dance battle!\"",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a lip sync contest!\"",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a paintball contest!\"",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at an arm wrestling contest!\"",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a staring contest!\"",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a contest of riddles!\"",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a strength contest!\"",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a first to laugh contest!\"",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at an archery contest!\"",
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
                        'msg': "EManiacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at a writing contest!\"",
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
                        'msg': "Maniacal laughter fills the air as VILLAIN appears before you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "A challenge rings out in the air: \"Let's see if you can best me... at an ugly sweater contest!\"",
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
                        'msg': "The challenge is finally over. An adoring crowd rushes over, impressed with your magnificent skills!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You sign autographs until your hands grow sore!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The Chimera finally makes its way through to the other side.",
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
                        'msg': "The challenge is finally over. ",
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
                        'msg': "The challenge is finally over. ",
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
                        'msg': "The challenge is finally over. ",
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
                        'msg': "The challenge is finally over. ",
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
                        'msg': "The challenge is finally over. Suddenly, you're in the park entrance! How did you get out here?",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "No, it's just an illusion! You focus your thoughts, and the world around you starts to dissolve.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The Chimera snorts with disdain and saunters through the evaporating mist.",
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
                        'msg': "The challenge is finally over. ",
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
                        'msg': "The challenge is finally over. ",
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
                        'msg': "The challenge is finally over. The mist clears... you find yourself at the pinnacle of a mountain!",
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
                        'msg': "The challenge is finally over. The Chimera lumbers away and crashes into the side of a surburban home. ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Within, the startled inhabitants leap to their feet, knocking over a board covered in dice and miniatures. You've interrupted a night of Caverns and Chimeras!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The owner of the house puts on his robe and wizard hat. He attempts to make you pay for the damages. Alas, he rolls a one.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Bored, the Chimera breaks a few more pieces of furniture as it ventures back out to the street.",
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
                        'msg': "The challenge is finally over. You suddently realize the sky is curved...",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "It's the inside of a giant monitor! Wait, why is everything blocky? You're in a video game!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The only way out is to die on purpose. Spotting a tall cliff, the Chimera launches itself off into a free fall!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You feel the cells of your body de-pixellating as you return to the physical plane.",
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
                        'msg': "But the worst is yet to come. At the horizon, you spot the silhouette of a tornado coming straight at you!",
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
                        'msg': "But the worst is yet to come. ",
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
                        'msg': "But the worst is yet to come. ",
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
                        'msg': "But the worst is yet to come. ",
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
                        'msg': "But the worst is yet to come. ",
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
                        'msg': "But the worst is yet to come. ",
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
                        'msg': "But the worst is yet to come. ",
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
                        'msg': "But the worst is yet to come. ",
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
                        'msg': "But the worst is yet to come. ",
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
                        'msg': "But the worst is yet to come. ",
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
                        'msg': "But the worst is yet to come. ",
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
                        'msg': "But the worst is yet to come. ",
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
                        'msg': "But the worst is yet to come. ",
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
                        'msg': "But the worst is yet to come. ",
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
                        'msg': "But the worst is yet to come. An ominous hum overwhelms your ears as the air fills with thousands upon thousands of bees!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "The Chimera hisses as the bees attack, but their stingers are no match for its legendary scales!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "After several minutes, the vicious swarm recedes, allowing you to escape!",
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
                        'msg': "You can never trust VILLAIN! There's one more obstacle between you and them!",
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
                        'msg': "You can never trust VILLAIN! There's one more obstacle between you and them!",
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
                        'msg': "You can never trust VILLAIN! There's one more obstacle between you and them!",
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
                        'msg': "You can never trust VILLAIN! There's one more obstacle between you and them!",
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
                        'msg': "You can never trust VILLAIN! There's one more obstacle between you and them!",
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
                        'msg': "You can never trust VILLAIN! There's one more obstacle between you and them!",
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
                        'msg': "You can never trust VILLAIN! There's one more obstacle between you and them!",
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
                        'msg': "Delighted that the danger is over, a pack of paparazzi approaches!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Now it's surely time for a happy ending.",
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
                        'msg': "Delighted that the danger is over, a ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Now it's surely time for a happy ending.",
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
                        'msg': "Delighted that the danger is over, a ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Now it's surely time for a happy ending.",
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
                        'msg': "Delighted that the danger is over, a ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Now it's surely time for a happy ending.",
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
                        'msg': "Delighted that the danger is over, a swarm of special effects artists approaches, setting up equipment and green screens on all sides of you.",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Now it's surely time for a happy ending.",
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
                        'msg': "Delighted that the danger is over, a ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Now it's surely time for a happy ending.",
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
                        'msg': "Delighted that the danger is over, a ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Now it's surely time for a happy ending.",
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
                        'msg': "Delighted that the danger is over, a ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Now it's surely time for a happy ending.",
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
                        'msg': "Delighted that the danger is over, a ",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': '',
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "You briefly perceive a flash of light!",
                        'delay': DEFAULT_EVENT_DELAY,
                    },
                    {
                        'msg': "Now it's surely time for a happy ending.",
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
                'option_name': 'power of heart',
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
