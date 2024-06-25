# Customer Banking Assignment

This repo shows a simple Python program for modeling the potential earned interest for a savings account and for a CD.

## Purpose

The project presents a potential solution for the UNC-Chapel Hill AI bootcamp assignment for the Module 3 Challenge.

## Files in this repository

### Account.py

The program's primary class outlines the core functions of a customer's account.

* Parameters: `balance` and `interest`
* Methods
  * `set_balance`: Float. Sets the balance for the account.
  * `set_interest`: Float. Sets the interest rate for the account.

### cd_account.py

Inherits from Account.py. This file includes functions for calculating the potential earned interest for a CD.

* Parameters: `balance (float)`, `interest_rate (float)`, `months (float)`
* Returns:
  * `cd_balance (float)`: The updated CD account balance after adding the interest earned.
  * `cd_interest_earned (float)`: The interest earned.
  * `cd_months (int)`: The number of months used to calculate the new balance.
  
### savings_account.py

This file defines the `create_savings_account` function, which includes methods for calculating the potential earned interest for a savings account.

* Parameters: `balance (float)`, `interest_rate (float)`, `months (float)`
* Returns
  * `savings_balance (float)`: The updated savings account balance after adding the interest earned.
  * `interest_earned (float)`: The earned interest.
  * `savings_months (int)`: The number of months used to calculate the savings_balance.

### customer_banking.py

This file executes the program and includes the `main` function. It includes code to prompt the user to input values to calculate the potential earned interest and final balances for a savings account and a CD.

## Running the solution

At the Command Line: Run `python3 customer_banking.py`

The program will prompt you to enter values for the current balances for a hypothetical savings and CD account, the APRs for their interest, and the number of months to calculate the new balance.
