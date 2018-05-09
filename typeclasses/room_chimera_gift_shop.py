import random
import datetime

from evennia import CmdSet, Command
from evennia import create_object
from evennia import DefaultRoom, DefaultObject
from evennia import DefaultExit
from evennia import TICKER_HANDLER


GIFT_SHOP_ITEMS = [
    {
        'key': 'small',
        'shelf command name': 'left shelf',
        'shelf description': '|cSmall|n gifts for your friends! Only |c%s|n points!',
        'item price': 10,
        'items': [
            {
                'names': ['Baby Chimera Keychain','keychain'],
                'desc': "Aren't they cute when they're little? 1/50th Scale.",
            },
            {
                'names': ['Sourvenir Pin', 'pin'],
                'desc': "Proudly identifies you as a \"Thrill Seeker!\"",
            },
            {
                'names': ['Chimera Mug', 'mug'],
                'desc': "Changes color depending on your drink's temperature.",
            },
            {
                'names': ['Flip Flops', 'flip flop'],
                'desc': "The squishy soles are meant to withstand multiple hours of standing in line.",
            },
            {
                'names': ['Cottom Candy'],
                'desc': "It tastes different with every bite.",
            },
            {
                'names': ['Souvenir Park map', 'map'],
                'desc': "An illustration of the park from above.",
            },
            {
                'names': ['Chimera Scented Candle', 'candle'],
                'desc': "You won't always be here at the park, but you can always smell like you are!",
            },
            {
                'names': ['Paper Fan', 'fan'],
                'desc': "Flap this back and forth to cool down your sweaty face!",
            },
            {
                'names': ['Chimera Cookie Cutter', 'cookie cutter'],
                'desc': "It bends out of shape easily.",
            },
            {
                'names': ['Sunglasses', 'sunglass'],
                'desc': "If you wear them, you won't be able to see what people are emoting.",
            },
            {
                'names': ['Pegasus Pencil', 'pencil'],
                'desc': "Carved out of real Pegasus hoof. Or so it claims.",
            },
            {
                'names': ['Headphones', 'head phones'],
                'desc': "If you wear them, you won't be able to hear what people are saying.",
            },
            {
                'names': ['Wyvern Onesie', 'onesie'],
                'desc': "For the little monster back at home!",
            },
            {
                'names': ['Ghostly Glowstick', 'glowstick'],
                'desc': "Filled with donated ectoplasm.",
            },
            {
                'names': ['20-sided Dice', 'dice', 'd20'],
                'desc': "In case you need to attempt something dangerous.",
            },
        ],
    },
    {
        'key': 'medium',
        'shelf command name': 'middle shelf',
        'shelf description': 'These |cmedium|n items are fantastic merchandise for |c%s|n points!',
        'item price': 20,
        'items': [
            {
                'names': ['Chimera Canteen'],
                'desc': "Helps you quench your thirst throughout your visit.",
            },
            {
                'names': ['The Guidebook to Chimera Training'],
                'desc': "It's the ultimate guide to starting your own career in Mythical Beast Management!",
            },
            {
                'names': ['Scaly Shirt'],
                'desc': "Show off your inner reptile with this patterned tee!",
            },
            {
                'names': ['Baseball Cap'],
                'desc': "It's even got horns!",
            },
            {
                'names': ['Unicorn Pillow'],
                'desc': "Everyone loves unicorns, even though they don't exist.",
            },
            {
                'names': ['Chimera Coaster Set'],
                'desc': "Keeps your tables dry and your drinks elevated! Fun at parties.",
            },
            {
                'names': ['Selkie Scarf'],
                'desc': "Seals in your natural warmth.",
            },
            {
                'names': ['Umbrose Umbrella'],
                'desc': "Useful in both sun and rain.",
            },
            {
                'names': ['Chimera Plush Toy'],
                'desc': "It's softer and more huggable than a real Chimera.",
            },
            {
                'names': ['Chia-Mera Pet'],
                'desc': "The leaves of your plant will look like its hair!",
            },
        ],
    },
    {
        'key': 'large',
        'shelf command name': 'top shelf',
        'shelf description': 'Really nice |clarge|n items for |c%s|n points!',
        'item price': 50,
        'items': [
            {
                'names': ['Mystical Blanket', 'blanket'],
                'desc': "The weaving process is a closely kept secret.",
            },
            {
                'names': ['Hydra\'s Cube', 'hydra'],
                'desc': "Every time you solve a side, it seems to gain one?!",
            },
            {
                'names': ['Musical Snowglobe'],
                'desc': "Wind it up and watch it snow on a miniature version of the park!",
            },
            {
                'names': ['Chimera Chronometer'],
                'desc': "Never run out of time again with this classic instrument.",
            },
            {
                'names': ['Chimera Figurine'],
                'desc': "A collector's replica carved with care. Not a toy!",
            },
        ],
    },
    {
        'key': 'legendary',
        'shelf command name': 'behind the counter',
        'shelf description': 'Purchase these |clegendary|n, one of a kind items for |c%s|n points!',
        'item price': 100,
        'items': [
            {
                'names': ['Lucky Charm'],
                'desc': "Holding on to this might make your day a little better. Might.",
            },
        ],
    },
]

    
class GiftShopItem(DefaultObject):
    "Gift Shop Item"
    def at_object_creation(self):
        "Called whenever a new object is created"
        
        # lock the object down by default
        self.locks.add("get:false()")
        self.locks.add("drop:false()")
        
        self.db.get_err_msg = "Security guard: \"Hey! Is that yours? Better leave it right where it is.\""
        self.db.drop_err_msg = "Security guard: \"Wait up! I think you dropped this! Good thing I was around.\""


class CmdBuyGiftShopObject(Command):
    """
    Buy an item from the gift shop.

    Usage:
      buy <item name>
    """
    key = "buy"
    aliases = ["purchase"]
    help_category = "The Ride"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        location = caller.location

        # Did they specify an object?
        if not self.args:
            caller.msg("buy <item name>")
            return

        # Try to get from config dictionary
        target_shelf_info = None
        target_info = None # Leave target_info as None if it doesn't exist

        arg_name = ("%s" % self.args).strip().lower()
        # Look on each shelf
        for shelf_info in GIFT_SHOP_ITEMS:
            # Look at all items on the shelf
            for item_info in shelf_info['items']:
                # Look at all names for a particular item
                for item_name in item_info['names']:
                    # Cast both to lower and trim for best chance of a match
                    valueA = item_name.strip().lower()
                    if valueA == arg_name:
                        # Found a match
                        shelf_info = target_shelf_info = shelf_info
                        target_info = item_info
                        break

                if target_info:
                    break
            
            if target_info:
                break


        # Is that object on the 'for-sale' list?
        if not target_info:
            caller.msg("We don't have anything like that here.")
            return

        # Can the player afford it?
        target_cost = target_shelf_info['item price']
        player_can_afford = caller.db.pass_points >= target_cost
        if not player_can_afford:
            caller.msg("I'm sorry, you cannot afford that item. It costs |c%s|n points and you have |c%s|n points." % (target_cost, caller.db.pass_points))
            return

        # Give the player their item and take their points
        caller.db.pass_points = caller.db.pass_points - target_cost # Pay for item
        target_name = target_info['names'][0]
        new_item = create_object(GiftShopItem, key=target_name, location=caller) # Receive item
        new_item.db.desc = target_info['desc']

        msg = "Store attendant: \"Here you are! Enjoy your |m%s|n!\n|c%s|n points have been deducted from your park pass. Your new balance is |c%s|n." % (target_name, target_cost, caller.db.pass_points)
        caller.msg(msg)


class CmdShelfSmall(Command):
    """
    Look at the small item shelf.
    """
    key = "left shelf"
    aliases = ["left", "small", "small shelf"]
    help_category = "The Ride"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        location = caller.location

        location.display_shelf(caller, 'small')


class CmdShelfMedium(Command):
    """
    Look at the medium item shelf.
    """
    key = "middle shelf"
    aliases = ["middle", 'medium', 'medium shelf']
    help_category = "The Ride"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        location = caller.location

        location.display_shelf(caller, 'medium')


class CmdShelfLarge(Command):
    """
    Look at the large item shelf.
    """
    key = "top shelf"
    aliases = ["top", 'large', 'large shelf']
    help_category = "The Ride"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        location = caller.location

        location.display_shelf(caller, 'large')


class CmdShelfLegendary(Command):
    """
    Look at the legendary item shelf.
    """
    key = "behind the counter"
    aliases = ["behind", 'counter', 'legendary', 'legend', 'legendary shelf']
    help_category = "The Ride"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        location = caller.location

        location.display_shelf(caller, 'legendary')


class CmdSetGiftShop(CmdSet):
    """This groups the commands"""
    key = "Gift Shop Commands"

    def at_cmdset_creation(self):
        """Called at first cmdset creation"""
        self.add(CmdBuyGiftShopObject())

        self.add(CmdShelfSmall())
        self.add(CmdShelfMedium())
        self.add(CmdShelfLarge())
        self.add(CmdShelfLegendary())


class ChimeraGiftShopRoom(DefaultRoom):
    
    def at_object_creation(self):
        super(ChimeraGiftShopRoom, self).at_object_creation()

        self.cmdset.add_default(CmdSetGiftShop)

    def return_appearance(self, looker, **kwargs):
        msg = ""

        msg += "You are standing in a gift shop with shelves of merchandising lining every wall.\n"
        msg += "Type the name of a shelf to see more details about the items that are there.\n"

        # For each shelf
        for shelf_info in GIFT_SHOP_ITEMS:
            shelf_desc = shelf_info['shelf description'] % (shelf_info['item price'])
            msg += "  |g%s|n: %s\n" % (shelf_info['shelf command name'], shelf_desc)

            # For all items on a shelf
            #for item_info in shelf_info['items']:
            #    msg += "    |m%s|n: %s\n" % (item_info['names'][0], item_info['desc'])

        self.db.desc = msg

        return super(ChimeraGiftShopRoom, self).return_appearance(looker, **kwargs)

    def display_shelf(self, caller, shelf_key):
        msg = ""

        msg += "You look at the items on the shelf.\n"

        # For each shelf
        target_shelf = None
        for shelf_info in GIFT_SHOP_ITEMS:
            if shelf_info['key'] == shelf_key:
                target_shelf = shelf_info
                break

        if not target_shelf:
            caller.msg("Could not find shelf.")
            return

        shelf_desc = target_shelf['shelf description'] % (target_shelf['item price'])

        msg += "%s\n" % (shelf_desc)

        # For all items on a shelf
        for item_info in target_shelf['items']:
            msg += "  |m%s|n: %s\n" % (item_info['names'][0], item_info['desc'])

        msg += "Type |gbuy <item name>|n to purchase any of these wonderful items!"

        caller.msg(msg)