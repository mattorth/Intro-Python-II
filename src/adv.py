from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Hatchet", "A small axe")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Rope", "For all your binding needs")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Flint", "Fire starter")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Torch", "Let there be light")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Coin", "Silver coin")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
user_name = input("What is your name, Quester? ")
new_player = Player(user_name, room['outside'], [Item("Flask", "Stay Hydrated")] )
new_player.print_inventory()
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

user = True
while not user == "q":
    print(f"\n{new_player}")

    user = input(f"""What action would you like to take?\n  
    [n] move north\n  
    [s] move south\n  
    [e] move east\n  
    [w] move west\n  
    [get {[i.name for i in new_player.current_room.items]}]\n  
    [drop {[i.name for i in new_player.items]}]\n  
    [i] inventory\n  
    [q] quit\n""")

    action = user.split()
    if len(action) == 1:
        if action[0] == "n":
            if new_player.current_room.n_to is not None:
                new_player.current_room = new_player.current_room.n_to
            else:
                print(f"Movement not allowed, {new_player.name}!")
        elif action[0] == "s":
            if new_player.current_room.s_to is not None:
                new_player.current_room = new_player.current_room.s_to
            else:
                print(f"Movement not allowed, {new_player.name}!")
        elif action[0] == "e":
            if new_player.current_room.e_to is not None:
                new_player.current_room = new_player.current_room.e_to
            else:
                print(f"Movement not allowed, {new_player.name}!")
        elif action[0] == "w":
            if new_player.current_room.w_to is not None:
                new_player.current_room = new_player.current_room.w_to
            else:
                print(f"Movement not allowed, {new_player.name}!")
        elif action[0] == "i":
            new_player.print_inventory()
    elif len(action) == 2:
        if action[0] == ("get" or "take"):
            if any(item.name == action[1] for item in new_player.current_room.items):
                for i in new_player.current_room.items:
                    if i.name == action[1]:
                        i.on_take()
                        new_player.items.append(i)
                        new_player.current_room.items.remove(i)
            else:
                print(f"There is no {action[1]} here, {new_player.name}")
            # new_player.items.append(new_player.current_room.items[action[1]])
        elif action[0] == "drop":
            print("drop")
            if any(item.name == action[1] for item in new_player.items):
                for i in new_player.items:
                    if i.name == action[1]:
                        i.on_drop()
                        new_player.items.remove(i)
                        new_player.current_room.items.append(i)
            else:
                print(f"{action[1]} isn't in your inventory, {new_player.name}.")
            # if action[1] in new_player.items.name: new_player.items.remove()
                # if new_player.items[i].name == action[2]
                #     return remove(new_player.items[]
                #     remove(new_player.items[action[2]])

# def convert(lst): 
# return (lst[0].split()) 

# # Driver code 
# lst =  ["Geeks For geeks"] 
# print( convert(lst)) 







