# ========== SE T12 - Compulsory Task 1 ==========

# Imports.
import math

# Printing an introduction to the user.
print("""Choose either 'investment' or 'bond' from the menu below to proceed:\n
investment  -   to calculate the amount of interest you'll earn on your investment
bond        -   to calculate the amount you'll have to pay on a home loan\n""")

# Defining a flag variable to break out of the nested loops to come.
break_while = False

# Using a while loop to handle the user's calculator selection and also incorrect selections, in which case the user
# will be asked to re-enter their selection.
while True:
    selection = input("Please enter your choice here: ").upper()

    # Using an if-elif-else statement to request, in this instance, 'investment' inputs from the user.
    if selection == "INVESTMENT":
        deposit = float(input("How much money are you depositing? Enter: "))
        interest_rate = float(input("What is your estimated interest rate (%)? Enter: "))
        years = float(input("How many years do you plan on investing for? Enter: "))

        # Using a while loop and if-elif-else to select either the 'simple' or 'compound' formula. The amount is then
        # calculated and displayed. The user is asked again if an incorrect/unrecognisable input is entered.
        while True:
            interest = input("Do you want simple or compound interest? Enter 'simple' or 'compound': ").upper()
            if interest == "SIMPLE":
                total = round(deposit * (1 + interest_rate/100 * years), 2)

                break_while = True
                break
            elif interest == "COMPOUND":
                total = round(deposit * math.pow(1 + interest_rate/100, years), 2)
                break_while = True
                break
            else:
                print("Sorry, I didn't understand that. I am going to kindly ask again.")
        print(f"Based on what you told us, you will get back R{total}.")

        if break_while:
            break

    # Using an if-elif-else statement to request, in this instance, 'bond' inputs from the user. The amount repayable
    # per month is then calculated/displayed.
    elif selection == "BOND":
        house_value = float(input("What is your current house value? Enter: "))
        interest_rate = float(input("What is your estimated interest rate (%)? Enter: "))
        interest_rate = interest_rate/100
        months_repay = float(input("How many months do intend to take to repay the bond? Enter: "))

        total = round((interest_rate / 12) * house_value / (1 - (1 + (interest_rate / 12)) ** (months_repay * -1)), 2)
        print(f"Based on what you told us, each month you will have to repay R{total}.")
        break_while = True
    else:
        print("Sorry, I didn't understand that. I am going to kindly ask again.")
    if break_while:
        break
