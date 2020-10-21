import math
#add k calc later please

xBar = float(input("enter X bar: "))
kVal = float(input("enter k value: "))
standDev = float(input("enter pop or sample S.D.: "))
sampSize = float(input("enter sample size: "))


floor = xBar - (kVal*(standDev/math.sqrt(sampSize)))
ceil = xBar + (kVal*(standDev/math.sqrt(sampSize)))

print(floor, "< p <", ceil)
