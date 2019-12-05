import time

# This is to define the talk functions and dialogue for each NPC


def beardedprisoner1(player):
    print("There are multiple prisoners in your cell. One is bearded and lying on the bed,")
    time.sleep(2)
    print("You approach the bearded prisoner")
    time.sleep(1)
    print("The bearded prisoner yawns... ")
    time.sleep(1)
    print("Oh yeah...")
    time.sleep(1), player,
    print("""Good morning. This place sucks. I wish I could get outta here like the last guy 
to escape. He just grabbed some guard clothes and strolled outta here, pretending to be a guard...""")
    time.sleep(1)
    print("""I don't even know where he found those clothes. He was a genius, that guy'""")

# this is the function that begins the game. It will only run once


def gamestarttext():
    name = str(input("What is your name?: "))
    print("Welcome.", name)
    print("You wake up, startled. Shaking your head, you slowly get up")
    time.sleep(1.5)
    print("You are inside of a prison cell. You have been wrongly convicted of a crime...")
    time.sleep(2.5)
    print("You have to escape!")
    time.sleep(1)
    print("--------------------------------------------------------------------------")
    time.sleep(2)
    beardedprisoner1(name)

# dialogue for the alpha in the prison


def alpha():
    print("""The last guy that escape just grabbed guard clothes and left, said he found the keys to unlock the supply 
room in the warden’s office. It’s a shame now that they put a guard there…""")
    time.sleep(2)
    print("You know what. Maybe I could help you.")
    time.sleep(1)
    print("I lost some things around the prison that my mama gave to me, some of my treasured objects.")
    time.sleep(1.5)
    print("""Maybe if you found them and got them to me I could find 
a way to distract the guard away from the warden’s office.""")


gamestarttext()


def map1():
    room_list = []
    # -- initial room (0)
    room = ["""You are in your cell and see the prisoner. To the south, the door to the hallway has been left 
open""", None, None, 1, None]
    room_list.append(room)

    # -- hallway between cell and shower (1)
    room = ["""You find yourself at the east end of the hallway next to your cell, on the north side of the hallway is 
your cell, on the south side of the hallway is a door, you could also move east deeper near the middle of the 
hallway""", 0, 3, 2, None]
    room_list.append(room)

    # -- shower (2)
    room = ["""You find yourself inside of the bathroom. On the ground you see a toothbrush with the name "Alpha" 
scribbled on the neck in what looks like a child's handwriting. The door to back the hallway is 
north""", 1, None, None, None]
    room_list.append(room)

    # -- hallway in front of supply room (3)
    room = ["""You are now near the middle of your hallway closer to your cell. On the north 
side of the hallway, there is one door with the words, "SUPPLY ROOM" in bold above it. If you go west, you will 
approach the hall by your cell, towards the east you could go further into the hallway""", 4, 5, None, 1]
    room_list.append(room)

    # -- supply room (4)
    room = ["""The supply room is locked, it seems like you need a key""", None, None, 3, None]
    room_list.append(room)

    # -- hallway between warden's office and cafeteria (5)
    room = ["""You are now closer the west end of the hallway away from your cell, you see two doors on both sides 
of you. 'Wow, this prison is designed terribly', you think to yourself as you examine the doors. To the north is the 
Warden's office, and on the other side is the doorway to the cafeteria, the smell of the horrible food wafting in 
your direction.""", 6, 8, 7, 3]
    room_list.append(room)

    # -- warden's office (6)
    room = ["""You step into the warden's office, at the far end of the room on his desk are some keys, directly to your 
right is the warden's coat on a coathanger""", None, None, 5, None]
    room_list.append(room)

    # -- cafeteria (7)
    room = ["""Stepping into the cafeteria you are confronted by a sight, you see a rotten apple sitting on the table 
and a plate of food that smells like it has been there for weeks. You also see a teddy bear on the desk with its ear
worn off, there is a small name tag on the bottom that reads the name "Alpha". To the north is the exit back into 
the hallway""", 5, None, None, None]
    room_list.append(room)

    # -- hallway between yard and exit (8)
    room = ["""You are now at the west end of the hallway furthest from your cell and find that the exit is to your 
south. To the north you also see the doorway that opens into the yard where the other prisoners hang 
around.""", 9, None, 10, 5]
    room_list.append(room)

    # -- yard (9)
    room = ["""You step into the yard. Further north there is another crowd of prisoners, down south is the 
hallway?""", 12, None, 8, None]
    room_list.append(room)

    # -- exit (10)
    room = ["""You near the door to the exit, but as you try to do so, a guard behind you sees you and sounds the alarm!
The guard nears you and grabs your arm and chuckles... "Bad idea buddy".""", 8, None, 11, None]
    room_list.append(room)

    # -- freedom (11)
    room = ["You are free!"]
    room_list.append(room)

    # -- alpha (12)
    room = ["""You go further north into the yard towards the big boss. He looks you up and down with a smirk on his 
face. You are surrounded on your left and right by the fence. And you think of fleeing back south to the first part 
of the yard.""", None, None, 9, None]
    room_list.append(room)

    # -- Starting point
    current_room = 0

    # -- Main Loop
    finished = False

    while finished is False:
        hasKey = False
        hasUniform = False
        commotion = False
        onQuest = False
        hasTeddy = False
        hasToothbrush = False

        print(room_list[current_room][0])

        # to ensure that the player does not attempt to go into the wardens office without a commotion
        if current_room == 6 and commotion is False:
            print("You can hear some feet shuffling behind you... It must be a guard!")
            time.sleep(1.5)
            print("A guard suddenly appears behind you and places their hand on you shoulder.")
            print("""Snooping around the warden's office aye? That's not good. You're getting solitary confinement 
        for a few days...""")
            current_room = 0
            time.sleep(1)
            print("------------------------------------------")
            time.sleep(1)
            print("""You wake up after a few days in your cell. You probably shouldn't snoop around the warden's office
        while the guard is there...""")

        # for when there is a commotion and the warden's office is accessible
        if commotion is True:
            room_list[6].remove(room_list[6][0])
            room_list[6].insert(room_list[6][0], """You enter into the Warden's office as the guard deals with the 
        commotion in the yard. You spot the key on the Warden's desk and go to grab it... You now have the key!!""")

        # this is to ensure that the player does not attempt to escape prematurely
        if current_room == 10 and hasUniform is False:
            current_room = 0
            print("You wake up the next morning in your cell...")
            time.sleep(2)
            print("Your belongings were confiscated and are back to their original position")
            
        # before anything with booleans, we have to assure that the player gets put on their quest
        if current_room == 12:
            if onQuest is False:
                approach = input("Would you like to approach him? (y/n)")
                approachcheck = approach.lower()
                if approachcheck == 'y':
                    print("Hey chump, what’re you doing on my turf?")
                    time.sleep(2)
                    print("Oh… You want to escape?")
                    time.sleep(1)
                    print("Yeah…")
                    time.sleep(1)
                    print("The last guy that escape just grabbed guard clothes and left,")
                    time.sleep(1)
                    print("said he found the keys to unlock the supply room in the warden’s office.")
                    time.sleep(1)
                    print("It’s a shame now that they put a guard there…")
                    time.sleep(3)
                    print("You know what. Maybe I could help you.")
                    time.sleep(2)
                    print("I lost some things around the prison that my mama gave to me:")
                    print("""some of my treasured objects. Maybe if you found them and got them to me I could find a way 
                to distract the guard away from the warden’s office.""")
                    onQuest = True
                elif approachcheck == "n":
                    print("You decide not to approach him")
                    pass
                else:
                    print("Error: Invalid input. Only y or n is accepted")

            # when on quest in search of items
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

            # once commotion has started
            if commotion is True and current_room == 9:
                print("""There is a big commotion in the yard with the prisoners and the Guard is there trying to 
            break it up.""")

            # once the player has acquired all items and returned to alpha

            if hasToothbrush is True and hasTeddy is True:
                # starts commotion
                print("""'Thanks. I owe you one, consider this my way of repaying you...
            I'll make sure we start some commotion so we can distract the guard by the wardens office, 
            make sure you go in and grab the key.'""")
                commotion = True
                print("The alpha starts rounding up prisoners to start a commotion")
            elif hasToothbrush:
                print("'Thanks, Now go get my teddy'")
            elif hasTeddy:
                print("'Thanks, now go get my toothbrush'")
            else:
                print("'It doesn't look like you have my stuff...'")

        # when the supply room can be unlocked, removes the supply room from the list and adds in the newly open one
        if hasKey is True:
            room_list[4].remove(room_list[4][0])
            room_list[4].insert(room_list[4][0], "You open the supply room with the key. You manage to step inside.")

        # when has key

        if current_room == 4 and hasKey is True:
            time.sleep(1)
            print("In front of you there is a rack with multiple uniforms for guards.")
            time.sleep(2)
            print("There is one missing from the rack of spares...")
            time.sleep(2)
            print("The person who escaped must have taken that one..")
            time.sleep(1)
            print("You put on the guard uniform slowly with a sense of accomplishment")
            time.sleep(1)
            print("You will escape!")
            hasUniform = True

        if hasUniform is True:
            room_list[10].remove(room_list[10][3])
            room_list[3].insert(room_list[10][3], 11)

        # Ending game if prisoner comes free
        if current_room == 11:
            print("... Thanks for playing! You've completed the game.")

        # These are all of the direction and interactive codes. They are not part of the story.

        userInput = input("Which direction would you like to go?: ")

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


map1()
