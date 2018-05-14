
# Game config
GAME_TITLE = "Mythari Park"
GAME_HELP_CATEGORY = "Mythari Park"

MAP_LINE_ROOM_OBJECT_NAME = "Waiting in Line" # This needs to be unique and return 1 result
MAP_GIFT_SHOP_OBJECT_NAME = "Chimera Gift Shop" # This needs to be unique and return 1 result

GAME_FEEDBACK_LOG_FILE_PATH = "D:/logs/mythari_park_feedback.log"
FEEDBACK_DISPLAY_EXCEPTIONS = False # In PROD this should be False

# Line Room
LINE_ROOM_BETWEEN_CARS_DELAY = 30
LINE_ROOM_BOARD_TIME_DELAY = 15
LINE_ROOM_PEOPLE_PER_CAR = 4
LINE_ROOM_DISPLAY_SECONDS_ELAPSED = False # In PROD this should be False

GUESS_NUMBER_GAME_MIN = 1
GUESS_NUMBER_GAME_MAX = 100

HOT_DOG_PRICE = 2 # Note: The vendor has a hard code talk_to_msg that shows the price in theride.ev

# Chimera Ride Room
CHIMERA_RIDE_DEFAULT_EVENT_DELAY = 5
CHIMERA_RIDE_TEST_BATTLE = False # In PROD this should be False
CHIMERA_RIDE_ADD_EVENT_NAME_PREFIX = False # In PROD this should be False

# Chimera Exit Room
PHOTO_PRICE = 2
PHOTO_ALBUM_MAX_NAME_LENGTH = 100


