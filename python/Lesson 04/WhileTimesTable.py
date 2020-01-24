#TimesTable.py
#A program that displays a multiplication table

#Constants

X_END = 10
Y_END = 10

#Variables

thisLine = "" #this holds each row as it it being built

#Main program

y = 0
while y < Y_END:
    multiplicand = y + 1
    thisLine = ""
    x = 0
    while x < X_END:
        multiplier = x + 1
        product = multiplicand * multiplier
        thisLine = thisLine + format(product, ">4d")
        x += 1
    print(thisLine)
    y += 1
