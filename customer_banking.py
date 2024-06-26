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
from savings_account import create_savings_account
from cd_account import create_cd_account

# The following two functions provide input validation
def get_float_input(prompt, min_value=None):
    """Accepts an input and throws an error if it's not a float 

    Returns:
        prompt (float): Returns the float format of the user's input
    """
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print("Please enter a value greater than 0.01")
                continue
            return value
        except ValueError:
            print("Invalid option. Please enter a number.")

def get_int_input(prompt, min_value=None):
    """Accepts an input and throws an error if it's not an int 

    Returns:
        prompt (int): Returns the int format of the user's input
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = get_float_input("What is the beginning savings balance? ", 0.01)
    savings_interest = get_float_input("What is the savings interest rate? ", 0.01)
    savings_maturity = get_int_input("Over how many months will interest accrue? ", 1)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned, savings_months = create_savings_account(
        savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with
    # interest earned for the given months.
    print("-" * 42)
    print(f"The interest is ${interest_earned:,.2f} over {savings_months} month(s)")
    print(f"The updated balance for the savings account will be ${updated_savings_balance:,.2f}")
    print(" " * 42)
    print("-" * 42)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = get_float_input("What is the CD balance? ", 0.01)
    cd_interest = get_float_input("What is the CD's APR? ", 0.01)
    cd_maturity = get_int_input("Over how many months will the CD mature? ", 1)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_earned_interest, cd_months = create_cd_account(
        cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance
    # with interest earned for the given months.
    print("-" * 42)
    print(f"The interest earned for the CD is ${cd_earned_interest:,.2f} over {cd_months} month(s)")
    print(f"The updated CD balance is ${updated_cd_balance:,.2f}")
    print(" " * 42)


if __name__ == "__main__":
    main()
