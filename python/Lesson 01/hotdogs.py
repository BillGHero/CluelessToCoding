print("Hot Dogs!")

numHotDogs = 35
print("we have", numHotDogs, "hot dogs.")

weightHotDogOz = 1.5
print("These hot dogs weigh", weightHotDogOz, "ounces.")

brand_hotDog = "Piggy Toes"
print("They are", brand_hotDog, "brand hot dogs.")

print()
numHotDogsPerPack = 12
costPerHotDogPack = 3.65

costPerHotDog = costPerHotDogPack / numHotDogsPerPack

print("These hot dogs cost $", costPerHotDogPack, "per pack.")
print("And with", numHotDogsPerPack, "per pack they cost $", costPerHotDog, "each.")

print()
numBunsPerPack = 12
costPerBunPack = 1.49

costPerBun = costPerBunPack / numBunsPerPack

print("The buns cost $", costPerBunPack, "per pack.")
print("And with", numBunsPerPack, "buns per pack, the cost $", costPerBun, "each.")

totalCostPerHotDog = costPerBun + costPerHotDog

markup = 0.33

markupCost = markup * totalCostPerHotDog
pricePerHotDog = markupCost + totalCostPerHotDog

print()
print("The final price per hot dog is", pricePerHotDog)


