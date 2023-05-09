"""Transaction class for ATM. Starts a Withdrawal, Deposit or Inquiry transaction."""

"""Transaction class for ATM. Starts a Withdrawal, Deposit or Inquiry transaction."""
from balances import Balance
from customer_console import CustomerConsole

class Transaction():
    """Starts a Withdrawal, Deposit or Inquiry transaction."""
    def __init__(self, atm, card, pin, serial_number):
        """Initializes transaction constructer
        
        Args:
            self: communicates with the atm module
            card (integer): the customer's card
            pin (integer): the PIN entered by the customer
            serial_number (integer): transaction serial number
    
        """
        self.atm = atm
        self.card = card
        self.pin = pin
        self.serial_number = serial_number + 1
        self.balance = 0

    def perform_transaction(self):
        """Asks user if they want to Withdraw, Deposit 
        or check balance and executes it.

        Returns: None
        """   
        prompt = 'Please select an option or press <enter> to go back.'
        options = ['Account Balance', 'Withdraw', 'Deposit']
        """ choice = self.atm.get_customer_console().read_menu_choices(self, prompt, options)"""
        my_console = CustomerConsole()
        self.pin = my_console.read_pin()
        
        choice = my_console.read_menu_choices(prompt, options)
        
        
        if choice == 1:
            print("Getting account balance.")
            self.balance = Balance(self.pin).account_balance()
            print(self.balance)
        elif choice == 2:
            print("Starting withdrawal.") # TEMPORARY
        elif choice == 3:
            print("Starting deposit.") # TEMPORARY


    def repeat_transaction(self):
        prompt = ("Would you like to perform another transaction? ")
        options = ['Yes', 'No']
        while True:
            choice = self.atm.get_customer_console().read_menu_choices(self, prompt, options)

            if choice is not None:
                return choice
