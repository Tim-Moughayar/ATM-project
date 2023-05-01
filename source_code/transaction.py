"""Transaction class for ATM. Starts a Withdrawal, Deposit or Inquiry transaction."""

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
        # self.balance = Balances()

    def perform_transaction(self):
        """Asks user if they want to Withdraw, Deposit 
        or check balance and executes it.

        Returns: None
        """
        
        while True:
            prompt = 'Please select an option'
            options = ['Account Balance', 'Withdraw', 'Deposit']
            choice = self.atm.get_customer_console().read_menu_choices(self, prompt, options)

            if choice == 1:
                print("Getting account balance.") # TEMPORARY
            elif choice == 2:
                print("Starting withdrawal.") # TEMPORARY
            elif choice == 3:
                print("Starting deposit.") # TEMPORARY

            prompt = ("Would you like to perform another transaction?")
            options = ['Yes', 'No']
            choice = self.atm.get_customer_console().read_menu_choices(self, prompt, options)

            if choice == 2:
                break
