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
    ["Left elbow room", 9, 7, True, False], # room 32
    ["Right elbow room", 7, 13, True, True], # room 33
    ["The science lab", 13, 13, False, True], # room 34
    ["The greenhouse", 13, 13, True, False], # room 35
    [PLAYER_NAME + "'s sleeping quaters", 9, 11, False, False], # room 36
    ["West corridor", 15, 5, True, True], # room 37
    ["The briefing room", 7, 13, False, True], # room 38
    ["The crew's community room", 11, 13, True, False], # room 39
    ["Main Mission Control", 14, 14, False, False], # room 40
    ["The sick bay", 12, 7, True, False], # room 41
    ["West corridor", 9, 7, True, False], # room 42
    ["Utilities control room", 9, 9, False, True], # room 43
    ["Systems engineering bay", 9, 11, False, False], # room 44
    ["Security portal to Mission Control", 7, 7, True, False], # room 45
    [FRIEND1_NAME + "'s sleeping quaters", 9, 11, True, True], # room 46
    [FRIEND2_NAME + "'s sleeping quaters", 9, 11, True, True], # room 47
    ["The pipeworks", 13, 11, True, False], # room 48
    ["The chief scientist's office", 9, 7, True, True], # room 49
    ["The robot workshop", 9, 11, True, False], # room 50
    ]

# sanity check on the map data
assert len(GAME_MAP)-1 == MAP_SIZE, "Map size and GAME_MAP don't match"

## MAKE MAP ##

def get_floor_type():
    if current_room in outdoor_rooms:
        return 2 # soil
    else:
        return 0 # tiled floor

def generate_map(): # This makes the map of the current room using room, scenery, and prop data.
    global room_map, room_width, room_height, room_name, hazard_map
    global top_left_x, top_left_y, wall_transparency_frame
    room_data = GAME_MAP[current_room]
    room_name = room_data[0]
    room_height = room_data[1]
    room_width = room_data[2]

    floor_type = get_floor_type()
    if current_room in range(1, 21):
        bottom_edge = 2 # soil
        side_edge = 2 # soil
    if current_room in range(21, 26):
        bottom_edge = 1 # wall
        side_edge = 2 # soil
    if current_room > 25:
        bottom_edge = 1 # wall
        side_edge = 1 # wall

    # Create top line of room map
    room_map=[[side_edge] * room_width]
    # Add lines
    for y in range(room_height - 2):
        room_map.append([side_edge] + [floor_type]*(room_width - 2) + [side_edge])