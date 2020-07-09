from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].w_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].w_to = room['overlook']
room['foyer'].d_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].a_to = room['foyer']
room['narrow'].w_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

playername = input("Player Name: ")

direction = {
    "w": "North",
    "d": "East",
    "a": "West",
    "s": "South"
}

if len(playername) > 1:

    print(f"Glad you could join us, {playername}")

    # instantiate current player
    currentplayer = Player(playername, room["outside"])
    print(currentplayer.location)

    while True:
        
        userinput = input(">> ").lower()

        # supported keys (movement)
        if userinput in ["w", "a", "s", "d"]:
            print(f"You move to the {direction[userinput]}")
            movetolocation= getattr(currentplayer.location, f"{userinput}_to")
            if movetolocation == None:
                print("There is nothing to see here, try moving somewhere else")
            else:
                currentplayer.location = movetolocation
                print(currentplayer.location)

        # quitting with confirmation
        if userinput == "q":
            print("Are you sure you want to quit?")
            quitterinput = input("Quit? y / n: ").lower()
            if quitterinput == "y":
                break

        # unknown key handler
        elif userinput not in ["w", "a", "s", "d"]:
            print("Try using movement keys WASD, or Q to quit!")
else:
    print("You must choose a name for yourself")

