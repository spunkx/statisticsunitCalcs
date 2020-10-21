import math
print("cohen's d calculator")

choice = (input("Independent(I) or Paired(P)? ")).lower()

if choice == "i":
    mean1 = float(input("enter mean1 "))
    mean2 = float(input("enter mean2 "))
    
    samplesizeN1 = float(input("Enter sample size for first var "))
    samplesizeN2 = float(input("Enter sample size for next var "))

    SD1 = float(input("Enter SD for first var "))
    SD2 = float(input("Enter SD for next var "))

    pooledSD = math.sqrt((((samplesizeN1-1)*(SD1**2)) + ((samplesizeN2-1)*(SD2**2)))/(samplesizeN1 + samplesizeN2 - 2))
    
    d = (mean1 - mean2) / pooledSD
    
    print("pooled SD", pooledSD)
    print("Cohen's D ", d)

elif choice == "p":
    mean1 = float(input("enter mean1 "))
    mean2 = float(input("enter mean2 "))
    SD = float(input("enter SD "))

    d = (mean1 - mean2) / SD

    print("Cohen's D ", d)

