ICE_CREAM = "Ice-Cream"
ICE_CREAM_CUP = "Ice-Cream in a Cup"
ICE_CREAM_CAKE_CONE = "Ice-Cream in a Cake Cone"
ICE_CREAM_WAFFLE_CONE = "Ice-Cream in a Waffle Cone"
ICE_CREAM_SANDAE = "Ice-Cream Sundae"
FROZEN_YOGURT = "Frozen Yogurt"

FLAVOR_VANILLA = "Vanilla"
FLAVOR_CHOCOLATE = "Chocolate"
FLAVOR_STRAWBERRY = "Strawberry"
FLAVOR_NONDAIRY_VANILLA = "Non-Dairy Vanilla"


product = None
maxScoops = None
numScoops = None
flavor = None
ouncesFrozenYogurt = None


print("Welcome to Our Ice Cream Shop!")
print()
print()

print("What would you like?-")
print("  (1) - Ice cream")
print("  (2) - Frozen yogurt")

userInput = str.strip(input("Your choice is:"))

print()

if userInput == '1':
    print("You chose Ice-Cream, yay!")
    print()
    product = ICE_CREAM

    print()
    print()
    print("---Ice-Cream Menu---")
    print(" (A) - in a Cup")
    print(" (B) - in a Cake Cone")
    print(" (C) - in a Waffle Cone")
    print(" (D) - as a Sundae")
    userInput = str.upper( str.strip( input("Your Choice:") ) )

    if userInput == 'A':
        product = ICE_CREAM_CUP
        maxScoops = 3
    elif userInput == 'B':
        product = ICE_CREAM_CAKE_CONE
        maxScoops = 2
    elif userInput == 'C':
        product = ICE_CREAM_WAFFLE_CONE
        maxScoops = 3
    elif userInput == 'D':
        product = ICE_CREAM_SANDAE
        maxScoops = 5
    else:
        print(userInput, "is not a valid choice...")
        print("...Defaulting to", ICE_CREAM_CUP, ".")
        product = ICE_CREAM_CUP
        maxScoops = 3

    print()
    print()
    print("What flavor would you care for in your", product,"?")
    print(" (V) - Vanilla")
    print(" (C) - Chocolate")
    print(" (S) - Strawberry")
    print(" (N) - Non-Dairy Vanilla (Rice-Based)")
    userInput = str.upper( str.strip( input("Your choice?:") ) )

    if userInput == 'V':
        flavor = FLAVOR_VANILLA
    elif userInput == 'C':
        flavor = FLAVOR_CHOCOLATE
    elif userInput == 'S':
        flavor = FLAVOR_STRAWBERRY
    elif userInput == 'N':
        flavor = FLAVOR_NONDAIRY_VANILLA
    else:
        print(userInput, "isn't an option!")
        print("Selecting", FLAVOR_NONDAIRY_VANILLA, ".")
        flavor = FLAVOR_NONDAIRY_VANILLA

    print()
    print()
    print("You can have up to", maxScoops, "scoops of", flavor, "in a", product)
    userInput = input("How many would you like?:")
    numScoops = int(userInput)

    if numScoops > maxScoops:
        numScoops = maxScoops
    elif numScoops < 1:
        numScoops = 1
        
    
elif userInput == '2':
    print("Nice! Frozen Yogurt.")
    print()
    product = FROZEN_YOGURT

    print()
    print("Frozen yogurt is sold by the ounce. We charge for a minimum of 10 ounces,")
    print("and the container more than 36 ounces.")
    ouncesFrozenYogurt = float(input("How many ounces do you have?:"))

    if ouncesFrozenYogurt < 10:
        ouncesFrozenYogurt = 10.0
    elif ouncesFrozenYogurt > 36:
        ouncesFrozenYogurt = 36.0
                               
else:
    print("oh '", userInput, "' is not a valid option...")


if product == None:
    print("You didn't order anything. Don't you want a yummy desert?")
elif product == FROZEN_YOGURT:
    print()
    print()
    print("You have", ouncesFrozenYogurt, "ounces of", product)

else:
    print()
    print()
    print("You have", numScoops, "scoops of", flavor, product)
