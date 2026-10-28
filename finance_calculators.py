import math

# Display the calculator menu and get the user's selection.
calculation_type = input(
    "Investment - to calculate the amount of interest you'll earn "
    "on your investment.\n"
    "Bond - to calculate the amount you'll have to pay on a home loan.\n\n"
    'Enter either "investment" or "bond" from the menu above to proceed: ').lower()

# Calculate the final value of an investment.
if calculation_type == "investment":
    deposit_amount = float(input("Enter the amount of money you are depositing: "))
    annual_interest_rate = float(input("Enter the annual interest rate as a percentage: "))
    investment_years = int(input("Enter the number of years you plan to invest: "))

    interest = input('Enter either "simple" or "compound" interest: ').lower()

    # Convert the percentage entered by the user into a decimal.
    interest_rate_decimal = annual_interest_rate / 100

    if interest == "simple":
        final_amount = deposit_amount * (1 + interest_rate_decimal * investment_years)
        print(f"Total investment value: R{final_amount:.2f}")

    elif interest == "compound":
        final_amount = deposit_amount * math.pow(1 + interest_rate_decimal, investment_years)
        print(f"Total investment value: R{final_amount:.2f}")

    else:
        print('Invalid interest type. Please enter "simple" or "compound".')

# Calculate the monthly repayment on a home loan.
elif calculation_type == "bond":
    house_value = float(input("Enter the present value of the house: "))
    annual_interest_rate = float(input("Enter the annual interest rate as a percentage: "))
    repayment_months = int(input("Enter the number of months over which the bond will be repaid: "))

    # Convert the annual percentage rate into a monthly decimal rate.
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    monthly_repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** (-repayment_months))
    print(f"Monthly bond repayment: R{monthly_repayment:.2f}")

else:
    print('Invalid selection. Please enter either "investment" or "bond".')

#I was guided by chatGPT to create this code.