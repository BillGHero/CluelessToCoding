""" 07_GoodTime.py - A script for Clueless To Coding - Python - Lesson 4"""

#Next Step: Status Report!
""" The last moving part we need is a tidy way to display the final report. For
   this we will write a function that does that, and then call it from the main
   program. Within this new function we will see a new way to use for loops in
   Python. Check out the coments in the Function Section for more details.
   """

#----> Import statements go here:
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
    

# makeNiceTime(time) - takes an input in number of seconds and sorts it into
#hours, minutes, seconds, and hundredths
def makeNiceTime(time):
    """makeNiceTime(time) - formats the time, in seconds."""
    
    niceTime = ""

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
    

#NEXT - Write a function definition statement for the new function. Name it
#  'shwoFinalTimes' and include an argument variable named 'timeList'. Note that
#  this function is replacing the for loop at the very end of the program. After
#  writing the definition statement, unquote the code block. Check out the
#  comments in the Main Program section to continue.
#showFinalTimes() - Accepts a list of times (in seconds) and displays them in
#  a nicely formatted table.
#--->Replace this line with the function definition statement<---
    """print()
    print("Lap Time Report:")
    print()
    print("hh:mm:ss:%%")

    for thisTime in timeList:
        print(makeNiceTime(thisTime))
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

    rawTime = time()

    if userInput == "":
        thisTime =  rawTime - startTime
        lapTimes.append(thisTime)
        print("\----->", makeNiceTime(thisTime))
        
        

#NEXT - Delete the for loop below, and then unquote the function call.
for index in range(len(lapTimes)):
    print(index, makeNiceTime(lapTimes[index]))
"""showFinalTimes(lapTimes)"""


#NEXT - This causes a reasonably neat list of times to print out along with
# column headers to suggest what each column is. It is a little different than
# previous uses of the for loop in that we are not using range(). Instead, we
# are actually using the main list of data the for loop is meant to act upon.
# This is an incredibly useful option for using with for loops.

#NEXT -  Save the changes and run the program.


#WHAT THIS SHOULD DO: At this point the program should record times, print each
#  time out as it is recorded and print all the times out before exiting. But
#  the final print-out should look better.

#NEXT STEP --> Open the file 'GoodTime.py' and follow its instrctions.
