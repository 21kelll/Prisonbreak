room_list = []
inventory = []

# -- initial room (0)
room = [" You stumbl", None, None, 1, None]
room_list.append(room)

# -- hallway between cell and shower (1)
room = ["description", 0, 3, 2, None]
room_list.append(room)

# -- shower (2)
room = ["description", 1, None, None, None]
room_list.append(room)

# -- hallway in front of supply room (3)
room = ["description", 4, 5, None, 1]
room_list.append(room)

# -- supply room (4)
room = ["description", None, None, 3, None]
room_list.append(room)

# -- hallway between warden's office and cafeteria (5)
room = ["description", 6, 8, 7, 3]
room_list.append(room)

# -- warden's office (6)
room = ["description", None, None, 5, None]
room_list.append(room)

# -- cafeteria (7)
room = ["description", 5, None, None, None]
room_list.append(room)

# -- hallway between yard and exit (8)
room = ["description", 9, None, 10, 5]
room_list.append(room)

# -- yard (9)
room = ["description", 12, None, 8, None]
room_list.append(room)

# -- alpha (12)
room = ["description", None, None, 9, None]
room_list.append(room)

# -- exit (10)
room = ["description", 8, None, 11, None ]
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
        next_room = current_room[1]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
        
    # -- East
    elif userInput.lower() == "e":
        next_room = current_room[2]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room

    # -- South
    elif userInput.lower() == "s":
        next_room = current_room[3]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room

        # -- West
    elif userInput.lower() == "w":
        next_room = current_room[4]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
