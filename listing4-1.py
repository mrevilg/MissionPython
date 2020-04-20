import time, random, math

## VARIABLES ##

WIDTH = 800 # window size
HEIGHT = 800

# Player variables
PLAYER_NAME = "Stephen"
FRIEND1_NAME = "Danny G"
FRIEND2_NAME = "Luigi"
current_room = 31 # start room = 31

top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar, images.soil]

## MAP ##

MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT
GAME_MAP = [ ["Room 0 - where unused objects are kept", 0, 0, False, False] ]

outdoor_rooms = range(1, 26)
for planetsectors in range(1, 26): 
    GAME_MAP.append( ["The dusty planet surface", 13, 13, True, True] )

GAME_MAP += [
    #["Room Name", height, width, top exit?, right exit?] 
    ["The airlock", 13, 5, True, False], # room 26
    ["The engineering lab", 13, 13, False, False], # room 27
    ["Poodle Mission Control", 9, 13, False, True], # room 28
    ["The viewing gallery", 9, 15, False, False], # room 29
    ["The crew's bathroom", 5, 5, False, False], # room 30
    ["The airlock entry bay", 7, 11, True, True], # room 31
    
]

# sanity check on the map data
assert len(GAME_MAP)-1 == MAP_SIZE, "Map size and GAME_MAP don't match"