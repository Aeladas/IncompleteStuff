#Orthagonals program.
#Import necessary modules
from time import sleep
import math

print("Please input all the forces and angles displayed in the diagram.")
sleep(2)
print("--------------------")

#Prompt the user for an input about what's their forces and angles.
forceOne = int(input("What's the first force? -> "))
sleep(3)
forceTwo = int(input("What's the second force? -> "))
sleep(3)
angleOne = int(input("What's the first angle? -> "))
sleep(3)
angleTwo = int(input("What's the second angle? -> "))

#Manipulation of the user's inputs.
vertical1 = float(math.sin(angleOne)) * float(forceOne)
horizontal1 = float(math.cos(angleOne)) * float(forceOne)
vertical2 = float(math.sin(angleTwo)) * float(forceTwo)
horizontal2 = float(math.cos(angleTwo)) * float(forceTwo)
totalHorizontal = float(horizontal1) + float(horizontal2)
totalVertical = float(vertical1) + float(vertical2)
longestSideSqd = float(float(totalHorizontal) ** float(2)) + float(float(totalVertical) ** float(2))
longestSide = math.sqrt(longestSideSqd)
angleRad = math.atan(float(totalVertical) / float(longestSide))
angleDeg = math.degrees(angleRad)

#Output the manipulated values...
print("---------------------")
sleep(2)
print("The length of the hypotenuse is:",longestSide)
sleep(2)
print("The overall angle is:",angleDeg)