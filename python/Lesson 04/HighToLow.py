#HighToLow.py
#A program which inputs several numbers from the user and then sorts them high to low.


#Variables

#List to hold the original values
originalList = []

#List to hold the sorted values
sortedList = []


#Let the user know what this program does
print("---------->Sort It Out<----------")
print()
print("This program allows you to type in some numbers, one at a time,")
print(" and then sorts those numbers from highest to lowest.")
print()



#Loop to input several numbers from the user and put them into a list
#While loop that uses a boolean variable to control whether or not to continue
#Have the user keep typing numbers in, and then just press the enter key without any
#input to indicate they are done. Use a boolean variable to keep track of
#whether or not the loop should continue.
print("enter as many numbers as you like, integers only please.")
print("Press the ENTER key without any input to indicate you are done.")

shouldContinue = True
while shouldContinue:
    userInput = input("ENTER by itself to quit:")
    if userInput == "":
        shouldContinue = False
    else:
        newInt = int(userInput)
        originalList += [newInt]


#Loop to display all the numbers in the order they were entered
#While loop that uses 'True' and then 'break' to stop execution
#Use an index variable to access each element of the original list and
#increment it within a while loop, adding each element to a string. Print the
#string after the while loop is complete. Also, use an if structure to ensure that if
#the list is empty some message is displayed and that all the baove is bypassed
#altogether
print()
print()
print("So, here is what you entered:")

if len(originalList) < 1:
    print("--Youd didn't enter any numbers...")
else:
    neatLine = ""
    index = 0
    while True:
        neatLine += " > " + str(originalList[index])
        index += 1
        if index >= len(originalList):
            break
    print(neatLine)
    



#Loop to sort the list high to low
#Nested while loops where the outer loop uses the length() function to decide
#  when it is time to stop
#There should be two loops, one nested within the other. The inner loop will
# pass through the original list and identify the current highest value.
#The outer loop will 'pop' the highest value from the original list and
#'append' it to the sorted list. It will keep going until all the numbers
# are transferred over to the sorted list.
while len(originalList) > 0:
    highestIndex = 0
    index = 0
    while index < len(originalList):
        if originalList[index] > originalList[highestIndex]:
            highestIndex = index
        index += 1
    #Here we use two new list functions
    sortedList.append( originalList.pop(highestIndex) )
    
    



#Loop to display the sorted list
#While loop that uses 'continue' to bypass a section of the ocde until the last iteration
#Use an index variable to access each element of the original list and
#increment it within a while loop to add each elemnt to a string. Also, ensure that
#the loop doesn't execute if the sorted list is empty.
#Also, cause the while loop to print out the string when it is finally full.
index = 0
neatLine = ""
while index < len(sortedList):
    neatLine += str(sortedList[index])
    index += 1
    if index < len(sortedList):
        neatLine += ", "
        continue
    print()
    print("When the numbers are sorted from high to low, they look like this:")
    print(neatLine)
    
    
