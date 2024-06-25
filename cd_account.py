"""Import the Account class from the Account.py file.

In the cd_account.py file, you will import the 
Account class and create a create_cd_account function 
that will create a CD account instance, 
calculate the interest earned based on user input, 
update the account balance with the earned interest, 
and return the updated balance and interest earned.
"""
# ADD YOUR CODE HERE
from account import Account


def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        cd_balance (float): The updated CD account balance after adding the interest earned.
        cd_interest_earned (float): The interest earned.
        cd_months (int): The number of months used to calculate the new balance.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    cd_interest = Account(balance, 0)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    cd_months = months
    cd_interest_earned = balance * (interest_rate/100 * cd_months/12)

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    cd_balance = balance + cd_interest_earned

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_interest.set_balance = cd_balance

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_interest.set_interest = cd_interest_earned

    # Return the updated balance and interest earned.
    return cd_balance, cd_interest_earned, cd_months
