#Import various libraies that we might need
import time #Slows the prompts down

# Here we set up the various variables needed
_extra_charge = ["0", "0.75", "1.35", "2.00", "2.50"]
_pizzas = []

_discount = round(float(0), 2)
_delivery_charge = round(float(0.00), 2)
_total = round(float(0), 2)
_pizza_total = round(float(0), 2)
_small_amount = round(float(0), 2)
_medium_amount = round(float(0), 2)
_large_amount = round(float(0), 2)
_small_price = round(float(3.25), 2)
_medium_price = round(float(5.51), 2)
_large_price = round(float(7.15), 2)
_add_cost = round(float(0), 2)

_choice = 0
_attempts = 0

_tops = False
_deliver = False

_cust_name = ""
_cust_addr = ""
_cust_numb = ""
_cod = ""
_toppings = ""
_pizza_request = int(0)


#Costs + Output
def SophieFrancis():
    print("__________\nName:",_cust_name,"\nAddress:",_cust_addr,"\nContact Number(#):",_cust_numb)
    print("----------\n      Pizzas\n    SIZE    PRICE(£)")
    for i in range(len(_pizzas)):
        if _pizzas[i] == "S":
            print("    ",_pizzas[i],"     ",round(_small_price, 2))
        elif _pizzas[i] == "M":
            print("    ",_pizzas[i],"     ",round(_medium_price, 2))
        elif _pizzas[i] == "L":
            print("    ",_pizzas[i],"     ",round(_large_price, 2))
        else:
            print("An Error has occured. Please restart the program!")
    print("----------\n    TOPPINGS(#)    PRICE(£)    TOPPINGS\n        ",_choice,"          ",round(_add_cost, 2),"    ",_toppings)
    print("----------\n    EXTRA CHARGES(£)\n      Delivery: ",round(_delivery_charge, 2),"\n       Discount: ", round(_discount, 2))
    print("----------\n      TOTAL\n    (£)",round(_total, 2),"\n__________")
        
def MrBeltandWezol():
#Here we want to:
#        * Create a link to the variables declared eariler.
#        * Find out the cost of the pizzas without any additional costs such as delivery
#        * What we do is multiply the price for each pizza by the counters we increased eariler, then add them all together.
#        * Add cost and delivery charge were defined just before we asked for the pizza sizes.

    global _total
    global _pizza_total
    global _small_price
    global _medium_price
    global _large_price
    global _small_amount
    global _medium_amount
    global _large_amount
    global _add_cost
    global _discount
    global _deliver
    global _delivery_charge
    _pizza_total = (_small_price * _small_amount) + (_medium_price * _medium_amount) + (_large_price * _large_amount)
    _total = (_pizza_total) + (_add_cost)
    if _total >= 20:
        _discount = (_total)/(10)
    else:
        _discount = 0

    if _cod == "Y":
        _delivery_charge = float(2.50)
        #print("hello")
    elif _cod == "N":
        _delivery_charge = float(0)
        #print("world")
    else:
        _delivery_charge = float(1234.56)
        
    _total = (_pizza_total) + (_add_cost) - (_discount) + (_delivery_charge)
    SophieFrancis()


#Pizza Handler
def RavingUnicornKitty():
#Here we want to:
#        * Ask the user what size of pizza they want, depending on how many they asked for.
#        * After, the counter is increased to find out how many specific size pizzas were requested (USED LATER ON!)
#        * Finally we move onto the function that tallies up the total cost. """
    for i in range (_pizza_request): #Create a loop so that the function will run as long as the var is within the range
        n = i + 1
        print("----------\nPizza", n)
        _new_pizza = str(input("What size (S/M/L): "))
        _pizzas.append(_new_pizza)
        if _new_pizza == "S":
            global _small_amount
            _small_amount = _small_amount + 1
        elif _new_pizza == "M":
            global _medium_amount
            _medium_amount = _medium_amount + 1
        elif _new_pizza == "L":
            global _large_amount
            _large_amount = _large_amount + 1
        else:
            print("Invailid Input - Try again :)")
            global _attempts
            if _attempts == 10:
                print("Stop wasting our time :)")
                quit()
            else:
                _attempts = _attempts + 1
                RavingUnicornKitty()
    
    print("----------\nNow for toppings.\nIMPORTANT: If you DO NOT want any type (0)!!")
    
    _tops_number = float(input("How many toppings? (0-4): "))
    if _tops_number == 0:
        _choice = 0
        _add_cost = float(_extra_charge[0])
    elif _tops_number == 1:
        _toppings = str(input("Please enter what topping(s): "))
        _choice = 1
        _add_cost = float(_extra_charge[1])
    elif _tops_number == 2:
        _toppings = str(input("Please enter what topping(s): "))
        _choice = 2
        _add_cost = float(_extra_charge[2])
    elif _tops_number == 3:
        _toppings = str(input("Please enter what topping(s): "))
        _choice = 3
        _add_cost = float(_extra_charge[3])
    elif _tops_number == 4:
        _toppings = str(input("Please enter what topping(s): "))
        _choice = 4
        _add_cost = float(_extra_charge[4])
    else:
        print("Stop wasting our time.")
        Start()

    MrBeltandWezol()    #After the condition is met the program exits the loop and runs the next function


# Now come in the inputs
def Start():
#Here we need to:
#        * Create links to the variables declared eariler to edit them.
#        * Prompt the user for information, while creating a timer to make it easier to read.
#        * Then ask how many toppings they want (0 to 4).
#        * Afterwards the statement is ran to set the extra cost to the amount of toppings asked for, 1 -> £0.75 etc
#        * Now we check for if the user asked for delivery then set the boolean appropriate to their request
#        * Finally we start the function to ask for pizza sizes"""
    global _cust_name
    global _cust_addr
    global _cust_numb
    global _cod
    global _pizza_request
    global _toppings
    global _choice
    global _add_cost
    
    time.sleep(1)   #Set an interval between the print messages so that the screen doesn't get overloaded with text
    _cust_name = str(input("Name: "))   #Ask for the name, address and phone number
    time.sleep(1)
    _cust_addr = str(input("Address: "))
    time.sleep(1)
    _cust_numb = float(input("Phone: "))
    time.sleep(1)
    _cod = str(input("Deliver(Y/N): "))
    time.sleep(1)
    _pizza_request = int(input("Pizzas (#): "))
    time.sleep(1)
    RavingUnicornKitty()
print("----------\nPlease fill out the following form to complete your order:")     #THIS IS THE START!!!!
Start()
#Daxess - ©
