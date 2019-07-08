#Spencer Poultney, October 3rd 2017
#'''This program allows a user to choose a specific type of beverage, after that is done it calculates the total cost and prints it along with details of the beverage'''

#Declaring tax as a constant and price as a changeable integer
TAX = 1.11
price = 0
#Allows us to have delays after error messages and when we print our final statement so python doesnt close down before the user can read them
import time
#Getting name of customer and making only first letter capitalized
customerName = str(input("Hello, what is your first name?: ")).lower().title()
#If they enter a name with only characters..
if customerName.isalpha() :
    #Get whether they are drinking coffee or tea
    beverage = input("Nice to meet you, what kind of beverage would you like today?(Coffee or Tea): ").upper()
    #If they choose coffee..
    if beverage == "COFFEE" or beverage == "C" :
        beverage = "coffee"
        #Get what size they would like and raise price accordingly
        size = input("What size will that be?(Small, Medium, or Large): ").upper()

        if size == "SMALL" or size == "S" :
            size = "small"
            price = price + 1.50
            #Get what flavoring they would like and raise price accordingly
            flavoring = input("Would you like any flavor shots?(Vanilla, Chocolate, Maple, or none): ").upper()
            if flavoring == "VANILLA" or flavoring == "V" :
                flavoring = "vanilla"
                price = price + 0.25
            elif flavoring == "CHOCOLATE" or flavoring == "C" :
                flavoring = "chocolate"
                price = price + 0.75
            elif flavoring == "MAPLE" or flavoring == "M" :
                flavoring = "Maple"
                price = price + 0.50
            elif flavoring == "NONE" or flavoring == "N" :
                flavoring = "no"
                price = price + 0
             #Sends error message then quits program if an unlisted option is entered, this repeats throughout the code
            else :
                print("Sorry, that flavor does not exist.")
                time.sleep(5)
                quit()


        elif size == "MEDIUM" or size == "M" :
            size = "medium"
            price = price + 2.50

            flavoring = input("Would you like any flavor shots?(Vanilla, Chocolate, Maple, or none): ").upper()
            if flavoring == "VANILLA" or flavoring == "V" :
                flavoring = "vanilla"
                price = price + 0.25
            elif flavoring == "CHOCOLATE" or flavoring == "C" :
                flavoring = "chocolate"
                price = price + 0.75
            elif flavoring == "MAPLE" or flavoring == "M" :
                flavoring = "Maple"
                price = price + 0.50
            elif flavoring == "NONE" or flavoring == "N" :
                flavoring = "no"
                price = price + 0
            else :
                print("Sorry, that flavor does not exist.")
                time.sleep(5)
                quit()

        elif size == "LARGE" or size == "L" :
            size = "large"
            price = price + 3.25

            flavoring = input("Would you like any flavor shots?(Vanilla, Chocolate, Maple, or none): ").upper()
            if flavoring == "VANILLA" or flavoring == "V" :
                flavoring = "vanilla"
                price = price + 0.25
            elif flavoring == "CHOCOLATE" or flavoring == "C" :
                flavoring = "chocolate"
                price = price + 0.75
            elif flavoring == "MAPLE" or flavoring == "M" :
                flavoring = "Maple"
                price = price + 0.50
            elif flavoring == "NONE" or flavoring == "N" :
                flavoring = "no"
                price = price + 0

            else :
                print("Sorry, that flavor does not exist")
                time.sleep(5)
                quit()
        else :
            print("Sorry, that size does not exist.")
            time.sleep(5)
            quit()

    #If customer chooses tea... (same process as for coffee just different flavors)
    elif beverage == "TEA" or beverage == "T" :
        beverage = "tea"

        size = input("What size will that be?(Small, Medium, or Large): ").upper()

        if size == "SMALL" or size == "S" :
            size = "small"
            price = price + 1.50

            flavoring = input("Would you like any flavor shots?(Mint, Lemon, or None): ").upper()
            if flavoring == "MINT" or flavoring == "M" :
                flavoring = "mint"
                price = price + 0.50
            elif flavoring == "LEMON" or flavoring == "L" :
                flavoring = "lemon"
                price = price + 0.25
            elif flavoring == "NONE" or flavoring == "N" :
                flavoring = "no"
                price = price + 0

            else :
                print("Sorry, that flavor does not exist.")
                time.sleep(5)
                quit()

        elif size == "MEDIUM" or size == "M" :
            size = "medium"
            price = price + 2.50

            flavoring = input("Would you like any flavor shots?(Mint, Lemon, or None): ").upper()
            if flavoring == "MINT" or flavoring == "M" :
                flavoring = "mint"
                price = price + 0.50
            elif flavoring == "LEMON" or flavoring == "L" :
                flavoring = "lemon"
                price = price + 0.25
            elif flavoring == "NONE" or flavoring == "N" :
                flavoring = "no"
                price = price + 0

            else :
                print("Sorry, that flavoring does not exist.")
                time.sleep(5)
                quit()

        elif size == "LARGE" or size == "L" :
            size = "large"
            price = price + 3.25

            flavoring = input("Would you like any flavor shots?(Mint, Lemon, or None): ").upper()
            if flavoring == "MINT" or flavoring == "M" :
                flavoring = "mint"
                price = price + 0.50
            elif flavoring == "LEMON" or flavoring == "L" :
                flavoring = "lemon"
                price = price + 0.25
            elif flavoring == "NONE" or flavoring == "N" :
                flavoring = "no"
                price = price + 0

            else :
                print("Sorry, that flavor does not exist.")
                time.sleep(5)
                quit()
        else :
            print("Sorry, that size does not exist.")
            time.sleep(5)
            quit()

    else :
        print("Sorry, we don't sell that type of beverage.")
        time.sleep(5)
        quit()
    #Calculating final price of beverage with tax included
    price = price * TAX
    #Printing final statement which states the name of the customer, the size of their beverage, the type of beverage, any added flavoring, and the final price
    print("For {}, a {} {} with {} flavoring, that will be ${} including tax".format(customerName,size.lower(),beverage.lower(),flavoring.lower(),round(price,2)))
    time.sleep(25)
    #If the customer did not enter a valid name using characters only, a error message displays
else :
    print("Error: You did not enter a valid name. (Characters only)")
    time.sleep(5)
    quit()
