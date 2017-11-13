# Introduction to Programming
# Author: Daniel Addison
# Date: 11/9/2017
ghostRider = 0
xcelerator = 1
boomerang = 2
funnelCake = 3
bullet = 4
bathroom = 5
spaceShuttle = 6
cottonCandy = 7
beachLagoon = 8
paperWorld = 9

#new for project4  
#this array holds the description of the players location
#global need it for game
#We craeted a matrix grid for Project4
#location names are index's for the locationDiscription list
inventory =[]
worldMatrix = [
[ -1,           -1,     -1,        -1,          -1],
[ -1,  cottonCandy, spaceShuttle,  beachLagoon, -1],
[ -1,  bathroom,    xcelerator,    -1,          -1],
[ -1,  boomerang,   ghostRider,    -1,          -1],
[ -1,  funnelCake,  bullet,        paperWorld,  -1],
[ -1,           -1,     -1,        -1,          -1]
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
shortName =["ghostRider", "xcelerator", "boomerang", "funnelCake", "bullet", "bathroom", "spaceShuttle", "cottonCandy", "beachLagoon", "paperworld"]
items =    ["none",       "camera", "none",      "none",       "map",    "none",     "none",         "waterBottle",   "none",       "none"]
#newloc   
playerScore = 5 
playerLocation = 3

#Booleans
#this is how we know where the player has been
hasVisited=[False,False,False,True,False,False,False,False,False,False]

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
#Player starts off in the funnel cake which has coords Y 4 X 1
    global playerY
    global playerX
    playerY = 4
    playerX = 1
    
    #Booleans
    #this is how we know where the player has been
    global hasVisited
    hasVisited = [0,0,0,0,0,0,0,0,0,0]
    
    #Time Limit
    global playerMoves
    playerMoves = 20

    print("\n" + locationDiscription[funnelCake])
    
def showScene():
    global locationDiscription
    global playerLocation

    #if the player has visited show them the short discritpion if they have not show them the long one
    if hasVisited[playerLocation]:
        print("\n The player is at " +  shortName[playerLocation])
    else:
        print("\nYour current Location is " + shortName[playerLocation])
    
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
#checks if the player has entered a direction 
    elif playerInput == "north" or playerInput == "south" or playerInput == "east" or playerInput == "west":
        moveTo()
    elif playerInput == "help":
        print("\nThe commands to this game is: North, South, East, West, Help, Points, Map, look, search, take, and Quit")       
    elif playerInput == "quit":
        print("\nGoodbye, Thank You for playing.")
        printEndingCopyright()
        quit()
    elif playerInput == "points":
        print("\nYour current score is " + str(playerScore))
    elif playerInput == "look":
        print("\nYour current Location is " + locationDiscription[playerLocation])
    elif playerInput == "search":
        print("you see the following items " + items[playerLocation])
    elif playerInput == "take":
        if items[playerLocation] == "none":
            print("there nothing there to take")
        else:
            print("you picked up a " + items[playerLocation])
            inventory.append(items[playerLocation])
            items[playerLocation] = "none"
    #this is the player map
    elif playerInput == "map":
        print(" 7 - 6 - 8")
        print(" |   |")
        print(" 5 - 1")
        print(" |   |")
        print(" 2 - 0")
        print(" |   |")
        print(" 3 - 4 - 9")
        print("0: Ghostrider \n1: Xcelerator")
        print("2: Boomerang \n3: Funnelcake")
        print("4: Bullet \n5: Bathroom")
        print("6: Spaceshuttle \n7: Cottoncandy")
        print("8: beachLagoon \n9: PaperWorld")
def moveTo():
    global hasVisited
    global playerScore
    global playerLocation
    global playerY
    global playerX
    global playerMoves
#copies the player coords in case the player can not move the direction they want
    tempX = playerX
    tempY = playerY
#gets a change in the list index given which direction the player entered
    if playerInput == "north" and playerY >= 0:
        playerY = playerY - 1
    elif playerInput == "south" and playerY < 5:
        playerY = playerY + 1
    elif playerInput == "east" and playerX < 4:
        playerX = playerX + 1
    elif playerInput == "west" and playerX >= 0:
        playerX = playerX - 1
    #makes sure the new location isn't -1 which is the value that means no location
    if worldMatrix[playerY][playerX] != -1:
        location = worldMatrix[playerY][playerX]
        playerLocation = location
        #shows scene right before change the boolean of visited to True
        showScene()
        playerMoves -= 1
        if not hasVisited[location]:
            playerScore = playerScore + 5
            hasVisited[location] = True
    else:
        print("You can't go", playerInput)
        playerX = tempX
        playerY = tempY
        
def checkForWin():
    numberofplacesVisited = 0
    visits = 0
    for i in hasvisited:
        if i == 1:
            numberofplacesvisited += i
        visits += i
        if numberofplacesVisited == 10:
            win()
        elif visit > 10:
            lose()
def win():
    print("you Win!")
    
def lose():
    print("sorry you lost, please try again")
    
def gameLoop():
    running = True
    while running:
        processInput()
        updateGame()
def main():
    printTitleIntro()
    playerCustomization()
    initGameData()
    gameLoop()
    printEndingCopyright()
main()

#make a new elif statement after it checks for directions then just have it print something like discriptions[location]
#make a new list of 10 things that has None for all and then have 3 items have a list
#make a new list of booleans all false that is if searched
#then add a search thing that makes that list of booleans true
#pick a location make an if statement in the go to then add a if item in statement then choose win or lose given a location

