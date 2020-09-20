import math
#add validiity check
#add estimation error calcualtor

totalN = float(input("enter the total n: ")) 
check = input("Enter ^p? y/n: ")
if(check == 'n'):
    sampleX = float(input("enter the sample size X: "))
    proportion = sampleX/totalN
elif(check == 'y'):
    proportion = float(input("enter the proportion: "))

intervalK = float(input("enter the interval k: "))


floor = proportion - (intervalK * math.sqrt((proportion*(1-proportion))/totalN))
ceiling = proportion + (intervalK * math.sqrt((proportion*(1-proportion))/totalN))

estimationError = (ceiling - floor) / 2

check2 = input("do you wish to check population sample at a specific interval y/n? ")
if(check2 == "y"):
    desiredConfidence = float(input("enter the confidence interval: "))
    newsampleSize = proportion*(1 - proportion) * ((intervalK/desiredConfidence)**2)
    print("Sample size at inverval",desiredConfidence,"is",newsampleSize)

print("estimation error:", estimationError)
print("sample proporiton: ", proportion)
print(floor, "< p  <", ceiling)
