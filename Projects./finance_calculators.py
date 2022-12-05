##Importing math module##
import math

##Printing information for user##
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n\
investment - to calculate the amount of interest you'll earn on your investment\n\
bond       - to calculate the amount you'll have to pay on a home loan")

calc_type = input().lower()
##Converting all to lower case to account for any caps in user's response##

##Calculations for investment##
if calc_type == 'investment':
    deposit = float(input("Please input the amount you wish to deposit: "))
    interest_rate = float(input("Please input the interest rate (%): "))
    years = int(input("Please input the number of years you plan on investing for: "))
    interest = input("Do you wish to use 'simple' or 'compound' interest? ").lower()
    ##If/else to split for individual equations based on interest type##
    if interest == 'simple':
        total = deposit * (1 + (interest_rate / 100) * years)
        print(f"Total after {years} years: {total}.")
    elif interest == 'compound':
        total = deposit * math.pow(1 + (interest_rate / 100), years)
        print(f"Total after {years} years: {total}.")
    else:
        ##Included else to account for instance where invalid answer given##
        print('Please enter either "simple" or "compound" for interest.')

##Bond section##
elif calc_type == 'bond':
    ##Prompting user for required information##
    curr_val = int(input("Please enter the current value of the house: "))
    interest_rate = float(input("Please enter the interest rate: "))
    months_to_repay = int(input("Please enter the number of months you plan to repay the bond over: "))

    ##Performing calculations##
    monthly_interest = interest_rate / 12
    per_month = (curr_val * monthly_interest) / (1 - (1 + monthly_interest) ** (-months_to_repay))
    print(f"You will have to repay {per_month} per month.")

##Invalid option chosen##
else:
    print("Error: Invalid option selected.")