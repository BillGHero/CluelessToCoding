userInput = input("Enter a temperature in Farenheit:")

floatInput = float(userInput)

celsius = (floatInput - 32) * 5 / 9

print(floatInput, "degF =", celsius, "deg C.")
