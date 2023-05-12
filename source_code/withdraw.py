import sqlite3
from balances import Balance
from customer_console import CustomerConsole


class Withdraw:
    """Deposit class is child to Transaction class."""

    def __init__(self, atm):
        """Initializes withdraw constructor."""
        self.atm = atm
        self.pin = pin


    def get_customer_specifics(self):
        """Get account to send deposit and amount to send.
        returns: list with account and amount
        
        """
        prompt = "Select account to Withdraw from:"
        options = ['checking', 'savings']
        choice = CustomerConsole.read_menu_choices(self.atm, prompt, options)
        if choice == 1:
            account_destination = options[choice - 1]
        else:
            account_destination = options[choice - 1]
            
        amount = CustomerConsole().read_amount()
        return [account_destination, amount]


    def complete_transaction(self, conn, account_destination, amount):
        """Update balance for selected account with new balance of
        current balance plus deposit.
        
        Args
            str: account_destination
            float: amount
            
        """
        conn = sqlite3.connect('atm_database.db')
        balances = Balance.get_balance(self)
        cursor = conn.cursor()
        current_amount = 'SELECT balances FROM Accounts WHERE AccountType={}'.format(account_destination)
        current_amount -= amount
        new_amount = 'UPDATE {} SET {}=?'.format(account_destination, balances)
        cursor.execute(new_amount, [current_amount])
        conn.close()
