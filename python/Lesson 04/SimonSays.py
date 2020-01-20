#SimonSays.py
#A program that plays a call and response game using a list of strings.


#Constants

CALL_LIST = ["Simon Says jump!", "Grab, Your toes!", "simon says SHOUT!",
             "Giggle!!!", "SIMON says booga booga booga!",
             "SIMON SAYS whisper...", "simon says Sit Down"]

SIMON_SAYS = "SIMON SAYS"
SIMON_SAYS_LENGTH = len(SIMON_SAYS)

#Main Program

print("---------->SIMON SAYS<----------")
print()
print()

for thisCall in CALL_LIST:
    print("Call:", thisCall)

    if SIMON_SAYS in str.upper(thisCall):
        beginResponse = SIMON_SAYS_LENGTH
        print("\---->", thisCall[beginResponse:])
    print()
    print()
    
        
        
