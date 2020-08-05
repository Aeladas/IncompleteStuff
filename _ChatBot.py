#MODULES (These are how we import specific functions from different libaries)
from math import *
from time import sleep
import random

#EXPLANATIONS (Now we provide the user with an explanation as to what will happen within the bot...)
print("Welcome to the chat room 'Version 1.0'!\nHere you can play games\nDo some revision\nSolve mathmatical questions\nTest yourself with trivia\neven decrypt a password!\n(Wait until it asks you to type before you start typing a greeting!)")
sleep(2)
print("------------------")
sleep(2)
print("Type one of the following greetings to get started...\nhi\nhey\nhello\nDON'T TYPE 'hi'AS IT CREATES ERRORS!\n")
sleep(2)
print("------------------")
sleep(2)
print(" ")

#ARRAYS (The arrays will store variables that we can use to validate the user's inputs.)
greetings = ['hi', 'hey', 'hello']
yesNo = ['yes', 'no']
jokes = ['Two atoms are walking along. One of them says:\n"Oh, no, I think I lost an electron.”\n“Are you sure?”\n“Yes, I’m positive.','I have a new theory on inertia but it doesn’t seem to be gaining momentum','Why can’t atheists solve exponential equations?\nBecause they don’t believe in higher powers','There are 10 types of people:\nthose who understand binary, and those who do not understand it','An optimist sees a glass half full.\nA pessimist sees it half empty.\nAn engineer sees it twice as large as it needs to be','No thanks']
randomfacts = ['If you consistently fart for 6 years & 9 months, enough gas is produced to create the energy of the atomic bomb!','In 2015, more people were killed from injuries caused by taking a selfie than by shark attacks.','Facebook, Skype and Twitter are all banned in China','The french language has 17 different words for "surrender"','The twitter bird actually has a name - Larry','Panphobia is the fear of everything...\nI guess thats an unlucky phobia to have :(','The bible is the most shoplifted book in the world!','Every year more than 2500 left-handed people are killed from using right-handed products.']

#GREETING THE USER...
usergreeting = input("... ")

if usergreeting == greetings[0]:
    print("Hi there! Did you know:")
    displayFact = random.choice[randomfacts]
    print(displayFact)
    Next()
elif usergreeting == greetings[1]:
    print("What's your favourite song???")
    myFaveSong = input("Mine is 'The Connection - Futurecode' -> ")
    sleep(5)
    print("Oooh I've not heard",myFaveSong,"before I'll have to listen to it before the next time I'm run!!!")
    Next()
elif usergreeting == greetings[2]:
    print("Long time not see haha XD") 
    sleep(1)
    print("Do you want to hear a joke?")
    tellMeaJoke = input("What's your answer? (yes or no) -> ")
    #TELLING A JOKE BASED ON THEIR DECISION...
    if tellMeaJoke == yesNo[0]:
        print("Okay then, pick a number.")
        sleep(0.5)
        jokechoices = ['1', '2', '3', '4', '5', 'Decline']
        myJokeChoice = input("type:\n1\n2\n3\n4\n5\nOr 'Decline', type answer here -> ")
        if myJokeChoice == jokechoices[0]:
            print(jokes[0])
            Next()
        elif myJokeChoice == jokechoices[1]:
            print(jokes[1])
            Next()
        elif myJokeChoice == jokechoices[2]:
            print(jokes[2])
            Next()
        elif myJokeChoice == jokechoices[3]:
            print(jokes[3])
            Next()
        elif myJokeChoice == jokechoices[4]:
            print(jokes[4])
            Next()
        else:
            print("Ok I will not tell you a joke :)")
            Next()
    else:
        print("Well you're no fun :(")
        quit()
else:
    print("Please type in one of the given greetings as I don't understand the dialect your using???")

def explictMode():
    
def Next():
    print("How are you?")
    feeling = input("")
    if feeling.find("good") == True:
        print("That's great to hear!")
    else
    


