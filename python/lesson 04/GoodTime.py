""" 07_GoodTime.py - A script for Clueless To Coding - Python - Lesson 4"""

#Next Step: By the Numbers, Please
""" That new method of using for loops to act directly upon a list is quite
   useful. It does come with one drawback: we no longer have an obvious way to
   know what index we are currently on. This means we need another method to
   track our lap numbers. The method we will use for this final change to the
   program is to use an 'Acumulator' variable. We will simply keep track of
   our iterations using a separate variable that is incremented each time
   the for loop iterates. Check out the comments in the Function Section for
   more details.
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
    

#showFinalTimes() - Accepts a list of times (in seconds) and displays them in
#  a nicely formatted table.
def showFinalTimes(timeList):
    print()
    print("Lap Time Report:")
    print()
    #NEXT - delete the following line and unquote the next one.
    print("hh:mm:ss:%%")
    """print("Lap>hh:mm:ss:%%")"""
    
    #NEXT - Unquote the following line:
    """lapNum = 1 #Initialize the accumulator to 1"""
    for thisTime in timeList:
        #NEXT - Delete the next line and unquote the triple quotes the follow:
        print(makeNiceTime(thisTime))
        """lapString = format(lapNum, '>3') + '>'
        print(lapString + makeNiceTime(thisTime))
        lapNum += 1
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
        

showFinalTimes(lapTimes)


#NEXT -
""" These changes add an extra column header for the list. Then a counter
 variable is initialized to 1 just prior to the for loop. Each iteration of the
 for loop builds a string to preface the lap time, and then increments the
 counter. The operator used to increment is interesting here. ‘ += ‘ is an
 operator which add whatever is on the right hand side to the variable on the
 left and then stores that result in the variable on the left. This short-hand
 way of incrementing variables is popular for more than just the typing it
 saves: it makes it very clear that the statement is meant to increment the
 variable on the left, this clarity is very helpful when maintaining and
 debugging code. """


#NEXT -  Save the changes and run the program.


#WHAT THIS SHOULD DO: At this point the program should record times, print each
#  time out as it is recorded and print all the times out before exiting. But
#  the final print-out should look even better.

#NEXT STEP --> That's it. We're done!
