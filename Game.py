# Introduction to Programming
# Author: Daniel Addison
# Date: 10/20/2017

def printTitleIntro():
    print(" Knotts Scary Farm" )
    print("Get scared from your socks this october for a very special night on halloween")

printTitleIntro()

def printEndingCopyright():
    print("You went home")
    print("copyright 2017 Daniel Addison Daniel.addison1@marist.edu")

#new for project2

def gameloop():
    print ("Game Loop")

def changeLocation():
    print ("Change Location")    


#Locations
ghostrider = "A wooden rollercoaster, is the longet, tallest rollercoater made to scare kids as if they were in a pirateship"   
xcelerator = " This rocket looking rolercoaster, is the fasteest ride at Knotts going 0.82 mph in 2.3 sec"
boomerang = " Have you ever took a rollercoaster ride and back again twice going 0 to 55 in 3 sec"
funnelCakeStand = "Best funnel cake you would buy at an amusment park, you haven't had anything good till you tried it"
bullet = " Our new fastest RollerCoaster to date with VR technoligy for the experience"
bathroom = "your scared, but you go to the bathroom for a even bigger suprise"

#Booleans

VisitedGhostrider= False
VisitedXclerator= False
VisitedBoomerang= False
VisitedFunnelcakestand= False
VisitedBullet= False
VisitedBathroom= False

#Game
playerScore = 0
playerLocation = funnelCakeStand

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

printEndingCopyright()

