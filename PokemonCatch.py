import tkinter
def FindPokemon():
    _numOfCandiesNeeded = input("How many Candies to evolve: ")
    _numOfCandiesCurrent = input("How many Candies you have: ")
    _numOfPokemonCatch = int(_numOfCandiesNeeded) - int(_numOfCandiesCurrent)
    _numOfPokemonCatch = int(_numOfPokemonCatch) / int(3)
    print("Pokemon needed to catch:",round(_numOfPokemonCatch))
    print(">>>>>>")

def FindPokemon2():
    _numOfCandiesNeeded = input("How many Candies to evolve: ")
    _numOfCandiesCurrent = input("How many Candies you have: ")
    _numOfPokemonCatch = int(_numOfCandiesNeeded) - int(_numOfCandiesCurrent)
    _numOfPokemonCatch = int(_numOfPokemonCatch) / int(6)
    print("Pokemon needed to catch:",round(_numOfPokemonCatch))
    print(">>>>>>")

mainInterface = tkinter.Tk()
mainInterface.title("Pokemon GO Catch Calculator")
_label = tkinter.Label(mainInterface, text="Click the button to start", font=("Terminal", 16), fg="#000000")
_button = tkinter.Button(mainInterface, text="Calculate(No Berries)!", font=("Terminal", 16), bg="#009900", fg="#ffffff", command=FindPokemon)
_button2 = tkinter.Button(mainInterface, text="Calculate (Berries)!", font=("Terminal", 16), bg="#990000", fg="#ffffff", command=FindPokemon2)

_label.grid(row=0, column=0)
_button.grid(row=0, column=1)
_button2.grid(row=0, column=2)
mainInterface.mainloop
