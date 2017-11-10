# Introduction to Programming
# Author: Daniel Addison
# Date: 11/7/2017

#new for project3  
#this array holds the description of the players location
#global need it for game
#We craeted a matrix grid for Project4
worldMatrix = [
[ -1, -1, -1, -1, -1],
[ -1,  7,  6,  8, -1],
[ -1,  5,  1, -1, -1],
[ -1,  2,  0, -1, -1],
[ -1,  3,  4,  9, -1],
[ -1, -1, -1, -1, -1]
]
#Added Two new Locations for Project4
locationDiscription=["Ghostrider: A wooden rollercoaster, is the longest, \
tallest roller-coaster made to scare kids as if they were in a pirate ship.",
                     "Xcelerator: This rocket looking roller-coaster, is the \
fastest ride at Knott’s going 0.82 mph in 2.3 sec.",
                     "Boomerang: Have you ever took a rollercoaster ride and back again twice going 0 to 55 in 3 sec.",
                     "The Funnel Stand: The Best funnel cake you would buy at an amusement park, \
you haven't had anything good till you tried it.",
                     "Bullet: Our new fastest Roller-coaster to date with VR technology for the experience.",
                     "Bathroom: we understand that your so scared,\
but wait till you go to the bathroom for an even bigger surprise.",
                     "Space Shuttle: Bus to carry you to the rides.",
                     "Cotton Candy: right by funnel cake, best cotton candy you ever had.",
                     "BeachLagoon: Slip and Slide.",
                     "Paperworld: Learn about the paper route empire."]                                        
#newloc   
playerScore = 5 
playerLocation = 3

#Booleans
#this is how we know where the player has been
hasVisited=[False,False,False,True,False,False,False,False,False,False]

#Matrix we going to keep track of the player Y and X cord...
player = 4
player = 1

#Time Limit
playerMoves = 20
playerInput = 3
playerName = ""
def playerCustomization():
    global playerName
    playerName = input("What is your name? ")
    print ("\nHi " + playerName + " Welcome to Knott’s Scary Farm.")
    print("\nTo get the commands of the game type help.")

def printTitleIntro():
    print("Welcome to Knott's Scary Farm!")
    print("==============================\n")
    print("Come to get scared from your socks this October for a very special night on Halloween.\n")
    
def printEndingCopyright():
    print("\nYou went home after a long day of Fright Fest.")
    print("\nCopyright 2017 Daniel Addison Daniel.addison1@marist.edu")
    
def initGameData():                                   
    #newloc
    global playerScore
    playerScore = 5
    global playerLocation
    playerLocation = 3
    
    #Booleans
    #this is how we know where the player has been
    global hasVisited
    hasVisited = [False,False,False,True,False,False,False,False,False,False]

    #Time Limit
    global playerMoves
    playerMoves = 20
    
def showScene():
    global locationDiscription
    global playerLocation

    print("\nYour current Location is " + locationDiscription[playerLocation])
    
def processInput():
    global playerInput
    playerInput = input("\nplease enter a command: ").lower()
    
def updateGame():
    #this check if the player has any moves left
    global playerMoves
    global playerName
    global playerLocation
    global playerInput
    if playerMoves == 0:
        running = False
    if playerInput == "north":
        print("\n" + playerName + " chose north")
        playerMoves -= 1
        if playerLocation == 0:
            moveTo(1)
        elif playerLocation == 1:
            moveTo(6)
        elif playerLocation == 4:
            moveTo(0)
        elif playerLocation == 3:
            moveTo(2)
        elif playerLocation == 2:
            moveTo(5)
        elif playerLocation == 5:
            moveTo(7)       
        else:
            print("\nYou cannot go that way!")
            
    elif playerInput == "south":
        print("\n" + playerName + " chose south")
        playerMoves -= 1
        if playerLocation == 1:
            moveTo(0)
        elif playerLocation == 0:
            moveTo(4)
        elif playerLocation == 5:
            moveTo(2)
        elif playerLocation == 2:
            moveTo(3)
        elif playerLocation == 6:
            moveTo(1)
        elif playerLocation == 7:
            moveTo(5)
        else:
            print("\nYou cannot go that way!")
            
    elif playerInput == "east":
        print("\n" + playerName + " chose east")
        playerMoves -= 1
        if playerLocation == 5:
            moveTo(1)
        elif playerLocation == 2:
            moveTo(0)
        elif playerLocation == 3:
            moveTo(4)
        elif playerLocation == 7:
            moveTo(6)
        else:
            print("\nYou cannot go that way!")

    elif playerInput == "west":
        print("\n" + playerName + " chose west")
        playerMoves -= 1
        if playerLocation == 1:
            moveTo(5)
        elif playerLocation == 0:
           moveTo(2)
        elif playerLocation == 4:
            moveTo(3)
        elif playerLocation == 6:
           moveTo(7)
        else:
            print("\nYou cannot go that way!")
            
    elif playerInput == "help":
        print("\nThe commands to this game is: North, South, East, West, Help, Points, Map, and Quit")
        playerMoves -= 1        
    elif playerInput == "quit":
        print("\nGoodbye, Thank You for playing.")
        printEndingCopyright()
        quit()
    elif playerInput == "points":
        print("\nYour current score is " + str(playerScore))
        playerMoves -= 1
    #this is the player map
    elif playerInput == "map":
        print(" 7 - 6")
        print(" |   |")
        print(" 5 - 1")
        print(" |   |")
        print(" 2 - 0")
        print(" |   |")
        print(" 3 - 4")
        print("0: Ghostrider \n1: Xcelerator")
        print("2: Boomerang \n3: Funnelcake")
        print("4: Bullet \n5: Bathroom")
        print("6: Spaceshuttle \n7: Cottoncandy")
    
def moveTo(location):
    global hasVisited
    global playerScore
    global playerLocation
    global playerY
    global playerX
#if direction == "north"
#pick up from here on sunday
    if not hasVisited[location]:
        playerScore = playerScore + 5
        hasVisited[location] = True
    playerLocation = location
    
def gameLoop():
    running = True
    while running:
        showScene()
        processInput()
        updateGame()
def main():
    printTitleIntro()
    playerCustomization()
    initGameData()
    gameLoop()
    printEndingCopyright()
main()
