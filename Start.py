# Define name for the player
playername = str(input("What is your name?"))
# This is to define the talk functions and dialogue for each NPC


def beardedprisoner1():
    print("You approach the bearded prisoner")
    print("""The bearded prisoner yawns... 'What was your name again? Oh yeah...,""", playername, """ 
, good morning. This place sucks. I wish I could get outta here like the last guy to escape. He just grabbed some guard
clothes and strolled outta here, pretending to be a guard... I don't even know where he found those clothes."
He was a genius, that guy'""")


def talk():
    print("There are multiple prisoners in your cell. One is bearded and lying on the bed,"
          " another is sitting against the wall")
    approach = str(input("Would you like to approach the bearded prisoner?"))
    approachcheck = approach.lower()
    if approachcheck == 'yes':
        beardedprisoner1()
    elif approachcheck == "no":
        print("You decide not to talk to the bearded prisoner")
    else:
        print("Error: Invalid input. Only yes or no is accepted")
        talk()


def gamestarttext():
    print("""You wake up, startled. Shaking your head ,you slowly get up. 
You are inside of a prison cell. You have been wrongly convicted of a crime, 
you have to escape!""")
    talk()


gamestarttext()
