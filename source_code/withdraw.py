"""Establishes Withdraw class that gets account to withdraw amount from and amount to withdraw
    and subbtracts amount from the balance of the chosen account.
    
    Input:
    amount to deposit
    account choice
    
    returns:
    updated balance
    
    References:
        * https://www.geeksforgeeks.org/python-call-parent-class-method/
        * https://www.w3schools.com/python/python_inheritance.asp#:~:text=Inheritance
    %20allows%20us%20to%20define,class%2C%20also%20called%20derived%20class.
        * https://www.math-cs.gordon.edu/courses/cs211/ATMExample/source/atm/transaction/Deposit.java
        * https://www.geeksforgeeks.org/types-of-inheritance-python/
"""
import sqlite3
from balances import Balance
from customer_console import CustomerConsole


class Withdraw:
    """Deposit class is child to Transaction class."""

    def __init__(self, atm):
        """Initializes withdraw constructor."""
        
        self.atm = atm


    def get_customer_specifics(self):
        """Get account to send deposit and amount to send.
        returns: list with account and amount
        
        """
        
        prompt = "Select account to withdraw from:"
        options = ['checking', 'savings']
        account_destination = CustomerConsole().read_menu_choices(prompt, options)
        amount = CustomerConsole().read_amount(self)
        return [account_destination, amount]


    def complete_transaction(self, conn, account_destination, amount):
        """Update balance for selected account with new balance of
        current balance plus deposit.
        
        Args
            str: account_destination
            float: amount
            
        """

        balances = Balance().get_balances(self)
        cursor = conn.cursor()
        current_amount = 'SELECT balances FROM {}'.format(account_destination)
        current_amount -= amount
        new_amount = 'UPDATE {} SET {}=?'.format(account_destination, balances)
        cursor.execute(new_amount, [current_amount])
        print(new_amount, [current_amount])


conn = sqlite3.connect('databasename.db')
withdraw = Withdraw()
withdraw.get_customer_specifics()
withdraw.complete_transaction()
