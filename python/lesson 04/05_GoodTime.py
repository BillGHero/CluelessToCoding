""" 05_GoodTime.py - A script for Clueless To Coding - Python - Lesson 4"""

#Next Step: Can We Make Nice Now?
""" We are going to add a new function that massages our lap times to make
   them easier to read. It is a rather long function, but it is also actually
   quite simple in its basic concepts. Check out the comments in the function
   section for more details.
   """

#----> Import stements go here:
from time import time


#----> Functions Go Here:

# showTitle() - Displays the title
def showTitle():
    print("**********Lap Timer**********")
    print()

# showInstructions() - Displays the instructions
def showInstructions():
    print("Press Enter to record time for each lap.")
    print("Enter 'q' after last lap is recorded.")
    
#NEXT - Create a function definition statement. Name the function 'makeNiceTime'
#  but there is a twist. This function takes an argument, the time to be
#  formatted - in seconds. To allow for this argument, place the variable name
#  'time' inside the parentheses within the function definition. Then unquote
#  the code block for the function. Then check the next NEXT in the Main Program
#  section.
# makeNiceTime(time) - takes an input in number of seconds and sorts it into
#hours, minutes, seconds, and hundredths
#--->Replace this line with the function definition<---
"""    niceTime = ""

    hours = int(time / (60*60) )
    niceTime = niceTime + format(hours, '02') + ":"
    time = time - (hours * (60 * 60) )

    minutes = int(time / 60)
    niceTime = niceTime + format(minutes, '02') + ":"
    time = time - (minutes * 60)

    seconds = int(time)
    niceTime = niceTime + format(seconds, '02') + ":"

    hundredths = int( (time % 1) * 100 ) # '%' modulus, or remainder. of a division
    niceTime = niceTime + format(hundredths, '02')

    return niceTime #'return' is used to send data back to the function caller.
    """



#----> Main program starts here:

showTitle()

showInstructions()

# use input() to find out when the user is ready to start timing
input("Press ENTER to start timing")
startTime = time()

userInput = "" #userInput will be used to decide if the user is done timing
lapTimes = []

while userInput == "": # IF the user just hits enter, the loop will contiune
    userInput = input("Press ENTER to record a lap time (or 'q' to quit)")
    thisTime = time()
    if userInput == "":
        lapTimes.append(thisTime - startTime)
        

#NEXT - Use the new function to format the lapTimes[] before they are printed.
#  To do this, change the print() call in the loop below by replacing the triple
#quotes with 'makeNiceTime(lapTimes[index])'
for index in range(len(lapTimes)):
    print(index, """lapTimes[index]""")
    


#NEXT - Save and run the program.


#WHAT THIS SHOULD DO: At this point the program should record times and print
#   them out in a much nicer format before exiting.

#NEXT STEP --> Open the file '06_GoodTime.py' and follow its instrctions.
