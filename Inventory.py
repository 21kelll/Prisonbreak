# Define name for the player
name = str(input("What is your name? "))

hasKey = False
hasUniform = False
onQuest = False
hasToothbrush = False
hasTeddy = False

# This is to define the talk functions and dialogue for each NPC

def beardedprisoner1(name):
    print("You approach the bearded prisoner")
    print("The bearded prisoner yawns... 'What was your name again? Oh yeah...,", name, """ 
, good morning. This place sucks. I wish I could get outta here like the last guy to escape. He just grabbed some guard
clothes and strolled outta here, pretending to be a guard... I don't even know where he found those clothes."
He was a genius, that guy'""")


def talk():
    print("There are multiple prisoners in your cell. One is bearded and lying on the bed,"
          " another is sitting against the wall")
    approach = str(input("Would you like to approach the bearded prisoner? (y/n): "))
    approachCheck = approach.lower()
    if approachCheck == 'y':
        beardedprisoner1(name)
    elif approachCheck == "n":
        print("You decide not to talk to the bearded prisoner")
    else:
        print("Error: Invalid input. Only y or n is accepted")
        talk()


def gamestarttext():
    print("""You wake up, startled. Shaking your head ,you slowly get up. 
You are inside of a prison cell. You have been wrongly convicted of a crime, 
you have to escape!""")
    talk()


gamestarttext()

room_list = []

# -- initial room (0)
room = ["""You are back in your cell and see the prisoners again. One is bearded and lying on the bed, another is 
sitting against the wall. To the south, the door to the hallway has been left open""", None, None, 1, None]
room_list.append(room)

# -- hallway between cell and shower (1)
room = ["""You find yourself at the east end of the hallway next to your cell, and on the north side of the hallway is
your cell, on the south side of the hallway is a door, you could also move east deeper near the middle of the 
hallway""", 0, 3, 2, None]
room_list.append(room)

# -- shower (2)
room = ["""You find yourself inside of the bathroom, looking around you notice the mouldy tiles and shower curtains. 
On the ground you see a toothbrush with the name "Alpha" scribbled on the neck in what looks like a child's handwriting.
You also see a bar of soap sitting on the broken sink. The door to back the hallway is north""", 1, None, None, None]
room_list.append(room)

# -- hallway in front of supply room (3)
room = ["""You are now near the middle of your hallway closer to your cell. On the north side of the hallway, 
there is one door with the words, "SUPPLY ROOM" in bold above it. If you go west, you will approach the hall by your 
cell, towards the east you could go further into the hallway""", 4, 5, None, 1]
room_list.append(room)

# -- supply room (4)
room = ["""The supply room is locked, it seems like you need a key""", None, None, 3, None]
room_list.append(room)

# -- hallway between warden's office and cafeteria (5)
room = ["""You are now closer the west end of the hallway away from your cell, you see two doors on both sides of you. 
'Wow, this prison is designed terribly', you think to yourself as you examine the doors. To the north is the 
Warden's office, and on the other side is the doorway to the cafeteria, the smell of the horrible food wafting in 
your direction.""", 6, 8, 7, 3]
room_list.append(room)

# -- warden's office (6)
room = ["""You step into the warden's office, at the far end of the room on his desk are some keys, directly to your 
right is the warden's coat on a coat hanger""", None, None, 5, None]
room_list.append(room)

# -- cafeteria (7)
room = ["""Stepping into the cafeteria you are confronted by a sight, you see a rotten apple sitting on the table and 
and a plate of food that smells like it has been there for weeks. You also see a teddy bear on the desk with its ear
worn off, there is a small name tag on the bottom that reads the name "Alpha". To the north is the exit back into the
 hallway""", 5, None, None, None]
room_list.append(room)

# -- hallway between yard and exit (8)
room = ["""You are now at the west end of the hallway furthest from your cell and find that the exit is to your south.
To the north you also see the doorway that opens into the yard where the other prisoners hang around.""", 9, None, 10,
        5]
room_list.append(room)

# -- yard (9)
room = ["""You tentatively step into the yard, careful not to strut or draw attention from the other prisoners.
Some are grunting while bench pressing in the corner. Others are playing a game of ball in the middle on the 
the cracked court. In the distance on the other end of the yard, you see a crowd of prisoners hanging out. The one in 
the middle looks like the boss. You think to yourself, you can retreat south back into the hallway or you can go 
further north into the yard to where the boss is. But is that a good idea?""", 12, None, 8, None]
room_list.append(room)

# -- alpha (12)
room = ["""You go further north into the yard towards the big boss. He looks you up and down with a smirk on his face. 
You are surrounded on your left and right by the fence. And you think of fleeing back south to the first part of the 
yard.""", None, None, 9, None]
room_list.append(room)

# -- exit (10)
room = ["""You near the door to the exit, but as you try to do so, a guard behind you sees you and sounds the alarm!!
The guard nears you and grabs your arm and chuckles... "Bad idea buddy". Go back inside.""", 8, None, None, None]
room_list.append(room)

# -- freedom (11)
room = ["""Wearing the guard uniform you found, you confidently walk out the exit. The guard greets you with a nod, 
and continues on with his business."""]
room_list.append(room)

# -- Starting point
current_room = 0

# -- Main Loop
finished = False

while not finished:
    print(room_list[current_room][0])

    if current_room == 12:
        if onQuest is False:
            approach = input("Would you like to approach him? (y/n)")
            approachcheck = approach.lower()
            if approachcheck == 'y':
                print("Hey new guy. So you wanna get out huh?")
                onQuest = True
            elif approachcheck == "n":
                pass
            else:
                print("Error: Invalid input. Only y or n is accepted")

        else:
            if hasToothbrush and hasTeddy:
                print("Thanks (text) Here's the key.")
                hasKey = True
            else:
                print("It doesn't look like you have my stuff...")


    # Ending game if prisoner comes free
    if current_room == 11:
        print("... Thanks for playing " + name + "! You've completed the game.")

    # conversation with alpha
    if current_room == 4 and hasKey is True:
        print("You take the guard clothes ")
        hasUniform = True

    if hasUniform is True:
        room_list[10].remove(room_list[10][3])
        room_list[3].insert(room_list[10][3], 11)

    if hasKey is True:
        room_list[4].remove(room_list[4][0])
        room_list[4].insert(room_list[4][0], "new description of supply room now open")
        openSupply = True

    if onQuest is True and current_room == 2:
        userTake = input("Do you want to take the toothbrush?: ")
        if userTake == "y":
            hasToothbrush = True
        else:
            print("You leave the toothbrush as it is.")

    if onQuest is True and current_room == 7:
        userTake = input("Do you want to take the teddy bear?: ")
        if userTake == "y":
            hasTeddy = True
        else:
            print("You leave the teddy bear as it is.")

    userInput = input("Which direction would you like to go?: ")

    # -- Quit
    if userInput.lower() == "q":
        print("Game over! Better luck next time.")
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
    else:
        print("That's not a valid input.")
