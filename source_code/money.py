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

    def __init__(self, dollars, cents, amount_to_add, amount_to_subtract, compare_to):
        """Money class constructor.

        Args:
            dollars: int dollar amount.
            cents: int cent amount.
            amount_to_add: amount to add to cents.
            amount_to_subtract: amount to subtract from cents.
            compare_to: amount to compare 

        """
        self.dollars = dollars
        self.cents = cents
        self.amount_to_add = amount_to_add
        self.amount_to_subtract = amount_to_subtract
        self.compare_to = compare_to
        self.money = 100 * dollars + cents

    def to_string(self, money):
        """Creates string representation of money amount.

        Returns:
            string: String representation of money amount
        """
        string_amount = money / 100
        string_amount = float('%.2f', string_amount)
        string_amount = "$" + str(string_amount)

        return string_amount

    def add(self):
        """Adds an amount of money"""
        self.cents += self.amount_to_add

    def subtract(self, amount):
        """Subtracts an amount of money"""
        if amount <= self.amount_to_subtract:
            self.cents -= self.amount_to_subtract

    def less_equal(self):
        """Compares two money amounts"""
        less_equal = self.cents <= self.compare_to
        if less_equal is True:
            return True
