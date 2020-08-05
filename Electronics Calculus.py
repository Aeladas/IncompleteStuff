#Electronics Calculator
#import the time management and mathematics modules.
from time import sleep
from tkinter import *
import math
import tkinter

#voltage gain = -Rf/Rin

#Choice system, allows the user to choose their type of calculations. Using a the UI system.
window = Tk()
window.geometry("725x275")
window.title("Choices")

#The arrays we use to validate inputs.
confirms = ["yes","no"]
ohms = ["resistance","voltage","current"]
capacitance = ["parallel","series"]
power = ["current", "power", "voltage"]
energy = ["energy","power","time"]

#This is where we create the fuction that will be instantiated later on...
def Ohms():
    #Ask the user what calculation they want to complete.
    #Also, tell them what exactly to type to achieve the desired outcome.
    print("Which do you want to find:\nResistance\nVoltage\nCurrent")
    sleep(1)
    print("Type either 'resistance', 'voltage' or 'current'.")
    ohms_choice = input("So what's your choice -> ")
    sleep(1)
    print("----------")

    #Check to see if the input is equal to the specified element of the array, if so then validation is complete.
    #Otherwise, tell the user to input a correct response.
    if ohms_choice == ohms[0]:
        print("Ok then, let's calculate resistance!")
        sleep(1)
        print("What are the voltage and current values?")
        ohms_voltage = float(input("Voltage is -> "))
        ohms_current = float(input("Current is -> "))
        ohms_resistance = float(ohms_voltage) / float(ohms_current)
        print("The resistance affecting the current  is:",ohms_resistance)
    elif ohms_choice == ohms[1]:
        print("Alright! Let's calculate Voltage")
        sleep(1)
        ohms_current2 = float(input("What's the current? -> "))
        ohms_resistance2 = float(input("What's the resistance? -> "))
        Ohms_voltage2 = float(ohms_current2) * float(ohms-resistance2)
        print("----------")
        sleep(1)
        print("This is the voltage being outputted:",Ohms_voltage2)
    elif ohms_choice == ohms[2]:
        print("So current is your intended calculation.")
        sleep(1)
        print("Enter in the corresponding values;")
        voltage3 = float(input("What's the voltage -> "))
        resistance3 = float(input("What's the resistance -> "))
        current3 = float(voltage3) / float(resistance3)
        print("There are this many amps flowing through the circuit,",current3)
    else:
        print("You've not entered in a adequate response")
    
def Capacitance():
    print("Which version of capacitance do you want to calculate:\nCapacitance in series\nOr\nCapacitance in parallel")
    sleep(1)
    print("Type either 'series' or 'parallel' to get started!")
    sleep(1)
    cap_choice = input("So what's your choice? -> ")
    sleep(1)
    print("----------")

    if cap_choice == capacitance[0]:
        print("Parallel! Ha these capacitors should have been colour-coded and swapped around, I can do this in nanoseconds.")
        sleep(1)
        number_of_caps = int(input("How many capacitors are there? -> "))
        for i in range(number_of_caps):
            Cap_value = int(input("What's the value of the capacitor? -> "))
    elif cap_choice == capacitance[1]:
        print("I see your choice is series...")
        sleep(1)
        number_of_series = int(input("How many capacitors are connected in series? -> "))
        for i in range(number_of_series):
            series_value = int(input("What's the value of this capacitor? -> "))
def Power():
    print("If the question involves power, current and voltage this is the correct function to utilise.")
    sleep(1)
    print("Type either 'current', 'power' or 'voltage'.")
    sleep(1)
    power_choice = input("What's your choice? -> ")
    def power_doover():
        print("Please type either 'current', 'power' or 'voltage'.")
        sleep(1)
        power_choice = input("What's your choice please choose a valid response this time.")

    if power_choice == power[0]:
        print("Current is what you want me to calculate, let's do it!")
        sleep(1)
        powerC = input("What's the power? -> ")
        voltageC = input("What's the voltage? -> ")
        currentC = float(powerC) / float(voltageC)
        sleep(1)
        print("The current is",currentC)
    elif power_choice == power[1]:
        print("So power is what you seek to find well;")
        sleep(1)
        voltageP = input("What's the voltage value that's being inducted into the circuit? -> ")
        currentP = input("What's the current value flowing within the circuit? -> ")
        powerP = float(voltageP) * float(currentP)
        sleep(1)
        print("This is how many watts are being used by the circuit",powerP)
    elif power_choice == power[2]:
        print("Voltage, this will be done lightning quick!")
        sleep(1)
        powerV = input("What's the power? -> ")
        currentV = input("What's the current -> ")
        voltageV = float(powerV) / float(currentV)
        print("The voltage being inducted is:",voltageV)
    else:
        print("Please try entering in a valid term because what you inputted is an invalid response.")
        power_doover()

def Energy():
    print("This is the energy calculation function\nType either 'energy', 'power' or 'time' to get started")
    sleep(1)
    energy_choice = input("Your choice is -> ")

    if energy_choice == energy[0]:
        print("The equation is Energy = Power * Time")
        sleep(1)
        powerE = input("The power is -> ")
        timeE = input("The time in seconds is -> ")
        energyE = float(powerE) * float(timeE)
        print("The amount of energy being utilised is:",energyE)
    elif energy_choice == energy[1]:
        print("The re-arranged equation is Power = Energy / Time")
        sleep(1)
        energyP = input("How much energy is being used? ->")
        timeP = input("How long was the device used for?(seconds!) -> ")
        powerP = float(energyP) / float(timeP)
        print("The amount of power being used is:",powerP)
    elif energy_choice == energy[2]:
        print("The equation we will use is Time = Energy / Power")
        sleep(1)
        EnergyT = input("The energy being used is -> ")
        PowerT = input("The amount of power being used is ->")
        TimeT = float(EnergyT) / float(PowerT)
        print("The total time is",TimeT)
    else:
        energy_redo()

def DC_Motors():
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
    print("The EMF value is:",EMFM)

def DC_Generators():
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
    
#If the button is clicked then the function is ran.

#Add text and create the buttons that will execute the functions in the UI.
introInstructions = tkinter.Label(window, text="Click the correct coloured button that matches the function you want to complete.")
extraInstructions = tkinter.Label(window, text="After clicking on a button switch to the window with the blue text in it!\nAny button text that is coloured in gray is disabled button meaning that it's code hasn't been added into the program yet.")
ohmsButton = tkinter.Button(window, text="Ohms", bg="#cc0000", fg="#ffffff", bd="2", command = Ohms)
capacitanceButton = tkinter.Button(window, text="Capacitance", bg="#0000cc", fg="#ffffff", bd="2", command = Capacitance, state="disabled")
powerButton = tkinter.Button(window, text="Power", bg="#00cc00", fg="#ffffff", bd="2", command = Power)
energyButton = tkinter.Button(window,text="Energy", bg="#ff9900", fg="#ffffff", bd="2", command = Energy)
motorsButton = tkinter.Button(window, text="DC Motors", bg="#cc0099", fg="#ffffff", bd="2", command = DC_Motors)
generatorButton = tkinter.Button(window, text="DC Generators", bg="#b3b300", fg="#ffffff", bd="2", command = DC_Generators)
#Create packets to make it easier when instantiating the text and buttons.
introInstructions.pack()
extraInstructions.pack()
ohmsButton.pack()
capacitanceButton.pack()
powerButton.pack()
energyButton.pack()
motorsButton.pack()
generatorButton.pack()
window.mainloop()
