import tkinter
import math
import random
import turtle
from time import sleep

"""
Constants
The programs will use these constants to validate the user's inputs.
"""

_pi = float(3.14159265359)
_unit_1_choices = []
unit2Choices = []
_unit_3_choices = ["centroid", "friction", "force", "kinetic", "momentum", "potential", "young's"]
unit4Choices = ["energy", "Generators", "Motors", "Ohms", "Phasor Diagrams", "Power", "RC"]
forceChoices = ["acceleration","force","mass"]
youngsChoices = ["strain","stress", "youngs"]
strainChoices = ["change","length", "strain"]
stressChoices = ["area", "force", "stress"]
potentialChoices = ["gravity", "height", "mass", "potential"]
kineticsChoices = ["energy", "mass", "velocity"]
momentumChoices = ["mass", "momentum", "velocity"]
frictionChoices = ["coefficient", "friction", "normal"]
centroidChoices = ["triangleSquare", "triangleSemi-circle"]
ohmsChoices = ["current", "resistance", "voltage"]
phaseChoices = ["Xl", "Xc"]
totalRcChoices = ["capacitance","resistance"]
spChoices = ["parallel", "series"]
powerChoices = ["current", "power", "resistance"]
energyChoices = ["energy", "power", "time"]
capArray = []
resistArray = []

def unit_1():
def unit_2():
def unit_3():
    print(">>>YOU'VE SELECTED UNIT 3 SUPPORT<<<")
    sleep(2)
    print("Type either of the following exactly how they appear on screen otherwise the computer will generate complex errors\n----------\ncentroid\nfriction\nforce\nkinetics\nmomentum\npotential\nyoung's\n----------")
    sleep(3)
    print("Type your answer into the entry box on the window with the unit selection buttons on.\nMake sure to clear it using 'backspace' every time you go to use it.")
    interfaceEntry = userEntry.get()
    if interfaceEntry == _unit_3_choices[0]:
        print("----------")
        sleep(1)
        print("This function will help calculate the centre of a centroid...")
        sleep(1)
        print("Let's begin by drawing a diagram to help us visually understand what is to happen.")
        centroidInput = str(input(
            "What's the shapes involved i.e. triangle and semi-circles.\nType either 'triangleSquare' or 'triangleSemi-circle' -> "))
        if centroidInput == centroidChoices[0]: #04/12/2000
            #        thread.start_new_thread
            turtle.pensize(2)
            turtle.speed(1)
            turtle.color("blue")
            turtle.penup()
            turtle.goto(-100, 0)

            turtle.pendown()
            turtle.forward(150)
            turtle.left(90)
            turtle.forward(150)
            turtle.left(135)
            turtle.forward(212)
            turtle.left(135)
            turtle.forward(300)
            turtle.left(90)
            turtle.forward(150)
            turtle.left(90)
            turtle.forward(150)
            turtle.penup()
            turtle.goto(-100, 0)
            turtle.right(180)

            print("----------")
            print(
                "This diagram should help identify how to solve the centre...\nYou know blue triangle that was moving, try and consider that as the origin point.")
            print("----------")
            sleep(2)
            print("Step 1 is to find all the variables such as the triangle length and areas...")
            sleep(1)

            totalLength = float(input("What's the total length? -> "))
            totalHeight = float(input("What's the total height? -> "))
            squareLength = float(input("What's the length of the square? -> "))
            triangleLength = float(totalLength) - float(squareLength)
            print("The length of the triangle is", '{:3f}'.format(triangleLength))
            triangleAreaM = float(triangleLength) * float(totalHeight)
            triangleArea = float(triangleAreaM) / float(2)

            sleep(1)
            print("The triangle area is", '{:3f}'.format(triangleArea))
            squareArea = float(squareLength) * float(totalHeight)
            print("The square area is", '{:3f}'.format(squareArea))
            totalArea = float(triangleArea) + float(squareArea)
            print("The total area is", '{:3f}'.format(totalArea))
            sleep(2)

            print("----------")
            sleep(1)
            print("Step 2 is to write an equation...")  #21/11/1969
            sleep(1)
            print(
                "The equation in your case would be (2/3 of triangle length) / (1/3 of the triangle height) x triangle area then this is added to half the square's x and y values being multiplied by the square's area.")
            sleep(2)
            print("Now try write out the equation from the values you've given the program.")
            sleep(5)
            print(
                "To find the x co-ordinate we just do the top row of the equation so ONLY the X values!\nI'm going to do this while you do it too.\nRemember the x value for the square is the triangle length added to half the length of the square.\nThe program will slowly count 90 seconds giving you enough time to calculate the x y co-ords")
            part1X = float(float(triangleLength) / float(3) * float(2)) * float(triangleArea) + float(
                float(float(squareLength) / float(2)) * float(squareArea))
            centroidX = float(part1X) / float(totalArea)
            part2Y = float(float(totalHeight) / float(3)) * float(triangleArea) + float(
                float(float(totalHeight) / float(2) * float(totalArea)))
            centroidY = float(part2Y) / float(totalArea)
            sleep(90)
            print("The centroid is", '{:3f}'.format(centroidX, centroidY))
        elif centroidInput == centroidChoices[1]:
            turtle.pensize(2)
            turtle.speed(3)
            turtle.color("#009900")

            def curveMove():
                for i in range(50):
                    turtle.forward(6.594)
                    turtle.right(2.5)

            # move the turtle into the correct position
            turtle.penup()
            turtle.goto(-350, 0)

            # Start drawing the triangle section...
            turtle.pendown()
            turtle.forward(150)
            turtle.left(90)
            turtle.forward(150)
            turtle.left(135)
            turtle.forward(212)
            turtle.left(135)
            turtle.penup()

            # Draw the semi circle section...
            turtle.goto(-50, 300)
            turtle.pendown()
            curveMove()

            # Write some Text!
            turtle.penup()
            turtle.goto(-350, -50)
            turtle.color("#000000")
            turtle.pendown()    #27/07/1971
            turtle.write("The turtle will not go to the position that will best represent the origin.",
                         font=("Helvetica", 16))
            turtle.penup()
            turtle.goto(-350, -100)
            turtle.pendown()
            turtle.write("The formula to find the centroid of a semi-circle is 4 * Radius / 3 * _pi .",
                         font=("Helvetica", 16))

            print("Let's go through this in stages.\nStep 1 - find all the necessary variables.")
            triangleSECLength = int(input("The length of the triangle? -> "))
            triangleSECHeight = int(input("The height of the triangle? -> "))
            circleSECRadius = int(input("What's the radius of the circle? -> "))
            twoThirds = float(float(triangleSECLength) / float(3) * float(2))
            oneThirds = float(triangleSECHeight) / float(3)
            triangleSECArea = float(float(triangleSECLength) * float(triangleSECHeight)) / float(2)
            circleSECArea = float(float(_pie) * float(circleSECRadius)) / float(2)
            circleX = float(float(4) * float(circleSECRadius)) / float(float(3) * float(_pie))
            sleep(2)
            print("     ")
            sleep(1)
            print(
                "Step 2 - Now we create the equation.\nTriangleX / TriangleY x Triangle Area + Semi-circleX[The formula is 4*radius / 3*_pi] / semi-circleY(This is just the radius) x semi-circle area . ")
            print("To avoid errors the program won't be creating an equation so you'll have to write one yourself.")
            sleep(2)
            print("     ")
            sleep(1)
            print(
                "Step 3 - Next your going to solve your equation one row at a time;\nTriangleX x triangle area + semi-circleX x  semi-circle area .")
            SECentroidX = float(float(twoThirds) * float(triangleSECArea)) + float(
                float(circleX) * float(circleSECArea))
            print("     ")
            sleep(1)
            print("Step 4 - Complete the bottom row;\nTriangleY x triangle area + radius x semi-circle area . ")
            SECentroidY = float(float(oneThirds) * float(triangleSECArea)) + float(
                float(circleSECRadius) * float(circleSECArea))
            print("     ")
            sleep(1)
            print("Step 5 - The final step is to clearly show the examiner your answers like so...")
            print("     ")
            print(SECentroidX)
            print("     ")
            print(SECentroidY)
    elif interfaceEntry == _unit_3_choices[1]:
        print("----------")
        sleep(1)
        print("So to you are seeking help on friction force I see? Well I'm just the right function for the job. In fact I'm the only function capable!")
        sleep(1)
        print("Type either 'coefficient', 'friction' or 'normal'.")
        frictionInput = str(input("Your choice is? -> "))
        if frictionInput == frictionChoices[0]: #09/01/2006
            print("----------")
            sleep(1)
            print("The equation to find out the co-efficient is:\nu = Ff / Fn.")
            sleep(1)
            print("Attempt to calculate this beforehand.")
            sleep(10)
            frictionU = float(input("The friction force? -> "))
            normalU = float(input("What's the normal force -> "))
            coefficientU = float(frictionU) / float(normalU)
            sleep(1)
            print("The coefficient is:"'{:3f}'.format(coefficientU))
        elif frictionInput == frictionChoices[1]:
            print("----------")
            sleep(1)
            print("Use the unchanged equation.\nFf = u * Fn")
            print("Attempt this before the computer completes it for you.")
            sleep(10)
            uF = float(input("What's the coefficient? -> "))
            normalF = float(input("What's the value of mg? -> "))
            frictionF = float(uF) * float(normalF)
            sleep(1)
            print("The friction force would be:"'{:3f}'.format(frictionF))
        elif frictionInput == frictionChoices[2]:
            print("----------")
            sleep(1)
            print("Use the rearranged equation Fn = Ff / u")
            frictionN = float(input("What's the friction force? -> "))
            uN = float(input("What's the coefficient? -> "))
            normalN = float(frictionN) / float(uN)
            sleep(1)
            print("The normal force is:"'{:3f}'.format(normalN))
        else:
            print("----------")
            sleep(1)
            print("You've inputted an invalid response, so you'll have to try again.")
    elif interfaceEntry == _unit_3_choices[2]:
        print("----------")
        sleep(1)
        print("This function will help you calculate Force, mass and acceleration.")
        sleep(1)
        print("Type either 'acceleration', 'force' or 'mass' to begin solving the desired equation.")
        sleep(1)
        print("------")
        forceInput = input("What's your choice? -> ")
        if forceInput == forceChoices[0]:
            print("So you want to calculate acceleration.\nThe equation is - Acceleration = Force / Mass")
            sleep(1)
            forceA = float(input("What's the force in newtons? -> "))
            massA = float(input("What's the mass of the object in kg -> "))
            accelerationA = float(forceA) / float(massA)    #07/08/2008
            print("The acceleration of the object in ms-2 is", '{:3f}'.format(accelerationA))
        elif forceInput == forceChoices[1]:
            print("To calculate the force acting upon an object we use the equation;\nForce = Mass * Acceleration")
            sleep(1)
            massF = float(input("What's the mass of the object(Kg)? -> "))
            accelerationF = float(input("What's the acceleration of the object(ms^-2) -> "))
            forceF = float(massF) * float(accelerationF)
            sleep(1)
            print("The force in netwons is:", '{:3f}'.format(forceF))
        elif forceInput == forceChoices[2]:
            print(
                "In order to calculate mass you need to know the force as well as the acceleration.\nThe equation is: Mass = Force / Acceleration")
            forceM = float(input("What's the force(N)? -> "))
            accelerationM = float(input("What's the acceleration(ms^-2)? -> "))
            massM = float(forceM) / float(accelerationM)
            sleep(1)
            print("The mass of the object in kilograms is:", '{:3f}'.format(massM))
    elif interfaceEntry == _unit_3_choices[3]:
        print("----------")
        sleep(1)
        print("This function will help teach you how to effectively use the kinetic energy formula:\nKE = ½ mv^2    ;)")
        sleep(1)
        print(
            "To get started type one of the following, if you make a mistake hit the reset button on the RESETS window.\nType either 'energy', 'mass' or 'velocity'.")
        kineticsInput = str(input("Which are you wanting help doing? -> "))
        if kineticsInput == kineticsChoices[0]:
            print("----------")
            sleep(1)
            print("The equation is: KE = ½ x m x v^2")
            massK = float(input("What's the mass? -> "))
            velocityK = float(input("What's the velocity? -> "))
            velocityKE = float(velocityK) ** 2
            KE = float(0.5) * float(massK) * float(velocityKE)
            sleep(1)
            print("The kinetic energy in joules is:", '{:3f}'.format(KE))
            KEKJ = float(KE) / float(1000)
            print("The kinetic energy in kilojoules is:", '{:3f}'.format(KEKJ))
        elif kineticsInput == kineticsChoices[1]:
            print("----------")
            sleep(1)
            print("The equation is m = KE / ½ x v^2")
            KEM = float(input("What's the total kinetic energy? -> "))
            half = float(0.5)
            velocityM = float(input("What's the velocity? -> "))
            V2M = float(velocityM) ** 2
            massKEM = float(KEM) / float(float(half) * float(V2M))
            sleep(1)
            print("The mass of the object is:", '{:3f}'.format(massKEM))
        elif kineticsInput == kineticsChoices[2]:
            print("----------") #10/05/2018
            sleep(1)
            print("The equation is v^2 = KE / ½ x m")
            KEV = float(input("Total kinetic energy? -> "))
            halfV = float(0.5)
            massV = float(input("What's the mass? -> "))
            v2V = float(KEV) / float(v2)
            v2 = float(halfV) * float(massV)
            sleep(1)
            print("The velocity squared is:", '{:3f}'.format(v2))
        else:
            print("You've entered in a invalid expression...")
            sleep(1)
    elif interfaceEntry == _unit_3_choices[4]:
        print("----------")
        sleep(1)
        print("The main equation is p = m * v.")
        sleep(2)
        print("Type either 'mass', 'momentum' or 'velocity' to begin...")
        momentumInput = input("What's your choice? -> ")
        if momentumInput == momentumChoices[0]:
            print("----------")
            sleep(1)
            print("To calculate mass the re-arrangement would be as follows:\nMass = Momentum / Velocity.")
            momentumM = float(input("Momentum of the object? -> "))
            velocityM = float(input("Velocity of the object? -> "))
            massMomentum = float(momentumM) / float(velocityM)
            sleep(1)
            print("The mass of the object is:", '{:3f}'.format(massMomentum))
        elif momentumInput == momentumChoices[1]:
            print("----------")
            sleep(1)
            print("In order to calculate momentum use the main equation!")
            massMom = float(input("What's the mass? -> "))
            velocityMom = float(input("What's the velocity of the object? -> "))
            momentumMom = float(massMom) * float(velocityMom)
            sleep(2)
            print("The momentum of object A is:", '{:3f}'.format(momentumMom))
        elif momentumInput == momentumChoices[2]:
            print("----------")
            sleep(1)
            print("When calculating velocity use\nVelocity = Momentum / Mass!")
            momentumVel = float(input("What's the momentum? -> "))
            massVel = float(input("What's the mass? -> "))
            velocityVel = float(massMom) * float(velocityMom)
            sleep(2)
            print("The velocity of object A is:", '{:3f}'.format(velocityVel))
        else:
            print("----------")
            sleep(1)
            print("Next time input a valid expression please...")   #05/09/2015
            sleep(1)
    elif interfaceEntry == _unit_3_choices[5]:
        print("----------")
        sleep(1)
        print("Potential Energy is calculated using mass, gravity and height.")
        sleep(1)
        print("Type either 'gravity', 'height', 'mass', or 'potential' to get started.")
        potentialInput = str(input("What's your choice? -> "))
        if potentialInput == potentialChoices[0]:
            print("----------")
            sleep(1)
            print("The equation is g = PE /m x h ")
            PEG = float(input("Total potential energy? -> "))
            massG = float(input("What's the total mass? -> "))
            heightG = float(input("What's the height of the object? -> "))
            mhG = float(massG) * float(heightG)
            gravityG = float(PEG) / float(mhG)
            sleep(1)
            print("The gravitation force acting upon the object is:", '{:3f}'.format(gravityG))
        elif potentialInput == potentialChoices[1]:
            print("----------")
            sleep(1)
            print("The equation would be h = PE / m x g ")
            PEH = float(input("Total potential energy? -> "))
            massH = float(input("Total mass? -> "))
            gravityH = float(input("Total graviational pull? -> "))
            mgH = float(massH) * float(gravityH)
            heightH = float(PEH) / float(mgH)
            sleep(1)
            print("The height in metres at which potential energy was reached at was:", '{:3f}'.format(heightH))
        elif potentialInput == potentialChoices[2]:
            print("----------")
            sleep(1)
            print("The equation is m = PE / g x h ")
            PEM = float(input("Total potential energy? -> "))
            gravityM = float(input("Total gravitational force? -> "))
            heightM = float(input("Maximum height reached? -> "))
            ghM = float(gravityM) * float(heightM)
            massM = float(PEM) / float(ghM)
            sleep(1)
            print("The mass of the object would be:", '{:3f}'.format(massM))
        elif potentialInput == potentialChoices[3]:
            print("----------")
            sleep(1)
            print("The equation is PE = m x g x h ")
            massPE = float(input("What's the total mass? -> "))
            gravityPE = float(input("What's the total gravitational force? -> "))
            heightPE = float(input("What's the maximum height? -> "))
            PEJ = float(massPE) * float(gravityPE) * float(heightPE)
            sleep(1)    #13/12/2017
            print("The potential energy in joules is:", PEJ)
            PEKJ = float(PE) / float(1000)
            sleep(1)
            print("The potential energy in kilojoules is:", PEKJ)
        else:
            print("Please retry the function again as you entered in an invalid expression. :)")
            sleep(1)
    elif interfaceEntry == _unit_3_choices[6]:
        print("With this function you can not only calculate the Young's modulus but also stress and strain!")
        sleep(2)
        print("Please type either 'strain', 'stress' or 'youngs' to get started...")
        sleep(1)
        print("----------")
        youngsInput = input("What's your choice? -> ")
        if youngsInput == youngsChoices[0]:
            print("----------")
            sleep(1)
            print("So if you want to calculate strain the equation would be;\nΔL / Length - Lets get practising one...")
            sleep(1)
            print("**The change in length may be specified in the question**")
            sleep(1)
            print("**Try calculate it on your own first and use the program to double check your answer**")
            sleep(1)
            print("Type either 'changeInLength', 'length' or 'strain' to get started.")
            print(
                "**Take into account that both inputs and outputs will not be converted so insert values in mm when it asks for length**")
            strainChoice = input("What's your choice? -> ")
            if strainChoice == strainChoices[0]:
                print("----------")
                print("To calculate the change in length we use the following equation:\nΔL = Strain * Length")
                strainΔL = float(input("What's the value of strain? -> "))
                lengthΔL = float(input("What was the original length? -> "))
                ΔLSC = float(strainΔL) * float(lengthΔL)
                sleep(2)
                print("The change in length would be:"'{:3f}'.format(ΔLSC))
            elif strainChoice == strainChoices[1]:
                print("----------")
                sleep(1)
                print("To calculate length we would use:\nLength = ΔL / Strain")
                sleep(1)
                ΔLength = float(input("What's the change in length? -> "))
                strainL = float(input("What's the value of strain? -> "))
                lengthL = float(ΔLength) / float(strainL)
                sleep(1)
                print("The original length was:", '{:3f}'.format(lengthL))
            elif strainChoice == strainChoices[2]:
                print("----------")
                sleep(1)
                print("To calculate strain the equation is:\nΔL / Length")
                sleep(1)
                ΔL = float(input("What's the change in length? -> "))
                length = float(input("What was the original length? -> "))
                strain = float(ΔL) / float(length)
                sleep(1)
                print(
                    "If you got the your answer equal to this try practising a few more just like it then you'll be able to do these in a snap :)\nMy answer was:",
                    '{.3f}'.format(strain))
            else:
                print("----------")
                print("Please enter a valid input next time.")

        elif youngsInput == youngsChoices[1]:
            print("----------")
            sleep(1)
            print("The equation to calculate stress is:\nStress = Force / Area.")
            sleep(1)
            print("Please type either 'area', 'force', or 'stress' to get started.")
            stressInput = str(input("What's is your response? -> "))
            if stressInput == stressChoices[0]:
                print("You want to calculate area? Well the equation is as follows:\nArea = Force * Stress")
                sleep(1)
                forceAR = float(input("The force in action is -> "))
                stressA = float(input("The stress in action is -> "))
                areaA = float(forceAR) / float(stressA)
                print("The total area is:", '{:3f}'.format(areaA))
            elif stressInput == stressChoices[1]:
                print("Force is your choice? The equation would be:\nForce = Area * Stress")
                sleep(1)
                areaF = int(input("What's the total area? -> "))
                stressF = int(input("What's the stress? -> "))
                forceF = float(stressA) * float(areaA)
                sleep(1)
                print("The force in newtons is", '{:3f}'.format(forceF))
            elif stressInput == stressChoices[2]:
                print("Stress is quite the easy one to complete to your full extentive engineering abilities.")
                sleep(1)
                areaS = float(input("What's the total area? -> "))
                forceS = float(input("What's the force acting upon the object? -> "))
            else:
                print("----------")
                sleep(1)
                print("Please enter a valid term as provided above.")
                stressRedo()
        elif youngsInput == youngsChoices[2]:
            print("----------")
            sleep(1)
            print("The equation for young's modulus is ε = σ / e")
            sleep(1)
            print("As you've not asked to complete the other functions I'll ask you to fill in all inputs that will be displayed.")
            print("----------") #/09/2019
            areaY = float(input("What's the total area? -> "))
            forceY = float(input("What's the total force? -> "))
            ΔL = float(input("What's the change in length? -> "))
            lengthY = float(input("What's the original length -> "))
            σ = float(forceY) / float(areaY)
            e = float(ΔL) / float(lengthY)
            ε = float(σ) / float(e)
            sleep(1)
            print("The young's modulus is", '{:3f}'.format(ε))
        else:
            print("Please enter a valid term.")
    else:
        print(">>>Error 1 - input was invalid, didn't meet requirements<<<")
        sleep(2)
        print("----------------------------------------")

def unit_4():
    print(">>>YOU'VE SELECTED UNIT 4 SUPPORT<<<")
    sleep(2)
    print("Type your answer into the entry box on the window with the unit selection buttons on.\nMake sure to clear it using 'backspace' every time you go to use it.")
    sleep(1)
    print("Choices include:\nEnergy\nGenerators\nMotors\nOhms\nPhasor Diagrams\nPower\nRC")
    decision = interfaceEntry.get()
    if decision == unit4Choices[0]:
        print("This is the energy calculation function\nType either 'energy', 'power' or 'time' to get started")
        sleep(1)
        energy_choice = input("Your choice is -> ")

        if energy_choice == energy[0]:
            print("The equation is Energy = Power * Time")
            sleep(1)
            powerE = input("The power is -> ")
            timeE = input("The time in seconds is -> ")
            energyE = float(powerE) * float(timeE)
            print("The amount of energy being utilised is:", energyE)
        elif energy_choice == energy[1]:
            print("The re-arranged equation is Power = Energy / Time")
            sleep(1)
            energyP = input("How much energy is being used? ->")
            timeP = input("How long was the device used for?(seconds!) -> ")
            powerP = float(energyP) / float(timeP)
            print("The amount of power being used is:", powerP)
        elif energy_choice == energy[2]:
            print("The equation we will use is Time = Energy / Power")
            sleep(1)
            EnergyT = input("The energy being used is -> ")
            PowerT = input("The amount of power being used is ->")
            TimeT = float(EnergyT) / float(PowerT)
            print("The total time is", TimeT)
        else:   05/06/2018
        print(">>>Error 1 - input was invalid, didn't meet requirements<<<")
        sleep(2)
        print("----------------------------------------")
    elif decision == unit4Choices[1]:
        print("This is how to calculate the EMF of a DC generator.")
        sleep(1)
        print("The equation is similar to the motor one but note that the + is changed to a - .\n    \nEMF = V - (Ia*Ra)")
        sleep(1)
        EMFV2 = input("What's the voltage? -> ")
        Rf2 = input("What's the value of the field resistance? -> ")
        Ra2 = input("What's the armature resistance? -> ")
        print("Give me 2 seconds to calculate the answer...")
        Ia2 = float(EMFV2) / float(Rf2)
        EMFG = float(EMFV2) - (float(Ia2) * float(Ra2))
        sleep(1)
        print("The EMF value of the generator is:", EMFG)
    elif decision == unit4Choices[2]:
        print("You have chosen to calculate the EMF of a DC motor.")
        sleep(1)
        print("The equation is E = V + (Ia*Ra)")
        EMFV = input("What's the voltage? -> ")
        Rf = input("What's the value of the field resistance? -> ")
        Ra = input("What's the armature resistance? -> ")
        print("Just give me 2 seconds to work this out...")
        Ia = float(EMFV) / float(Rf)
        EMFM = float(EMFV) + (float(Ia) * float(Ra))
        sleep(2)
        print("The EMF value is:", EMFM)
    elif decision == unit4Choices[3]:
        def Ohms():
            print("Which do you want to find:\nResistance\nVoltage\nCurrent")
            sleep(1)
            print("Type either 'resistance', 'voltage' or 'current'.")
            ohms_choice = input("So what's your choice -> ")
            sleep(1)
            print("----------")

            if ohms_choice == ohms[0]:
                print("Ok then, let's calculate resistance!")
                sleep(1)
                print("What are the voltage and current values?")
                ohms_voltage = float(input("Voltage is -> "))
                ohms_current = float(input("Current is -> "))
                ohms_resistance = float(ohms_voltage) / float(ohms_current)
                print("The resistance affecting the current  is:", ohms_resistance)
            elif ohms_choice == ohms[1]:
                print("Alright! Let's calculate Voltage")
                sleep(1)
                ohms_current2 = float(input("What's the current? -> "))
                ohms_resistance2 = float(input("What's the resistance? -> ")) #30/06/2018
                Ohms_voltage2 = float(ohms_current2) * float(ohms - resistance2)
                print("----------")
                sleep(1)
                print("This is the voltage being outputted:", Ohms_voltage2)
            elif ohms_choice == ohms[2]:
                print("So current is your intended calculation.")
                sleep(1)
                print("Enter in the corresponding values;")
                voltage3 = float(input("What's the voltage -> "))
                resistance3 = float(input("What's the resistance -> "))
                current3 = float(voltage3) / float(resistance3)
                print("There are this many amps flowing through the circuit,", current3)
            else:
                print(">>>>Error 1 - Invalid Input<<<<")
    elif decision == unit4Choices[4]:
        print("")
        print("The equations used are\nw=2πF\nXl = 2πFL\nXc = 2πFC\nFrequency will be standardised as will the angular velocity.")
        frequencyV = str(input("Frequency: "))
        angleV = float(2) * float(_pi) * float(frequencyV)
        print("Choose either:\nXl\nOr\nXc.\n----------")
        phaseInput = str(input("Choice: "))
        if phaseInput == phaseChoices[0]:
            print("")
            sleep(2)
            print("To calculate Xl we use the angular velocity(2πF) then multiply it by the amount of Henries(L)\nThe new equation becomes 2πFL")
            print("")
            henries = int(input("Henries: "))
            source = float(angleV) * float(henries)
            print("The solution is:",source)
        elif phaseInput == phaseChoices[1]:
            print("")
            sleep(2)
            print("To calulate Xc use the equation\n Xc = 2πFC")
            Xcapactiance = int(input("Capacitance: "))
            Therapy = float(angleV) * float(Xcapactiance)
            print("The solution is",Therapy)
        else:
            print("Error 1 - Invalid Input")
    elif decision == unit4Choices[5]:
        print("")
        sleep(2)
        print("Power is calculate through either\nP=I^2*R\nOr\nP=V*I\nIt's common practise to use the first equation as that is what's more likely to be used within the exam.")
        sleep(2)
        powerInput = str(input("Choice: "))
        if powerInput == powerChoices[0]:
            print("Current is calculated by using Power / Resistance")
            sleep(2)
            print("")
            sleep(2)
            PowerC = int(input("Power: "))
            resistanceC = int(input("Resistance: "))
            currentC = float(PowerC) * float(resistanceC)
            print("The value of current is,",currentC)
        elif powerInput == powerChoices[1]:
            print("Power is calculated by using Current^2 x resistance")
            sleep(2)
            print("")
            currentP = int(input("Current: "))
            currentP2 = float(currentP) * float(currentP)
            resistanceP = int(input("Resistance: "))
            power2 = float(currentP2) * float(resistanceP)
            print("The power value is,", power2)
        elif powerInput == powerChoices[2]:
            print("Resistance is calculated by using power / current^2")
            sleep(2)
            print("")
            powerR = int(input("Power: "))
            currentR = int(input("Current: "))
            currentR2 = float(currentR) * float(currentR)
            resistanceR = float(powerR) / float(currentR2)
            print("The value of the resistance is", resistanceR)
        else:
            print(">>>Error 1 - Invalid Input<<<")
    elif decision == unit4Choices[6]:
        print("")
        sleep(2)
        print("Type either:\nCapacitance\nResistance")
        totalInput = str(input("Choice: "))
        if totalInput == totalRcChoices[0]:
            print("")
            sleep(2)
            print("Series or parallel")
            def seriesCap():
                userInput = int(input("Number of capactitors: "))
                for i in range(0, userInput):
                    ca_pinput = int(input("Capacitor Value: ")
                    capArray.append(ca_pinput)  # 27/12/1977
                print(capArray)
                totalCap = float(1) / float(sum(capArray))
                print(totalCap)
            def parallelCap():
                userInput = int(input("Number of capactitors: "))
                for i in range(0, userInput):
                    ca_pinput = int(input("Capacitor Value: ")
                    capArray.append(ca_pinput)  # 27/12/1977
                    print(capArray)
                    totalCap = sum(capArray)
                    print(totalCap)
            if totalInput == spChoices[0]:
                parallelCap()
            elif totalInput == spChoices[1]:
                seriesCap()
            else:
                print("Error 1 - Invalid Input")
        elif totalInput == totalRcChoices[1]:
            print("")
            sleep(2)
            print("Parallel or series")
            def seriesRes():
                resInput = int(input("N# Resistors: "))
                for i in range(resInput):
                    resValue = int(input("Resistor Value: "))
                    resistArray.append(resValue)
                #print(resistArray)
                totalResS = sum(resistArray)
                sleep(2)
                print(totalResS)
            def parallelRes():
                resInput = int(input("N# Resistors: "))
                for i in range(resInput):
                    resValue = int(input("Resistor Value: "))
                    new_resValue = float(1) / float(resValue)
                    resistArray.append(new_resValue)
                print(resistArray)
                totalResP = float(1) / float(sum(resistArray))
                sleep(2)
                print(totalResP)
            S_pinput = str(input("Choice: "))
            if S_pinput == spChoices[0]:
                parallelRes()
            elif S_pinput == spChoices[1]:
                seriesRes()
            else:
                print("Error 1 - Invalid Input")
        else:
            print("Error 1 - Invalid Input")
window = tkinter.Tk()
window.title("Unit Revision selection UI")
explainLabel = tkinter.Label(window, text="Click either Unit 1, Unit2, Unit 3 or Unit 4 to begin...", font=("Arial", 10))
interfaceEntry = tkinter.Entry(window)
unit1Button = tkinter.Button(window, text="Unit 1", font=("OCR A extended", 9), bg="#cc0000", fg="#000000", state="disabled")
unit2Button = tkinter.Button(window, text="Unit 2", font=("OCR A extended", 9), bg="#0000cc", fg="#000000", state="disabled")
unit3Button = tkinter.Button(window, text="Unit 3", font=("OCR A extended", 9), bg="#00cc00", fg="#000000", state="disabled")
unit4Button = tkinter.Button(window, text="Unit 4", font=("OCR A extended", 9), bg="#ffffff", fg="#000000", state="disabled")



