feet = float(input("Enter the number of feet:"))
inches = float(input("Enter the number of inches:"))

print("You entered", feet, "ft. and", inches, "in.")

totalInches = (feet *12) + inches

print("That is a total of", totalInches, "in.")

cFactor = 0.3936
totalCentimeters = totalInches / cFactor

print("That is a total of", totalCentimeters, "cm.")

meters = int(totalCentimeters / 100)
centimeters = totalCentimeters % 100

print("Which is", meters, "m. and", centimeters, "cm.")

