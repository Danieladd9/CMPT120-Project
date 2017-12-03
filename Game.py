# Introduction to Programming
# Author: Daniel Addison
# Date: 12/2/2017

class Location:
    def __init__(self, shortName, items, description):
        self.description = description
        self.name = shortName
        self.items = items
        self.hasVisited = False
        self.hasSearched = False
    def search(self):
        print("you see the following items " + self.items)
        self.hasSearched = True
    def look(self):
        print("\nYour current Location is " + self.description)
    def take(self, item):
        if self.hasSearched == True:
            if item in self.items:
                print("you picked up a " + item)
                self.items = "none"
                return item
            else:
                print("there nothing there to take")
        else:
            print("You do not see anything")
    #def drop():

        
        
        


class Player:
    def __init__(self, userName):
        self.x = 1
        self.y = 4
        self.userName = userName
        self.inventory = []
        self.score = 5
        self.moves = 20
        self.location = 3
    def updateLocation(self):
        self.location = worldMatrix[self.y][self.x]
    #def use():
        
    

locations = [
    Location("ghostrider", "camera", "Ghostrider: A wooden rollercoaster, is the longest, \
tallest roller-coaster made to scare kids as if they were in a pirate ship."),
    Location("xcelerator", "none", "Xcelerator: This rocket looking roller-coaster, is the \
fastest ride at Knott’s going 0.82 mph in 2.3 sec."),
    Location("boomerang", "none", "Boomerang: Have you ever took a rollercoaster ride and \
back again twice going 0 to 55 in 3 sec."),
    Location("funnelCake", "fries", "The Funnel Stand: The Best funnel cake you would buy at an amusement park, \
you haven't had anything good till you tried it."),
    Location("bullet", "map", "Bullet: Our new fastest Roller-coaster to date with VR technology for the experience."),
    Location("bathroom", "none", "Bathroom: we understand that your so scared,\
but wait till you go to the bathroom for an even bigger surprise."),
    Location("spaceShuttle", "none", "Space Shuttle: Bus to carry you to the rides."),
    Location("cottoncandy", "waterbottle", "Cotton Candy: right by funnel cake, best cotton candy you ever had."),
    Location("beachLagoon", "none", "BeachLagoon: Slip and Slide."),
    Location("paperworld", "none", "Paperworld: Learn about the paper route empire."),
    Location("waterslide", "bucket", "Extreme water unlike like you ever seen"),
    Location("legoblockland", "legos", "Build your way out the land")
    ]

#new for project4  items,
#this array holds the description of the players location
#global need it for game
#We craeted a matrix grid for Project4
#location names are index's for the locationDiscription list
inventory =[]
worldMatrix = [
[ -1,-1,-1, -1,-1],
[ -1, 7, 6, 8, -1],
[ -1, 5, 1, 10,-1],
[ -1, 2, 0, 11 -1],
[ -1, 3, 4, 9, -1],
[ -1,-1,-1,-1, -1]
]
#-------------------------------------------------------------------------------------------------------------------------------------------------
#Added Two new Locations for Project4
#locationDiscription=["Ghostrider: A wooden rollercoaster, is the longest, \
#tallest roller-coaster made to scare kids as if they were in a pirate ship.",
#                     "Xcelerator: This rocket looking roller-coaster, is the \
#fastest ride at Knott’s going 0.82 mph in 2.3 sec.",
#                     "Boomerang: Have you ever took a rollercoaster ride and back again twice going 0 to 55 in 3 sec.",
#                     "The Funnel Stand: The Best funnel cake you would buy at an amusement park, \
#you haven't had anything good till you tried it.",
#                     "Bullet: Our new fastest Roller-coaster to date with VR technology for the experience.",
#                     "Bathroom: we understand that your so scared,\
#but wait till you go to the bathroom for an even bigger surprise.",
#                     "Space Shuttle: Bus to carry you to the rides.",
#                     "Cotton Candy: right by funnel cake, best cotton candy you ever had.",
#                     "BeachLagoon: Slip and Slide.",
#                     "Paperworld: Learn about the paper route empire."]
#shortName = ["ghostRider", "xcelerator", "boomerang", "funnelCake", "bullet", "bathRoom", "spaceShuttle", "cottonCandy", "beachLagoon", "paperWorld"]
#items     = ["camera",       "none",        "none",   "fries",       "map",    "none",     "none",         "waterBottle",   "none",       "none"]
#hasSearched = [False, False, False, False, False, False, False, False, False, False]
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#newloc   
#playerScore = 5 
#playerLocation = 3

#Booleans
#this is how we know where the player has been
#hasVisited=[False,False,False,True,False,False,False,False,False,False]

#Time Limit
#playerMoves = 20
playerInput = 3
#playerName = ""
def playerCustomization():
#    global playerName
    playerName = input("What is your name? ")
    player1 = Player(playerName)
    print ("\nHi " + player1.userName + " Welcome to Knott’s Scary Farm.")
    print("\nTo get the commands of the game type help.")
    return player1

def printTitleIntro():
    print("Welcome to Knott's Scary Farm!")
    print("==============================\n")
    print("Come to get scared from your socks this October for a very special night on Halloween.\n")
    
def printEndingCopyright():
    print("\nYou went home after a long day of Fright Fest.")
    print("\nCopyright 2017 Daniel Addison Daniel.addison1@marist.edu")
    
def initGameData():                                   
    #newloc
#    global playerScore
#    playerScore = 5
#    global playerLocation
#    playerLocation = 3
#Player starts off in the funnel cake which has coords Y 4 X 1
#    global playerY
#    global playerX
#    playerY = 4
#    playerX = 1
    
    #Booleans
    #this is how we know where the player has been
#    global hasVisited
#    hasVisited = [0,0,0,0,0,0,0,0,0,0]
    
    #Time Limit
#    global playerMoves
#    playerMoves = 20

    print("\n" + locations[3].description)
    locations[3].hasVisited = True
    
def showScene(player1):
#    global locationDiscription
#    global playerLocation

    #if the player has visited show them the short discritpion if they have not show them the long one
    if locations[player1.location].hasVisited:
        print("\n You are at " + locations[player1.location].name)
    else:
        print("You are at " + locations[player1.location].description)
    
def processInput():
    global playerInput
    playerInput = input("\nplease enter a command: ").lower()
    
def updateGame(player1):
    #this check if the player has any moves left
#    global playerMoves
#    global playerName
#    global playerLocation
    global playerInput
    if player1.moves == 0:
        running = False
#checks if the player has entered a direction 
    elif playerInput == "north" or playerInput == "south" or playerInput == "east" or playerInput == "west":
        moveTo(player1)
    elif playerInput == "help":
        print("\nThe commands to this game is: North, South, East, West, Help, Points, Map, look, search, take, and Quit")       
    elif playerInput == "quit":
        print("\nGoodbye, Thank You for playing.")
        printEndingCopyright()
        quit()
    elif playerInput == "points":
        print("\nYour current score is " + str(player1.score))
    elif playerInput == "look":
        locations[player1.location].look()
    elif playerInput == "search":
        locations[player1.location].search()
    elif playerInput == "take":
        item = input("\nWhat would you like to take? ").lower()
        player1.inventory.append(locations[player1.location].take(item))
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
def moveTo(player1):
#    global playerScore
#    global playerLocation
#    global playerY
#    global playerX
#    global playerMoves
#copies the player coords in case the player can not move the direction they want
    tempX = player1.x
    tempY = player1.y
#gets a change in the list index given which direction the player entered
    if playerInput == "north" and player1.y >= 0:
        player1.y = player1.y - 1
    elif playerInput == "south" and player1.y < 5:
        player1.y = player1.y + 1
    elif playerInput == "east" and player1.x < 4:
        player1.x = player1.x + 1
    elif playerInput == "west" and player1.x >= 0:
        player1.x = player1.x - 1
    #makes sure the new location isn't -1 which is the value that means no location
    if worldMatrix[player1.y][player1.x] != -1:
        #take away one move form the player moves
        player1.moves -= 1
        player1.updateLocation()
        #shows scene right before change the boolean of visited to True
        showScene(player1)
        if not locations[player1.location].hasVisited:
            player1.score = player1.score + 5
            locations[player1.location].hasVisited = True
    else:
        print("You can't go", playerInput)
        player1.x = tempX
        player1.y = tempY
        
def checkForWin(player1):
    if player1.moves <= 0:
        runOutOfMoves()
        return False
    #if player is at ghost rider and they have a camera make them lose
    elif player1.location == 1 and "camera" in player1.inventory:
        lose()
        return False
    #if player is at beach lagon and has fries they win
    elif player1.location == 9 and "fries" in player1.inventory:
        win()
        return False
    return True
    
    


def win():
    print("you Win!")
    
def lose():
    print("you dropped your camera while on the xcelerator and it broke, please try again")

def runOutOfMoves():
    print("You've ran out moves")
    
def gameLoop(player1):
    running = True
    while running:
        processInput()
        updateGame(player1)
        running = checkForWin(player1)
def main():
    printTitleIntro()
    player1 = playerCustomization()
    initGameData()
    gameLoop(player1)
    printEndingCopyright()
main()

#make a new elif statement after it checks for directions then just have it print something like discriptions[location]
#make a new list of 10 things that has None for all and then have 3 items have a list
#make a new list of booleans all false that is if searched
#then add a search thing that makes that list of booleans true
#pick a location make an if statement in the go to then add a if item in statement then choose win or lose given a location

