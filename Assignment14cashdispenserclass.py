class CashDispenser:

    def __init__(self, cash_on_hand):
        self.cash_on_hand = cash_on_hand

    def set_initial_cash(self, money, initial_cash):
        """
        Sets the amount of cash initially on hand.
        """
        self.initial_cash = initial_cash
        return initial_cash

    def check_cash_on_hand(self, money, amount):
        """
        Checks if there is enough cash present to handle transation request.

        Args:
            self: referring to current object.
            money: amount of money present for transations.
            amount: amount user is requesting.

        Returns:
            boolean: True if amount requested is less than or
            equal to the amount of money present; False if not.
        """
        self.amount = amount
        if amount <= money:
            return True
        else:
            return False

    def dispense_cash(self, money, amount):
        """
        Dispenses cash to the customer.

        Args:
            self: referring to current object.
            amount: amount user is requesting
        """
        print('Dispensing', amount)
