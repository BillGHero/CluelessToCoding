#TimesTable.py
#A program that displays a multiplication table

#Constants

X_END = 10
Y_END = 10

#Variables

thisLine = "" #this holds each row as it it being built

#Main program

for y in range(Y_END):
    multiplicand = y + 1
    thisLine = ""
    for x in range(X_END):
        multiplier = x + 1
        product = multiplicand * multiplier
        thisLine = thisLine + format(product, ">4d")
    print(thisLine)
        
