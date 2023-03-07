import math

# This code allows users to calculate the amount of money they will either receive or need to pay back.
# First, the users see their options displayed.
print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")
print("investment\t-\tto calculate the amount of interest you'll earn on your investment")
print("bond\t\t-\tto calculate the amount you'll have to pay on a home loan\n")

# Then user input is required with their choice of calculation
# While loop is used to ensure that the correct input is entered
while True:
    calculation_type = input("Please enter either 'investment' or 'bond': ")
    calculation_type = calculation_type.lower()
    if calculation_type == 'investment' or calculation_type == 'bond':
        break
    else:
        print("Invalid input - Please enter either 'investment' or 'bond': ")

# If/ else statements are used to request input according to the calculation requred and
# calculate according to the conditions and formulas provided:
if calculation_type == 'investment':
    deposit = float(input("Please enter the amount you would like to deposit £: "))
    interest_rate = float(input("Please enter interest rate percentage (do not include '%' symbol): "))
    years = int(input("Please enter the number of years you plan to invest for: "))
    while True:
        interest = input ("Please enter 'simple' for simple rate or 'compound' for compound rate: ")
        interest = interest.lower()
        if interest == "simple" or interest == "compound":
            break
        else:
            print("Incorrect input - Please enter either 'simple' or 'compound': ")
    r = interest_rate / 100
    if interest == 'simple':
        payback = deposit * (1 + (r * years))
    else:
        payback = deposit * math.pow ((1 + r), years)
    print(f"in {years} years you will receive the total of {round(payback, 2)}")
else:
    house_value = float(input("Please enter the present value of the house: "))
    interest_rate = float(input("Please enter interest rate (e.g. 7): "))
    months = int(input("Please enter number of months you are planning to take to repay the bond (e.g. 120): "))
    r = interest_rate/100
    i = r / 12
    repayment = (i * house_value)/(1-math.pow(1 + i,-months))
    print(f"You will have to repay £{round(repayment, 2)} each month")