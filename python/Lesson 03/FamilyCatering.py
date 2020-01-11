#FamilyCatering.py
#A small menu program for a ficticious business that specializes in large meal catering.


#Constants

ENTREE_01 = "Fried Chicken Dinner"
ENTREE_02 = "Pot Roast Dinner"
ENTREE_03 = "Lasagna Dinner"
ENTREE_PRICE_01 = 4.25
ENTREE_PRICE_02 = 4.85
ENTREE_PRICE_03 = 5.15

MINIMUM_ORDER = 30.00

DISCOUNT_LOW = 5
DISCOUNT_HIGH = 10
DISCOUNT_LOW_PRICE = 50.00
DISCOUNT_HIGH_PRICE = 120.00


#Variable

entreeChoice = None
entreePrice = None

numPeople = None

totalCost = None #total *before* discount
totalPrice = None #total *after* discount

#Main Program
print("---------->Family Catering<------------")
print()
print("Entree menu;")
print(" (A) -", ENTREE_01, " > $", ENTREE_PRICE_01, "per person.")
print(" (B) -", ENTREE_02, " > $", ENTREE_PRICE_02, "per person.")
print(" (C) -", ENTREE_03, " > $", ENTREE_PRICE_03, "per person.")
print()
print("There is minimum price of $", MINIMUM_ORDER, "per order.")
print("There is a", DISCOUNT_LOW, "% discount on orders over $", DISCOUNT_LOW_PRICE)
print("There is a", DISCOUNT_HIGH, "% discount on orders over $", DISCOUNT_HIGH_PRICE)
print()

userInput = str.upper( str.strip( input("What entree would you like for your order?:") ) )

if userInput == "A":
    entreeChoice = ENTREE_01
    entreePrice = ENTREE_PRICE_01
elif userInput == "B":
    entreeChoice = ENTREE_02
    entreePrice = ENTREE_PRICE_02
elif userInput == "C":
    entreeChoice = ENTREE_03
    entreePrice = ENTREE_PRICE_03
else:
    print("...'", userInput, "' is not a valid option!")

if entreeChoice == None:
    print("..You did not select an entree.")
    print("CANCELING order.")

else:
    numPeople = int( input("How many people are you ordering for?:"))

    if numPeople < 1:
        print("...You must order for at least 1 person! Changing to 1 person...")
        numPeople = 1

    print()
    print()

    totalCost = numPeople * entreePrice

    if totalCost >= DISCOUNT_HIGH_PRICE:
        discount = totalCost * DISCOUNT_HIGH / 100
        totalPrice = totalCost - discount
        print("Applying a discount for this order.")
        print("$", totalCost," - ", DISCOUNT_HIGH, "% = $", totalPrice)
    elif totalCost >= DISCOUNT_LOW_PRICE:
        discount = totalCost * DISCOUNT_LOW / 100
        totalPrice = totalCost - discount
        print("Applying a discount for this order.")
        print("$", totalCost," - ", DISCOUNT_LOW, "% = $", totalPrice)
    elif totalCost < MINIMUM_ORDER:
        print("The minimum order price is $", MINIMUM_ORDER, "!")
        totalPrice = MINIMUM_ORDER
    else:
        totalPrice = totalCost

    print()
    print("Your order is for", entreeChoice, "to feed", numPeople, "people.")
    print("The final price is $", totalPrice)
    
