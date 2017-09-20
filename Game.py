# Introduction to Programming
# Author: Daniel Addison
# Date: 10/14/2017

ghostrider = "A wooden rollercoaster, is the longet, tallest rollercoater made to scare kids as if they were in a pirateship"   

VisitedGhostrider= False

xcelerator = " This rocket looking rolercoaster, is the fasteest ride at Knotts going 0.82 mph in 2.3 sec"

VisitedXclerator= False

boomerang = " Have you ever took a rollercoaster ride and back again twice going 0 to 55 in 3 sec"

VisitedBoomerang= False

funnelCakeStand = "Best funnel cake you would buy at an amusment park, you haven't had anything good till you tried it"

VisitedFunnelcakestand= False

Bullet = " Our new fastest RollerCoaster to date with VR technoligy for the experience"

VisitedBullet= False

Bathroom = "your scared, but you go to the bathroom for a even bigger suprise"

isitedBathroom= False

print(" Knotts Scary Farm" )
print("Get scared from your socks this october for a very special night on halloween")

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

print("You went home")
print("copyright 2017 Daniel Addison Daniel.addison1@marist.edu")
