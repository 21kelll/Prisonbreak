room_list = []
inventory = []

# -- initial room (0)
room = ["""You are back in your cell and see the prisoners again. One is bearded and lying on the bed, another is 
sitting against the wall. The door to the hallway has been left open""", None, None, 1, None]
room_list.append(room)

# -- hallway between cell and shower (1)
room = ["""You find yourself at the end of the hallway next to your cell, on the opposite side of your cell there is a
 door, you could also move forward deeper near the middle of the hallway""", 0, 3, 2, None]
room_list.append(room)

# -- shower (2)
room = ["""You find yourself inside of the bathroom, looking around you notice the mouldy tiles and shower curtains. 
On the ground you see a toothbrush with the name "Alpha" scribbled on the neck in what looks like a child's handwriting.
You also see a bar of soap sitting on the broken sink.""", 1, None, None, None]
room_list.append(room)

# -- hallway in front of supply room (3)
room = ["""You are now near the middle of your hallway closer to your cell. There is one door with the words
  "SUPPLY ROOM" in bold above it. You can go back closer towards your cell, or go further into the hallway""", 4, 5, None, 1]
room_list.append(room)

# -- supply room (4)
room = ["""The supply room is locked, it seems like you need a key""", None, None, 3, None]
room_list.append(room)

# -- hallway between warden's office and cafeteria (5)
room = ["""You are now near the end of the hallway away from your cell, you see two doors on both sides of you. 'Wow, 
this prison is designed terribly', you think to yourself as you examine the doors. On one side of you is the Warden's 
office, and on the other side is the doorway to the cafeteria, the smell of the horrible food wafting in your direction.
""", 6, 8, 7, 3]
room_list.append(room)

# -- warden's office (6)
room = ["description", None, None, 5, None]
room_list.append(room)

# -- cafeteria (7)
room = ["description", 5, None, None, None]
room_list.append(room)

# -- hallway between yard and exit (8)
room = ["""You are now at the end of the hallway furthest from your cell and find that the exit is in front of you.
You also see the doorway that opens into the yard where the other prisoners hang around.""", 9, None, 10, 5]
room_list.append(room)

# -- yard (9)
room = ["""You tentatively step into the yard, careful not to strut or draw attention from the other prisoners.
Some are grunting while bench pressing in the corner. Others are playing a game of ball in the middle on the 
the cracked court. In the distance on the other end of the yard, you see a crowd of prisoners hanging out. The one in 
the middle looks like the boss. You think to yourself, you can try talk to the prisoners around you and you can go 
further into the yard to where the boss is. But is either a good idea?""", 12, None, 8, None]
room_list.append(room)

# -- alpha (12)
room = ["""You go further into the yard towards the big boss. He looks you up and down with a smirk on his face. 
You are surrounded on your left and right by the fence.""", None, None, 9, None]
room_list.append(room)

# -- exit (10)
room = ["""You near the door to the exit, but as you try to do so, a guard behind you sees you and sounds the alarm!!
The guard nears you and grabs your arm and chuckles... "Bad idea buddy".""", 8, None, 11, None ]
room_list.append(room)

# -- freedom (11)
room = ["description"]
room_list.append(room)

# -- Starting point
current_room = 0

# -- Main Loop
finished = False

while not finished:
    print(room_list[current_room][0])
    userInput = input("Which way?: ")

    # -- Quit
    if userInput.lower() == "q":
        print("Thanks for playing! Better luck next time.")
        break

    # -- North
    elif userInput.lower() == "n":
        next_room = room_list[current_room][1]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room

    # -- East
    elif userInput.lower() == "e":
        next_room = room_list[current_room][2]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room

    # -- South
    elif userInput.lower() == "s":
        next_room = room_list[current_room][3]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room

    # -- West
    elif userInput.lower() == "w":
        next_room = room_list[current_room][4]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
