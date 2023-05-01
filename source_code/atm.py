from customer_console import CustomerConsole
from transaction import Transaction


class Atm:
    """ATM class for ATM software"""

    def __init__(self, id, place, bank_name):
        """Creates an ATM object.

        Args:
            id (int): Id number for the ATM. 
            place (str): Physical location of this ATM
            bank_name (str): Name of the bank owning this ATM

        """
        self.id = id
        self.place = place
        self.bank_name = bank_name

        # Create objects corresponding to component parts
        CustomerConsole()

    def run_atm(self):
        """Runs the ATM."""

        cash_in_atm = 10000
        print("Sending cash_in_atm to cash dispenser module. "       # TEMPORARY
              f"Amount: ${cash_in_atm}")
        # CashDispenser.set_initial_cash(cash_in_atm)

        # gets pin from user
        pin = CustomerConsole.read_pin(self)
        card = 5425233430109903

        transaction = Transaction(self, card, pin, 1)
        Transaction.perform_transaction(transaction)

    def get_ID(self):
        return self.id

    def get_place(self):
        return self.place

    def get_bank_name(self):
        return self.bank_name

    def get_customer_console(self):
        return CustomerConsole

    def test(self):
        """Tests all class properties and methods.

        Returns:
            True: If all tests successful.

        Raises:
            AssertionError: If a test fails.

        """
        atm = Atm(2023425, 'Lobby', 'Harper Bank')
        assert atm.get_ID() == 2023425
        assert atm.get_place() == 'Lobby'
        assert atm.get_bank_name() == 'Harper Bank'

        return True


if __name__ == "__main__":
    """Run tests if module is executed by name."""
    atm = Atm(2023425, 'Lobby', 'Harper Bank')
    if atm.test():
        print("All tests successful!")
