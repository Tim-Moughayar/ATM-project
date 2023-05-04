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
        while True:
            try:
                pin = getpass.getpass("Please enter your pin:")
                pin = int(pin)
                break
            except ValueError:
                pass
        return pin

    def read_amount(self):
        """Gets user's dollar amount
        Returns:
            float: User's desired dollar amount
        """
        amount = input("Please enter the desired $ amount.")
        amount = float('%.2f', amount)

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

            print(prompt)

            try:
                for num, option in enumerate(options):
                    print(f"{num + 1}: {option}")

                choice = input()
                choice = int(choice)

                if 1 <= choice <= len(options):
                    print()
                    return choice

            except ValueError:
                if choice == "":
                    return None
