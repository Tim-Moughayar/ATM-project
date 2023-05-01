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
        """Costumer console constructor"""

    def read_pin(self):
        """Gets user's pin number
        Returns:
            integer: Customer pin number
        """
        # print('Please insert your card')
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

    def display(self, statement):
        """Displays given statement.
        Returns: None
        """
        print(statement)

    def read_menu_choices(self, prompt, options):
        """Displays options and gets choice.

        Args:
            options (list): list of tables from database
            prompt (str): prompt for choice

        Returns:
            integer: User's desired menu choice

        """
        while True:
            try:
                print(prompt)
                
                for num, option in enumerate(options):
                    print(f"{num + 1}: {option}")

                choice = input()
                choice = int(choice)

                if 1 <= choice <= len(options):
                    print()
                    return choice
                print(f"{choice} is not one of the options.\n")

            except ValueError:
                print(f"ValueError: {choice} is not a valid choice.\n")
