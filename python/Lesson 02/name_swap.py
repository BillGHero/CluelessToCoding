firstName = str.strip(input("Enter a first name, please:"))
lastName = str.strip(input("Enter a last name, please:"))

firstEnd = len(firstName)
lastEnd = len(lastName)

newFirst = str.capitalize(lastName[0]) + firstName[1:firstEnd]
newLast = str.capitalize(firstName[0]) + lastName[1:lastEnd]

finalName = newFirst + " " + newLast

print("The new name is:", finalName)
