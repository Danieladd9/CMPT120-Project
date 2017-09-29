# Introduction to Programming
# Author: Daniel Addison
# Date: 10/20/2017



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
    VisitedBoomerang= True
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

    
printgameloop(playerScore,playerLocation)                    
printEndingCopyright()
   
    
