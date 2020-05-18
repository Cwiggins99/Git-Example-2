#Cameron Wiggins
#05/07/20
#First Project in Python

#Declaring the variables.
retirementSelection = 0.00
retirementDeduction = 0.02
grossPay = 0.00
netPay = 0.00
shift = 0.00
hours = 0.00
payRate = 0.00

#Setting the if statement, equations, and output together.

shift = int(input("Enter the shift that you work (1-Day 2-Afternoon 3-Night: "))
hours = float(input("Enter the amount of hours you worked: "))
if hours > 40:
    print("Invalid entry. Hours over 40 hours are considered overtime.: ")
elif shift > 3:
    print("Invalid entry.")
elif shift < 0:
    print("Invalid entry.")
elif shift == 1:
    payRate = 18.50
    grossPay = payRate * hours
    netPay = payRate * hours
    retirementDeduction = 0.00
    print("Hourly rate: ", payRate, "\nGross pay: ", grossPay, "\nRetirement deduction: ", "{:.2f}".format(retirementDeduction), "\nNet pay: ", netPay)
elif shift == 2:
    retirementSelection = int(input("Would you like to contribute to your retirement fund? (1-Yes 2-No): "))
    if retirementSelection == 1:
        payRate = 20.00
        grossPay = (payRate * hours) - (payRate * hours * retirementDeduction)
        netPay = payRate * hours
        retirementDeduction = netPay - grossPay
        print("Hourly rate: ", payRate, "\nGross pay: ", grossPay, "\nRetirement deduction: ", "{:.2f}".format(retirementDeduction), "\nNet pay: ", netPay)
    if retirementSelection == 2:
        payRate = 20.00
        grossPay = (payRate * hours)
        netPay = payRate * hours
        retirementDeduction = 0.00
        print("Hourly rate: ", payRate, "\nGross pay: ", grossPay, "\nRetirement deduction: ", "{:.2f}".format(retirementDeduction), "\nNet pay: ", netPay)
elif shift == 3:
    retirementSelection = int(input("Would you like to contribute to your retirement fund? (1-Yes 2-No): "))
    if retirementSelection == 1:
        payRate = 23.50
        grossPay = (payRate * hours) - (payRate * hours * retirementDeduction)
        netPay = payRate * hours
        retirementDeduction = netPay - grossPay
        print("Hourly rate: ", payRate, "\nGross pay: ", grossPay, "\nRetirement deduction: ", "{:.2f}".format(retirementDeduction), "\nNet pay: ", netPay,)
    if retirementSelection == 2:
        payRate = 23.50
        grossPay = (payRate * hours)
        netPay = payRate * hours
        retirementDeduction = 0.00
        print("Hourly rate: ", payRate, "\nGross pay: ", grossPay, "\nRetirement deduction: ", "{:.2f}".format(retirementDeduction), "\nNet pay: ", netPay)


     

    
    