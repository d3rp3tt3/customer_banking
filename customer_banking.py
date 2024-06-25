"""
In the customer_banking.py file, you will import
the create_savings_account and create_cd_account
functions, then create a main function that prompts
the user to enter the savings and CD account details,
call the corresponding functions to calculate the
interest earned and update the balances, and
display the results.
"""

# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    savings_balance = float(
        input("What is the balance of the savings account? "))
    savings_interest = float(input("What is the savings interest rate? "))
    savings_maturity = int(
        input("Over how many months would you like to calculate the earned interest ? "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned, savings_months = create_savings_account(
        savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with
    # interest earned for the given months.
    # ADD YOUR CODE HERE
    print("-" * 42)
    print("-" * 42)
    print(f"The account will earn ${interest_earned:,.2f} of interest over the period of {savings_months} months")
    print(f"The updated balance for the savings account will be ${updated_savings_balance:,.2f}")
    print("-" * 42)
    print(" " * 42)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("What is the CD balance? "))
    cd_interest = float(input("What is the CD's APR? "))
    cd_maturity = int(input("Over how many months will the CD mature? "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_earned_interest, cd_months = create_cd_account(
        cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance
    # with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("-" * 42)
    print(f"The interest earned for the CD is ${cd_earned_interest:,.2f}")
    print(f"The updated CD balance is ${updated_cd_balance:,.2f}")
    print("This is over a time period of", cd_months, "month(s)")
    print(" " * 42)


if __name__ == "__main__":
    main()
