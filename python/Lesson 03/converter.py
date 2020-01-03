userInput = input("Enter a temperature in Farenheit:")

floatInput = float(userInput)

celsius = (floatInput - 32) * 5 / 9

print(floatInput, "degF =", celsius, "deg C.")

if floatInput >= 85:
    print(floatInput, "degrees. Wow that's hot!")
elif floatInput <= 49:
    print(floatInput, "degrees is too colde for me!")
else:
    print(floatInput, "degrees is nice.")
