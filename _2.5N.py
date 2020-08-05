import math
from time import sleep

length = input("What's the length? ")
height = input("What's the height? ")
width = input("What's the width? ")
targetMass = input("What's the target mass? ")
blockMass = input("What's the block's mass? ")

crossSectionArea = float(length) * float(width)
volumeOfBlock = float(length) * float(height) * float(width)

densityOfBlock = float(blockMass) / float(volumeOfBlock)
massToRemove = float(blockMass) - float(targetMass)
volumeToRemove = float(massToRemove) / float(densityOfBlock)
lengthRequired = float(volumeToRemove) / float(crossSectionArea)

sleep(2.0)
print("The cross sectional area is",crossSectionArea)
sleep(1.0)
print("The volume of the block is",volumeOfBlock)
sleep(1.0)
print("Therefore the density would be",densityOfBlock)
sleep(1.0)
print("The amount of mass that's going to be removed is",massToRemove)
sleep(1.0)
print("This the volume that's going to be removed",volumeToRemove)
sleep(1.0)
print("Finally the length that's to be removed is",lengthRequired)
#while True:
#    goForIt = input("Type 'yes' if you want to know the new length, otherwise type 'reset' to restart the program")
#    if goForIt == yes:
#        newLength = float(length) - float(lengthRequired)
#        print("This will be the new length",newLength)
#    elif goForIt == reset:
#        continue
#    else:
#        print("-----   END   -----")
