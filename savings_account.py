"""Import the Account class from the Account.py file.

In the savings_account.py file, you will import the 
Account class and create a create_savings_account 
function that will create a savings account instance, 
calculate the interest earned based on user input, 
update the account balance with the earned interest, 
and return the updated balance and interest earned.
"""
# ADD YOUR CODE HERE
from account import Account

# Define a function for the Savings Account


def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        savings_balance (float): The updated savings account balance after interest.
        interest_earned (float): The earned interest.
        savings_months (int): The number of months used to calculate the savings_balance.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    my_account = Account(balance, 0)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    savings_months = months
    interest_earned = balance * (interest_rate/100 * savings_months/12)

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    savings_balance = balance + interest_earned

    # Pass the updated_balance to the set balance method
    # using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    my_account.set_balance = savings_balance

    # Pass the interest_earned to the set interest method
    # using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    my_account.set_interest = interest_earned

    # Return the updated balance and interest earned.
    return savings_balance, interest_earned, savings_months
