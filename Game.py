# Introduction to Programming
# Author: Daniel Addison
# Date: 10/8/2017

ghostrider = "A wooden rollercoaster made to scare kids as if they were in a pirateship"   
accelerator = " The fasteest ride at Knotts"
boomerang = " Have you ever took a rollercoaster ride and back again twice"
funnelCakeStand = "Best funnel cake you would buy at an amusment park"
    
print(" Knotts Scary Farm" )
print("Get scared from your socks this october for a very special halloween")

playerScore = 0
playerLocation = funnelCakeStand

print("player current score is " + str(playerScore ))
print("player current Location is " + playerLocation)
#move to ghostrider
input("press enter to continue")

playerLocation = ghostrider
print("player current Location is " + playerLocation)

playerScore = playerScore + 5
print("player current score is " + str(playerScore ))
#move to boomerang
input("press enter to continue")

playerLocation = boomerang
print("player current Location is " + playerLocation)

playerScore = playerScore + 5
print("player current score is " + str(playerScore ))
#move to accelerator
input("press enter to continue")

playerLocation = accelerator
print("player current Location is " + playerLocation)

playerScore = playerScore + 5
print("player current score is " + str(playerScore ))
#move to funnelCakestand
input("press enter to continue")

playerLocation = funnelCakeStand
print("player current Location is " + playerLocation)

playerScore = playerScore + 5
print("player current score is " + str(playerScore ))

print("You went home")
print("copyright 2017 Daniel Addison Daniel.addison1@marist.edu")
