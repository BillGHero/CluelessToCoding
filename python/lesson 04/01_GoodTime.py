""" 01_GoodTime.py - A script for Clueless To Coding - Python - Lesson 4"""

# Check out the above Docstring, it is the Docstring for this entire script
#  file.

#For this lesson we will build a 'Lap Timer' in a step-by-step fashion.
#  Each major step will start off with its own file. Each file is numbered
#  according to where it falls within the sequence. The only exception is the
#  final step. The final step file has no numeric prefix in its file name.

""" In many places it is more convenient to use these triple-quoted strings
   rather than a long run of single-line comments. So you will see these
   used throughout this lesson."""

""" This first file will introduce the use of 'functions'. Up to this point
   we have only used functions created by others. Those are the built-in
   functions such as print() and input() used in previous lesson. Starting
   here we will begin writing and using our own functions. """

""" Functions typically serve at least one two basic functions:
   1. Re-use of code that performs common operations
   2. Encapsulation of code for clarity and maintainability

   1. Re-usability - A function for some common operation can be written once
    and then called from wherever it is needed.

   2. Encapsulation - Functions are typically named according to what they
     do. This allows for a higher degree of clarity. In fact, sometimes
     a software engineer will use a function for single-use operations just
     to make what is being done more clear. Functions also allow the
     segregation of code so that later modification need only be done once.
     This makes code easier to maintain and debug.
     """

""" In python functions must first be defined, after which they can be called.
   Check out the function definition below:

def myFunction():
   print("This is my function.")
   print("Isn't it nice?")

   A function defintion starts with the Python keyword 'def'. The name of the
   function comes next. And next there is a set of parentheses. It is the
   parentheses which follow the name that tell Python it is a function. The
   final element is the colon. This colon tells Python that a code-block
   follows and it also tells Python that this is a function definition and
   not a function call.

   """

# showTitle() - Insert a function definition statement directly below these
#   comments. Name is 'showTitle'. Also notice the triple quotes directly
#   below? They enclose a set of print() calls. Remove the triple quotes
#   so that they become actual print() calls.
#--->Replace this line with the function definition statement<---
"""    print("**********Lap Timer**********")
    print()
   """


# Main program starts here:

#Notice the triple quotes below? They enclose a function call. Remove the
#triple quotes so that it becomes and executable statement. Then save and run
#this file.

"""showTitle()"""


#WHAT THIS SHOULD DO: At this point it should just print out the title of
#   program.

#NEXT STEP --> Open the file '02_GoodTime.py' and follow its instrctions.
