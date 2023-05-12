"""Transaction class for ATM. Starts a Withdrawal, Deposit or Inquiry transaction."""
from balances import Balance
from customer_console import CustomerConsole
from transfer import Transfer

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

    def perform_transaction(self):
        """Asks user if they want to Withdraw, Deposit 
        or check balance and executes it.

        Returns: None
        """   
        prompt = 'Please select an option or press <enter> to go back.'
        options = ['Account Balance', 'Withdraw', 'Deposit', 'Transfer']
        """ choice = self.atm.get_customer_console().read_menu_choices(self, prompt, options)"""
        my_console = CustomerConsole()
        self.pin = my_console.read_pin()
        
        choice = my_console.read_menu_choices(prompt, options)
        
        
        if choice == 1:
            print("Getting account balance.")
            balance = Balance(self.pin).account_balance
            print("Balance: " + str(balance))
        elif choice == 2:
            print("Starting withdrawal.") # TEMPORARY
        elif choice == 3:
            print("Starting deposit.") # TEMPORARY
        elif choice == 4:
            from_pin = my_console.prompt_transaction_input("Which account do you want to transfer from?")
            to_pin = my_console.prompt_transaction_input("Which account do you want to transfer to?")
            transfer_amount = my_console.prompt_transaction_input("How much would you like to transfer?")
            print("Starting tranfer")
            my_transfer = Transfer(from_pin, to_pin, transfer_amount)
            my_transfer.update_accounts()
            from_balance = Balance(from_pin).account_balance()
            print("Account Balance for " + str(from_pin) + ": " + str(from_balance))
            to_balance = Balance(to_pin).account_balance()
            print("Account Balance for " + str(to_pin) + ": " + str(to_balance))
            
            
    def repeat_transaction(self):
        prompt = ("Would you like to perform another transaction? ")
        options = ['Yes', 'No']
        while True:
            choice = self.atm.get_customer_console().read_menu_choices(self, prompt, options)

            if choice is not None:
                return choice