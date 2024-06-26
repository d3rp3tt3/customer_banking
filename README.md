# Customer Banking Assignment

This repo shows a simple Python program for modeling the potential earned interest for a savings account and for a CD.

## Purpose

The project presents a potential solution for the UNC-Chapel Hill AI bootcamp assignment for the Module 3 Challenge.

## Running the solution

At the Command Line: Run `python3 customer_banking.py`

The program will prompt you to enter values for the current balances for a hypothetical savings and CD account, the APRs for their interest, and the number of months to calculate the new balance.

## Files in this repository

### Account.py

The program's primary class outlines the core functions of a customer's account.

* Parameters: `balance` and `interest`
* Methods
  * `set_balance`: Float. Sets the balance for the account.
  * `set_interest`: Float. Sets the interest rate for the account.

### cd_account.py

This file defines the `reate_cd_account` function and includes methods for calculating the potential earned interest for a CD.

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

This file executes the program and includes three functions:

* `get_float_input` takes in two parameters: the user's input as a float and the minimum value that the input should accept. This ensures users cannot enter 0, a negative number, or a character.
* `get_int_input` takes in two parameters: the user's input as an int and the minimum value that the input should accept. This ensures users cannot enter 0, a negative number, or a character.
* The `main` function includes code to prompt the user to input values to calculate the potential earned interest and final balances for a savings account and a CD. The inputs call the `get_float_input` and `get_int_input` functions, passing the `prompt` input text and the `min_value` arguments.

While entering 0 is technically permitted, the program makes no sense if we don't require a value greater than 0. We're calculating interest.

**Note**
I chatted with Copilot to learn how to add input validation to my inputs and added this to my code after further study.
