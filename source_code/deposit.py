"""Establishes Deposit class that gets account to deposit and amount to deposit
    and adds amount to the balance of the chosen account.
    
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

from customer_console import CustomerConsole
import sqlite3

class Deposit:
    """Deposit class is child to CustomerConsole class."""

    def __init__(self, atm, account_destination):
        """Initiializes inheritance of values from CustomerConsole.
        """
        super().__init__(amount)
        self.account_destination = account_destination


    def get_customer_specifics(self):
        """Get account to send deposit and amount to send.
        returns: list with account and amount
        
        """
        prompt = "Select account to Deposit to:"
        self.account_destination = CustomerConsole.read_menu_choices(self, prompt, options)
        self.amount = CustomerConsole.read_amount(self)


    def complete_transaction(self, account_destination, amount):
        """Update balance for selected account with new balance of
        current balance plus deposit.
        
        Args
            str: account_destination
            float: amount
            
        """

        current_amount = 'SELECT balances FROM {}'.format(account_destination)
        current_amount += amount
        new_amount = 'UPDATE {} SET {}=?'.format(account_destination, balances)
        cursor.execute(new_amount, [current_amount])
        print(new_amount, [current_amount])


deposit = Deposit()
deposit.get_customer_speifics()
deposit.complete_transaction()
