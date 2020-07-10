from room import Room
from player import Player
from Item import Item
from Weapon import Weapon
import random

# Declare all items

# common items/weapons
rustydagger = Weapon("Dagger", "Not much to it but it will do", "Common", 2)
frailbow = Weapon("Bow", "The bowstring is hanging on by a thread", "Common", 1)
fryingpan = Weapon("Pan", "Cooking eggs isn't its only use", "Common", 3)

bandaid = Item("BandAid", "Can cover up my boo boos", "Common")
rope = Item("Rope", "A sturdy rope", "Common")
bag = Item("Bag", "Guess I can carry more stuff now", "Common")

# rare items/weapons
glock = Weapon("Glock", "It's black and has straight edges to it", "Rare", 5)
lightsaber = Weapon("Lightsaber", "Where have I seen one of these before", "Rare", 7)
grenade = Weapon("Grenade", "Looks like a green pinecone", "Rare", 8)

medkit = Item("Medkit", "This will help me heal", "Rare")
damagepotion = Item("Potion", "Damage is boosted", "Rare")
treasurechest = Item("Chest", "Looks like it needs a key. I wonder what's inside", "Rare")

# legendary items/weapons
rpg = Weapon("RPG", "Now this will do some damage", "Legendary", 10)
godsword = Weapon("GodSword", "Left here by the gods for me", "Legendary", 10)
laserbeam = Weapon("Laser", "Hotter than the sun", "Legendary", 10)

bodyarmor = Item("Armor", "I wont take any damage with this", "Legendary")
chestkey = Item("Key", "A key made of solid gold", "Legendary")
cloak = Item("Cloak", "Where'd I go??", "Legendary")

commonpool = {
    "weapons": [rustydagger, frailbow, fryingpan],
    "items": [bandaid, rope, bag]
}

rarepool = {
    "weapons": [glock, lightsaber, grenade],
    "items": [medkit, damagepotion, treasurechest]
}

legendarypool = {
    "weapons": [rpg, godsword, laserbeam],
    "items": [bodyarmor, chestkey, cloak]
}

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



room['outside'].w_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].w_to = room['overlook']
room['foyer'].d_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].a_to = room['foyer']
room['narrow'].w_to = room['treasure']
room['treasure'].s_to = room['narrow']


# randomized loot and returns an array of three
def itemGetter():
    loot = []
    roll1 = random.randrange(1, 100)
    roll2 = random.randrange(1, 100)
    roll3 = random.randrange(1, 100)

    rollresults = [roll1, roll2, roll3]

    # adds loot to list
    def getLoot(loottype, pool):
        if loottype == "weapons":
            rtnLoot = random.choices(pool["weapons"])[0]

            # no duplicates
            if rtnLoot in loot:
                getLoot(loottype, pool)
            else:
                loot.append(rtnLoot)
        elif loottype == "items":
            rtnLoot = random.choices(pool["items"])[0]

             # no duplicates
            if rtnLoot in loot:
                getLoot(loottype, pool)
            else:
                loot.append(rtnLoot)

    # determines which pool to pull from
    for e in rollresults:
        if e >= 90:
            loottype = random.choices(list(legendarypool.keys()))[0]
            getLoot(loottype, legendarypool)
        if e >= 80 and e < 90:
            loottype = random.choices(list(rarepool.keys()))[0]
            getLoot(loottype, rarepool)
        if e >= 1 and e < 80:
            loottype = random.choices(list(commonpool.keys()))[0]
            getLoot(loottype, commonpool)
    
    return loot


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

    # instantiate loot in rooms
    room['foyer'].itempool = itemGetter()
    room['overlook'].itempool = itemGetter()
    room['narrow'].itempool = itemGetter()
    room['treasure'].itempool = itemGetter()


    while True:
        
        userinput = input(">> ").lower()

        # supported keys (movement)
        if userinput in ["w", "a", "s", "d"]:
            print(f"\nYou move to the {direction[userinput]}")
            movetolocation= getattr(currentplayer.location, f"{userinput}_to")
            if movetolocation == None:
                print("There is nothing to see here, try moving somewhere else")
            else:
                currentplayer.location = movetolocation
                print(currentplayer.location)
                currentplayer.location.viewitems()

        # checks if userinput has two words
        if len(userinput.split()) == 2:

            # supported action words
            if userinput.split()[0] not in ["grab", "view", "drop"]:
                print("Try grab/drop <item name> - 'view inventory' to see your inventory")

            # add inputed item to players inventory
            elif userinput.split()[0] == "grab":
                itemtograb = userinput.split()[1]
                itempoolnames = []

                # array of names only to determine if it exists in room
                for e in currentplayer.location.getItemPool():
                    itempoolnames.append(e.printName().lower())

                # check if items exist
                if itemtograb not in itempoolnames:
                    print("!! There's no such thing")

                # if they do adds them to inventory
                elif itemtograb in itempoolnames:
                    for e in currentplayer.location.getItemPool():
                        if itemtograb == e.printName().lower():

                            # inventory max size is 5
                            if len(currentplayer.inventory) < 5:

                                # adds to inv
                                currentplayer.inventory.append(e)
                                # removes from current room
                                currentplayer.location.itempool.remove(e)
                                print(e.ontake())
                                print(f"Inventory Contents: {len(currentplayer.inventory)}/5")

                            else:
                                print("Your inventory is full!")


            # view inventory
            elif userinput.split()[0] == "view":
                if userinput.split()[1] == "inventory":
                    print(currentplayer.showinventory())


            # drops items
            elif userinput.split()[0] == "drop":
                itemtodrop = userinput.split()[1]
                itemsininventory = []

                for e in currentplayer.inventory:
                    itemsininventory.append(e.printName().lower())

                if itemtodrop in itemsininventory:
                    for e in currentplayer.inventory:
                        if itemtodrop == e.printName().lower():
                            currentplayer.inventory.remove(e)
                            print(f"{e.printName()} was removed from your inventory")
                else:
                    print("You don't have that item in your inventory")

        # quitting with confirmation
        if userinput == "q":
            print("Are you sure you want to quit?")
            quitterinput = input("Quit? y / n: ").lower()
            if quitterinput == "y":
                break

        # unknown key handler
        elif userinput not in ["w", "a", "s", "d"] and len(userinput.split()) < 2:
            print("!! Try using movement keys WASD, or Q to quit! To grab an item type: grab <item name>")
else:
    print("You must choose a name for yourself")
