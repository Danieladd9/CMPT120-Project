# Introduction to Programming
# Author: Daniel Addison
# Date: 10/20/2017

playerName = input("what is your name?")
print ("hi"" "+ playerName +" " "welcome to Knotts Scary Farm")

def printTitleIntro():
    print("Knotts Scary Farm" )
    print("Get scared from your socks this october for a very special night on halloween")

printTitleIntro()

def printEndingCopyright():
    print("You went home after a long day of fright")
    print("copyright 2017 Daniel Addison Daniel.addison1@marist.edu")

#new for project2

def gameloop():
    print ("Game Loop")

def changeLocation():
    print ("Change Location")    


#Locations
ghostrider = "Ghostrider: A wooden rollercoaster, is the longet, tallest rollercoater made to scare kids as if they were in a pirateship"   
xcelerator = "Xcelerator: This rocket looking rolercoaster, is the fasteest ride at Knotts going 0.82 mph in 2.3 sec"
boomerang = "Boomarang: Have you ever took a rollercoaster ride and back again twice going 0 to 55 in 3 sec"
funnelCakeStand = "The Funnel Stand: The Best funnel cake you would buy at an amusment park, you haven't had anything good till you tried it"
bullet = "Bullet: Our new fastest RollerCoaster to date with VR technoligy for the experience"
bathroom = "Bathroom: we understand that your so scared, but wait till you go to the bathroom for a even bigger suprise"
shuttle = "Space Shuttle: Bus to carry you to the rides"
cottonCandy = "Cotton Candy: right by funnel cake, best cotton candy you ever had"

locationDiscription=["Ghostrider: A wooden rollercoaster, is the longet, tallest rollercoater made to scare kids as if they were in a pirateship",
                     "Xcelerator: This rocket looking rolercoaster, is the fasteest ride at Knotts going 0.82 mph in 2.3 sec",
                     "Boomarang: Have you ever took a rollercoaster ride and back again twice going 0 to 55 in 3 sec",
                     "The Funnel Stand: The Best funnel cake you would buy at an amusment park, you haven't had anything good till you tried it",
                     "Bullet: Our new fastest RollerCoaster to date with VR technoligy for the experience",
                     "Bathroom: we understand that your so scared, but wait till you go to the bathroom for a even bigger suprise",
                     "Space Shuttle: Bus to carry you to the rides",
                     "Cotton Candy: right by funnel cake, best cotton candy you ever had"]                                        
#newloc   
playerScore = 0 
playerLocation = funnelCakeStand

#Booleans

VisitedGhostrider= False
VisitedXclerator= False
VisitedBoomerang= False
VisitedFunnelCakeStand= False
VisitedBullet= False
VisitedBathroom= False


hasVisited=[False,False,False,False,False,False,False,False,False,False]
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
running = True
while running:
    print("player current score is " + str(playerScore ))
    print("player current Location is " + playerLocation)
    playerInput = input("plaese enter a command").lower()
    if playerInput == "north":
        print (playerName +" ""chose"" ""north")          
        if playerLocation == 0:
            if not hasVisited[1]:
                playerScore = playerScore + 5
                hasVisited[1] = True
            playerLocation = 1
        elif playerLocation == 1:
            print ("you going the wrong way")
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
            if not VisitedBathroom:
                playerScore = playerScore + 5
                VisitedBathroom = True
            playerLocation = bathroom
        elif playerLocation == bathroom:
            print ("you going the wrong way")
            
    elif playerInput == "south":
        print (playerName +" ""chose"" ""south")
        if playerLocation == xcelerator:
            if not VisitedGhostrider:
                playerScore = playerScore + 5
                VisitedGhostrider = True
            playerLocation = ghostrider
        elif playerLocation == ghostrider:
            if not VisitedBullet:
                playerScore = playerScore + 5
                VisitedBullet = True
            playerLocation = bullet
        elif playerLocation == bullet:
            print ("you going the wrong way")
        elif playerLocation == bathroom:
            if not hasVisited[2]:
                playerScore = playerScore + 5
                hasVisited[2] = True
            playerLocation = 2
        elif playerLocation == 2:
            if not VisitedFunnelCakeStand:
                playerScore = playerScore + 5
                VisitedFunnelCakeStand = True
            playerLocation = funnelCakeStand
        elif playerLocation == funnelCakeStand:
            print ("you going the wrong way")
            
    elif playerInput == "east":
        print (playerName +" ""chose"" ""east")
        if playerLocation == bathroom:
            if not VisitedXclerator:
                playerScore = playerScore + 5
                VisitedXcelerator = True
            playerLocation = xcelerator
        elif playerLocation == xcelerator:
            print ("you going the wrong way")
        elif playerLocation == 2:
            if not VisitedGhostrider:
                playerScore = playerScore + 5
                VisitedGhostrider = True
            playerLocation = ghostrider
        elif playerLocation == ghostrider:
            print ("you going the wrong way")
        elif playerLocation == funnelCakeStand:
            if not VisitedBullet:
                playerScore = playerScore + 5
                VisitedBullet = True
            playerLocation = bullet
        elif playerLocation == bullet:
            print ("you going the wrong way")

    elif playerInput == "west":
        print (playerName +" ""chose"" ""west")
        if playerLocation == xcelerator:
            if not VisitedBathroom:
                playerScore = playerScore + 5
                VisitedBathroom = True
            playerLocation = bathroom
        elif playerLocation == bathroom:
            print ("you going the wrong way")
        elif playerLocation == ghostrider:
            if not hasVisited[2]:
                playerScore = playerScore + 5
                hasVisited[2] = True
            playerLocation = 2
        elif playerLocation == 2:
            print ("you going the wrong way")
        elif playerLocation == bullet:
            if not VisitedFunnelCakeStand:
                playerScore = playerScore + 5
                VisitedFunnelCakeStand = True
            playerLocation = funnelCakeStand
        elif playerLocation == funnelCakeStand:
            print ("you going the wrong way")
        
            
    elif playerInput == "help":
        print ("The commands to this game is: North, South, East, West, Help, and Quit")
    elif playerInput == "quit":
        print ("Goodbye,Thank You for playing")
        running = False
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
def printLocScore():
    print (playerScore+" " + playerLocation)
def printgameloop(playerScore,playerLocation):
    print ("gameloop")
#Game
    print("player current score is " + str(playerScore ))
    print("player current Location is " + playerLocation)
    
#move to ghostrider
    input("press enter to continue")

    playerLocation = ghostrider
    VisitedGhostrider= True
    print("player current Location is " + playerLocation)

    playerScore = playerScore + 5
    print("player current score is " + str(playerScore ))

#move to boomerang
    input("press enter to continue")

    playerLocation = boomerang
    hasVisited[2]= True
    print("player current Location is " + playerLocation)

    playerScore = playerScore + 5
    print("player current score is " + str(playerScore ))
#move to xcelerator
    input("press enter to continue")

    playerLocation = xcelerator
    VisitedXclerator= True

    print("player current Location is " + playerLocation)

    playerScore = playerScore + 5
    print("player current score is " + str(playerScore ))
#move to funnelCakestand
    input("press enter to continue")

    playerLocation = funnelCakeStand
    VistedFunnelcakestand = True
    print("player current Location is " + playerLocation)

    playerScore = playerScore + 5
    print("player current score is " + str(playerScore ))
#move to Bullet
    input("press enter to continue")

    playerLocation = bullet
    VistedBullet = True
    print("player current Location is " + playerLocation)

    playerScore = playerScore + 5
    print("player current score is " + str(playerScore ))
#move to Bathroom
    input("press enter to continue")

    playerLocation = bathroom
    VistedBathroom = True
    print("player current Location is " + playerLocation)

    playerScore = playerScore + 5
    print("player current score is " + str(playerScore ))

    
                    
printEndingCopyright()
   
    
