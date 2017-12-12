# Introduction to Programming
# Author: Daniel Addison
# Date: 12/2/2017

from Location import *
from Player import *

locations = [
    Location("ghostrider", ["camera"], "Ghostrider: A wooden rollercoaster, is the longest, \
tallest roller-coaster made to scare kids as if they were in a pirate ship."),
    Location("xcelerator", [], "Xcelerator: This rocket looking roller-coaster, is the \
fastest ride at Knott’s going 0.82 mph in 2.3 sec."),
    Location("boomerang", ["paperbag"], "Boomerang: Have you ever took a rollercoaster ride and \
back again twice going 0 to 55 in 3 sec."),
    Location("funnelCake", ["fries"], "The Funnel Stand: The Best funnel cake you would buy at an amusement park, \
you haven't had anything good till you tried it."),
    Location("bullet", ["map"], "Bullet: Our new fastest Roller-coaster to date with VR technology for the experience."),
    Location("bathroom", [], "Bathroom: we understand that your so scared,\
but wait till you go to the bathroom for an even bigger surprise."),
    Location("spaceShuttle", [], "Space Shuttle: Bus to carry you to the rides."),
    Location("cottoncandy", ["waterbottle"], "Cotton Candy: right by funnel cake, best cotton candy you ever had."),
    Location("beachLagoon", [], "BeachLagoon: Slip and Slide."),
    Location("paperworld", [], "Paperworld: Learn about the paper route empire."),
    Location("admissionoffice", ["pen"], "Admission Office: Regristiration and help desk"),
    Location("legoland", ["baby"], "LegoLand: Build your way out the land of legos")
    ]

playerInput = 3

#this makes the player instance and gets the username from player
def playerCustomization():
    playerName = input("What is your name? ")
    player1 = Player(playerName)
    print ("\nHi " + player1.userName + " Welcome to Knott’s Scary Farm.")
    print("\nTo get the commands of the game type help.")
    return player1

def printTitleIntro():
    print("\nWelcome to Knott's Scary Farm!")
    print("==============================\n")
    print("Come to get scared from your socks this October for a very special night on Halloween.\n")

def WinandFailure():
    playerInput = input("\nWould you like to player again? (Yes/No) ").lower()
    if playerInput == "yes":
        main()
    elif playerInput == "No":
        printEndingCopyright()
        quit()
        
def printEndingCopyright():
    print("\nYou went home after a long day of Fright Fest.")
    print("\nCopyright 2017 Daniel Addison Daniel.addison1@marist.edu")
    
def initGameData():                                   
    print("\n" + locations[3].description)
    locations[3].hasVisited = True
    
def showScene(player1):
    if locations[player1.location].hasVisited:
        print("\n You are at " + locations[player1.location].name)
    else:
        print("You are at " + locations[player1.location].description)
    
def processInput():
    global playerInput
    playerInput = input("\nplease enter a command: ").lower()
    
def updateGame(player1):
    global playerInput
    if player1.moves == 0:
        running = False
    #checks if the player has entered a direction 
    elif playerInput == "north" or playerInput == "south" or playerInput == "east" or playerInput == "west":
        moveTo(player1)
    elif playerInput == "help":
        print("\nThe commands to this game is: North, South, East, West, Help, Points, Map, look, search, take, drop, inventory, use, Converse, Backtrack, Pray, and Quit")       
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
    elif playerInput[0:4] == "take":
        # TODO before getting item name, first check that there is one (does the command have a second word?)
         item = playerInput.split()
         if len(item) == 2:
             player1.inventory.append(locations[player1.location].take(item[1]))
         else:
            print("there nothing there to take")       
    elif playerInput[0:4] == "drop":
        #gets the second word from the player input
         item = playerInput.split()
         if len(item) == 2:
             if item[1] in player1.inventory:
                 (locations[player1.location].drop(item[1]))
                 player1.inventory.remove(item[1])
         else:
            print("there nothing there to drop")
    elif playerInput[0:3] == "use":
        item = playerInput.split()
        if len(item) == 2:
            player1.use(item[1])
    elif playerInput == "inventory":
        player1.playerInventory()
    elif playerInput == "pray":
        player1.playerPray()
    elif playerInput == "converse":
        player1.playerConverse()
    elif playerInput == "backtrack":
        player1.backTrack()
        
    #this is the player map
    elif playerInput == "map":
        # TODO before printing the map, check if the map is in the player's inventory
        # if not, then do nothing, only print the map if it is
        if "map" in player1.inventory:
            print(" 7 - 6 - 8")
            print(" |   |")
            print(" 5 - 1 - 10")
            print(" |   |")
            print(" 2 - 0 - 11")
            print(" |   |")
            print(" 3 - 4 - 9")
            print("0: Ghostrider \n1: Xcelerator")
            print("2: Boomerang \n3: Funnelcake")
            print("4: Bullet \n5: Bathroom")
            print("6: Spaceshuttle \n7: Cottoncandy")
            print("8: beachLagoon \n9: PaperWorld")
            print("10: Admission office \n11: Lego Land")
        else:
            print("Go and find the map")
    else:
        print("Not a valid command")
def moveTo(player1):
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
    if player1.worldMatrix[player1.y][player1.x] != -1:
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
    elif player1.location == 1 and "camera" in player1.inventory:
        lose()
        return False
    elif player1.winOrLose == "win":
        win()
        return False
    return True

def win():
    print("You Won! You managed to bring the baby back.")
    
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
    WinandFailure()
    printEndingCopyright()
    
main()


