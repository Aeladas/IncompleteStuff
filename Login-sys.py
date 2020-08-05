#Project Aquaman
import tkinter
import csv

usernameArray = []
passwordArray = []

def Signup():
    new_username = usernameEntry.get()
    new_password = passwordEntry.get()
    new_name = nameEntry.get()
    usernameArray.append(new_username)
    passwordArray.append(new_password)
    with open("Aquaman.csv", "a") as comics:
        new_comic = csv.writer(comics, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        new_comic.writerow([new_name, new_username, new_password])

def Login():
    temp_username = usernameEntry.get()
    temp_password = passwordEntry.get()
    usernametrue = False
    passwordtrue = False
    with open("Aquaman.csv", "r") as comics2:
        for u in range (len(usernameArray)):
            if temp_username == usernameArray[u]:
                usernametrue = True
            else:
                u = u + 1
        for p in range(len(passwordArray)):
            if temp_password == passwordArray[p]:
                passwordtrue = True
            else:
                p = p + 1
    if (usernametrue == True & passwordtrue == True):
        print("Login successful!")
mainInterface = tkinter.Tk()
mainInterface.title("Log-in Window")
usernameLabel = tkinter.Label(mainInterface, text="Username:", fg="#000000")
passwordLabel = tkinter.Label(mainInterface, text="Password:", fg="#000000")
nameLabel = tkinter.Label(mainInterface, text="Name:", fg="#000000")
usernameEntry = tkinter.Entry(mainInterface, fg="#000099")
passwordEntry = tkinter.Entry(mainInterface, show="*", fg="#000099")
nameEntry = tkinter.Entry(mainInterface, fg="#000099")
loginButton = tkinter.Button(mainInterface, text="Login", bg="#009900", fg="#000000", command=Login)
registerButton = tkinter.Button(mainInterface, text="Register", bg="#990000", fg="#000000", command=Signup)

nameLabel.grid(row=0, column=0)
usernameLabel.grid(row=1, column=0)
passwordLabel.grid(row=2, column=0)
nameEntry.grid(row=0, column=1)
usernameEntry.grid(row=1, column=1)
passwordEntry.grid(row=2, column=1)
loginButton.grid(row=2, column=2)
registerButton.grid(row=0, column=2)
mainInterface.mainloop
