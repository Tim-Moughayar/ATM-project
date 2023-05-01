"""Customer console class for ATM.

Input:
    Customer Pin
    Customer money amount
    Customer menu choice

Output:
    Display message to customer

References: 
    * https://www.math-cs.gordon.edu/courses/cs211/ATMExample/javadoc/atm/physical/CustomerConsole.html

Created by Frank Boxenbaum
"""

import getpass


class CustomerConsole():
    """Customer console class for ATM."""
    def __init__(self):
        """Creates a customer console

        Args:
            read_pin (integer): Customer pin number
            read_menu_choice (integer): Customer menu choice

        Returns:
            read_amount (float): Customer entered money amount
        """

        self._read_pin = None
        self._read_menu_choice = None
        self._read_amount = None
        self._display = None

    def read_pin(self):
        """Gets user's pin number

        Returns:
            integer: Customer pin number

        """
        print('Please insert your card')
        pin = getpass.getpass("Please enter your pin:")
        pin = int(pin)

        return pin

    def read_amount(self):
        """Gets user's dollar amount

        Returns:
            float: User's desired dollar amount

        """
        amount = input("Please enter the desired $ amount.")
        amount = float(amount)

        return amount

    def display(self):
        """Displays the menu of ATM options.

        Returns: None

        """

        print('Please select an option')
        print('1: Account Balance')
        print('2: Withdraw')
        print('3: Deposit')

    def read_menu_choices(self):
        """Gets user's menu choice.

        Returns:
            integer: User's desired menu choice

        """
        choice = input()
        choice = int(choice)
        if choice

        return choice
