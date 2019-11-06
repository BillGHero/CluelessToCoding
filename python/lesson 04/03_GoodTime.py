""" 03_GoodTime.py - A script for Clueless To Coding - Python - Lesson 4"""

#Next Step: Postin a Sentinel
""" Next we will add a starting point for the timer and a while loop to capture
   each lap time. Check out the comments in the Main Program section for more.
   """


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

#remove the quotes from around the code below:
"""
# use input() to find out when the user is ready to start timing
input("Press ENTER to start timing")

userInput = "" #userInput will be used to decide if the user is done timing

while userInput == "": # IF the user just hits enter, the loop will contiune
    userInput = input("Press ENTER to record a lap time (or 'q' to quit)")
"""

#Notice that we are not actually looking for the letter 'q'. The loop will
#actually terminate as soon as the user enters any text at all.



#WHAT THIS SHOULD DO: At this point it should print out the title and the
#   instructions. Then it will enter a loop that continues as long as the user
#   only hits the ENTER key.

#NEXT STEP --> Open the file '04_GoodTime.py' and follow its instrctions.
