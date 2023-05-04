"""Money class for ATM.
    Input:
        add
        compare
        subtract
        to_string
    Output:
        Representation for money amounts
    References: 
        * https://www.math-cs.gordon.edu/courses/cs211/ATMExample/ClassLinks.html#Money
    Created by Frank Boxenbaum, Timothy El Moughayar, and Michael Radcliffe
    """
class Money:
    """Money class for ATM."""

    def __init__(self, dollars, cents, amount_to_add, amount_to_subtract):
        """Money class constructor.

        Args:
            dollars: int dollar amount.
            cents: int cent amount.

        """
        self.dollars = dollars
        self.cents = cents
        self.amount_to_add = amount_to_add
        self.amount_to_subtract = amount_to_subtract
        self.compare_to = compare_to

    def to_string(self, cents):
        """Creates string representation of money amount.

        Returns:
            string: String representation of money amount
        """
        string_amount = "$" + \
            cents/100 + (cents %100 >= 10  + "." + cents % 100 + ".0" + cents % 100)

        return string_amount

    def add(self):
        """Adds an amount of money"""
        self.cents += self.amount_to_add.cents

    def subtract(self, amount):
        """Subtracts an amount of money"""
        if amount <= self.amount_to_subtract:
            self.cents -= self.amount_to_subtract.cents

    def less_equal(self):
        """Compares two money amounts"""
        less_equal = self.cents <= self.compare_to.cents

        return less_equal
