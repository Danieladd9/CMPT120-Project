# Introduction to Programming
# Author: Daniel Addison
# Date: 10/25/2017

playerName = input("What is your name? ")
print ("Hi " + playerName + " Welcome to Knott’s Scary Farm")

def printTitleIntro():
    print("Knotts Scary Farm")
    print("Get scared from your socks this October for a very special night on Halloween.")

printTitleIntro()

def printEndingCopyright():
    print("You went home after a long day of Fright Fest.")
    print("Copyright 2017 Daniel Addison Daniel.addison1@marist.edu")

def gameloop():
    print ("Game Loop")

def changeLocation():
    print ("Change Location")  

#Locations
ghostrider = "Ghostrider: A wooden rollercoaster, is the longest, tallest roller-coaster made to scare kids as if they were in a pirate ship"   
xcelerator = "Xcelerator: This rocket looking roller-coaster, is the fastest ride at Knott’s going 0.82 mph in 2.3 sec"
boomerang = "Boomerang: Have you ever took a rollercoaster ride and back again twice going 0 to 55 in 3 sec"
funnelCakeStand = "The Funnel Stand: The Best funnel cake you would buy at an amusement park, you haven't had anything good till you tried it"
bullet = "Bullet: Our new fastest Roller-coaster to date with VR technology for the experience"
bathroom = "Bathroom: we understand that your so scared, but wait till you go to the bathroom for an even bigger surprise"
shuttle = "Space Shuttle: Bus to carry you to the rides"
cottonCandy = "Cotton Candy: right by funnel cake, best cotton candy you ever had"

#new for project3  
#this array holds the description of the players location
locationDiscription=["Ghostrider: A wooden rollercoaster, is the longest, \
tallest roller-coaster made to scare kids as if they were in a pirate ship",
                     "Xcelerator: This rocket looking roller-coaster, is the \
fastest ride at Knott’s going 0.82 mph in 2.3 sec",
                     "Boomerang: Have you ever took a rollercoaster ride and back again twice going 0 to 55 in 3 sec",
                     "The Funnel Stand: The Best funnel cake you would buy at an amusement park, \
you haven't had anything good till you tried it",
                     "Bullet: Our new fastest Roller-coaster to date with VR technology for the experience",
                     "Bathroom: we understand that your so scared,\
but wait till you go to the bathroom for an even bigger surprise",
                     "Space Shuttle: Bus to carry you to the rides",
                     "Cotton Candy: right by funnel cake, best cotton candy you ever had"]                                        
#newloc   
playerScore = 5 
playerLocation = 3

#Booleans
#this is how we know where the player has been
hasVisited=[False,False,False,True,False,False,False,False,False,False]

#Time Limit
playerMoves = 40
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
running = True
while running:
    #this check if the player has any moves left
    if playerMoves == 0:
        running = False
    print("player current Location is " + locationDiscription[playerLocation])
    playerInput = input("please enter a command: ").lower()
    if playerInput == "north":
        print(playerName + " chose north")
        playerMoves -= 1
        if playerLocation == 0:
            # move these fours lines into a new moveTo function
            # where the parameter to the function is the location index
            # then here just call that function with argument 1
            #moveTo(1)
            if not hasVisited[1]:
                playerScore = playerScore + 5
                hasVisited[1] = True
            playerLocation = 1
        elif playerLocation == 1:
            if not hasVisited[6]:
                playerScore = playerScore + 5
                hasVisited[6]= True
            playerLocation = 6
        elif playerLocation == 4:
            if not hasVisited[0]:
                playerScore = playerScore + 5
                hasVisited[0]= True
            playerLocation = 0
        elif playerLocation == 3:
            if not hasVisited[2]:
                playerScore = playerScore + 5
                hasVisited[2] = True
            playerLocation = 2
        elif playerLocation == 2:
            if not hasVisited[5]:
                playerScore = playerScore + 5
                hasVisited[5] = True
            playerLocation = 5
        elif playerLocation == 5:
            if not hasVisited[7]:
                playerScore = playerScore + 5
                hasVisited[7] = True
            playerLocation = 7
        else:
            print("You cannot go that way")
            
    elif playerInput == "south":
        print(playerName + " chose south")
        playerMoves -= 1
        if playerLocation == 1:
            if not hasVisited[0]:
                playerScore = playerScore + 5
                hasVisited[0] = True
            playerLocation = 0
        elif playerLocation == 0:
            if not hasVisited[4]:
                playerScore = playerScore + 5
                hasVisited[4] = True
            playerLocation = 4
        elif playerLocation == 5:
            if not hasVisited[2]:
                playerScore = playerScore + 5
                hasVisited[2] = True
            playerLocation = 2
        elif playerLocation == 2:
            if not hasVisited[3]:
                playerScore = playerScore + 5
                hasVisited[3] = True
            playerLocation = 3
        elif playerLocation == 6:
            if not hasVisited[1]:
                playerScore = playerScore + 5
                hasVisited[1]= True
            playerLocation = 1
        elif playerLocation == 7:
            if not hasVisited[5]:
                playerScore = playerScore + 5
                hasVisited[5] = True
            playerLocation = 5
        else:
            print("You cannot go that way")
            
    elif playerInput == "east":
        print(playerName + " chose east")
        playerMoves -= 1
        if playerLocation == 5:
            if not hasVisited[1]:
                playerScore = playerScore + 5
                hasVisited[1] = True
            playerLocation = 1
        elif playerLocation == 2:
            if not hasVisited[0]:
                playerScore = playerScore + 5
                hasVisited[0] = True
            playerLocation = 0
        elif playerLocation == 3:
            if not hasVisited[4]:
                playerScore = playerScore + 5
                hasVisited[4] = True
            playerLocation = 4
        elif playerLocation == 7:
            if not hasVisited[6]:
                playerScore = playerScore + 5
                hasVisited[6] = True
            playerLocation = 6
        else:
            print("You cannot go that way")

    elif playerInput == "west":
        print(playerName + " chose west")
        playerMoves -= 1
        if playerLocation == 1:
            if not hasVisited[5]:
                playerScore = playerScore + 5
                hasVisited[5] = True
            playerLocation = 5
        elif playerLocation == 0:
            if not hasVisited[2]:
                playerScore = playerScore + 5
                hasVisited[2] = True
            playerLocation = 2
        elif playerLocation == 4:
            if not hasVisited[3]:
                playerScore = playerScore + 5
                hasVisited[3] = True
            playerLocation = 3
        elif playerLocation == 6:
            if not hasVisited[7]:
                playerScore = playerScore + 5
                hasVisited[7] = True
            playerLocation = 7
        else:
            print("You cannot go that way")
        
    elif playerInput == "help":
        print("The commands to this game is: North, South, East, West, Help, Points, Map, and Quit")
        playerMoves -= 1
    elif playerInput == "quit":
        print("Goodbye, Thank You for playing")
        running = False
    elif playerInput == "points":
        print("Player current score is " + str(playerScore))
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
        
printEndingCopyright()
