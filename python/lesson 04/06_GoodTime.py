""" 06_GoodTime.py - A script for Clueless To Coding - Python - Lesson 4"""

#Next Step: Can We Make Nice Now?
""" Next we add a new feature by taking advantage of the reusability inherent
   in the use of functions. We will change the program so that it displays
   the time that is recorded whenever the user hits enter. Check out the
   comments in the Main Program section for more details.
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

    #NEXT- change the line below so that it assigns to 'rawTime' instead of
    # 'thisTime'
    thisTime = time()

    #NEXT - Unquote the code inside the if structure below:
    if userInput == "":
        """thisTime =  rawTime - startTime
        lapTimes.append(thisTime)
        print("\----->", makeNiceTime(thisTime))
        """
        

for index in range(len(lapTimes)):
    print(index, makeNiceTime(lapTimes[index]))
    


#NEXT - These changes move the calculation for the lap time outside of the
#  append() call so that the result can be used in both the append() call and
#  the print() call.

#NEXT -  Save the changes and run the program.


#WHAT THIS SHOULD DO: At this point the program should record times, print each
#  time out as it is recorded and print all the times out before exiting.

#NEXT STEP --> Open the file '07_GoodTime.py' and follow its instrctions.
