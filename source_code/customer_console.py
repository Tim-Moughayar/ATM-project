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
from gui_class import Window


class CustomerConsole():
    """Customer console class for ATM."""
    def __init__(self):
        """Costumer console constructor"""
        # self.gui = gui

    def read_pin(self):
        """Gets user's pin number
        Returns:
            integer: Customer pin number
        """
        while True:
            try:
                # gui = Window()
                # update_text = 'Please enter your pin:'
                # Window.update_output_box(self.gui, update_text)
                # pin = Window.get_input_box(self.gui)
                # # hidden_pin = "*" * len(pin)
                # # gui.mainloop()
                # print(pin)
                # print(type(pin))
                pin = getpass.getpass()
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
        amount = f'{float(amount):.2f}'

        return amount

    def display(self, statement):
        """Displays given statement.
        Returns: None
        """
        # Window.update_output_box(statement)
        # This will be changed to gui display

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
