"""Transaction class for ATM. Starts a Withdrawal, Deposit or Inquiry transaction.
Input:

Output:
    
References: 

"""
from atm import Atm


class Transaction():
    """Starts a Withdrawal, Deposit or Inquiry transaction."""
    def __init__(self, atm, card, pin, serial_number):
        """Initializes transaction constructer
        
        Args:
            self: communicates with the atm module
            card (integer): the customer's card
            pin (integer): the PIN entered by the customer
    
        """
        self.atm = atm
        self.card = card
        self.serial_number = serial_number + 1
        # self.balance = Balances()

    def perform_transaction(self):
        Atm.get_customer_console(self).display
