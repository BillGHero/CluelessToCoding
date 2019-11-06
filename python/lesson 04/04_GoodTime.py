""" 04_GoodTime.py - A script for Clueless To Coding - Python - Lesson 4"""

#Next Step: Well it is About Time
""" Add the actual timing functionality. This makes use of a function that is
   available from Python's standard labraries. But it is not 'built-in'. This
   means we will have to 'import' it. Importing other modules is quite common
   in most programming languages. Check out the instructions in the comment
   below.
   """

# When using a function from another module, it must first be imported. Remove
#  the triple quotes from the line below to import just the time() function
#  from the 'time' module. Then check out the other comments in the main program
#  section.
"""from time import time"""


#----> Functions Go Here:

# showTitle() - Displays the title
def showTitle():
    print("**********Lap Timer**********")
    print()

# showInstructions() - Displays the instructions
def showInstructions():
    print("Press Enter to record time for each lap.")
    print("Enter 'q' after last lap is recorded.")
    



#----> Main program starts here:

showTitle()

showInstructions()

# use input() to find out when the user is ready to start timing
input("Press ENTER to start timing")

#NEXT - Unquote the line below to record the base system time. This will be
#   subtracted from all the other recorded times to calculate the actual lap
#   times. These will all be in seconds.
"""startTime = time()"""

userInput = "" #userInput will be used to decide if the user is done timing

#NEXT - Unquote the line below to add a list variable to hold the lap times
"""lapTimes = []"""

while userInput == "": # IF the user just hits enter, the loop will contiune
    userInput = input("Press ENTER to record a lap time (or 'q' to quit)")
    #NEXT - Unquote the code below. It adds the code which records the lap times
    """thisTime = time()
    if userInput == "":
        lapTimes.append(thisTime - startTime)
        """

#NEXT - Unquote the code below that rpints out the list of lap times from this
#   session. Then save and run it.
"""for index in range(len(lapTimes)):
    print(index, lapTimes[index])
    """





#WHAT THIS SHOULD DO: At this point the program should record times and print
#   them out before exiting.

#NEXT STEP --> Open the file '05_GoodTime.py' and follow its instrctions.
