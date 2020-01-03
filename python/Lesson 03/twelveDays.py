DAY_01 = "a partridge in a pair tree"
DAY_02 = "Two turtle Doves"
DAY_03 = "Three French Hens"
DAY_04 = "Four Calling Birds"
DAY_05 = "Five Golden Rings"

notTheFirstDay = None




print("The Twelve Days of Christmas")
print()
print("I need know what day of Christmas it is.")

userInput = str.strip( input("What day is it?:") )

day_of = int(userInput)

if day_of > 12:
    day_of = 12
elif day_of < 1:
    day_of = 1

if day_of != 1:
    notTheFirstDay = True
else:
    notTheFirstDay = False
    

print()
print()
print("One the", day_of, " of Christmas my true love gave to me")

if day_of == 5:
    day_of = day_of - 1
    print(DAY_05)

if day_of == 4:
    day_of = day_of - 1
    print(DAY_04)

if day_of == 3:
    day_of = day_of - 1
    print(DAY_03)

if day_of == 2:
    day_of = day_of - 1
    print(DAY_02)

if day_of == 1:
    
    if notTheFirstDay:
        thisLine = "and " + DAY_01
    else:
        thisLine = DAY_01
        
    day_of = day_of - 1
    print(thisLine)

    
