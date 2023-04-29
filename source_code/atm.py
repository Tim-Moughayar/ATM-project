from customer_console import CustomerConsole
from transaction import Transaction


class Atm:
    """ATM class for ATM software"""
    IDLE_STATE = 0
    SERVING_CUSTOMER_STATE = 1

    switch_on = False
    card_inserted = False

    def __init__(self, id, place, bank_name, bank_address):
        """Creates an ATM object.
        
        Args:
            id: int id number for the ATM.
            place: str description of ATM locaton.
            bank_name: str name of bank ATM is located.
            bank_address: str address of ATM.

        """
        self.id = id
        self.place = place
        self.bank_name = bank_name
        self.bank_address = bank_address

        # Create objects corresponding to component parts
        CustomerConsole()

    def run_atm(self):
        """Starts the atm"""
        print("it's alive")
        
        cash_in_atm = 10000
        print(f"Sending cash_in_atm to cash dispenser module. Amount: {cash_in_atm}") # temporary
        # CashDispenser.set_initial_cash(cash_in_atm)

        # gets pin from user
        pin = CustomerConsole.read_pin(self)
        card = 5425233430109903

        Transaction(self, card, pin, 1)
        Transaction.perform_transaction

    def switch_state(self):
        self.switch_on = True

    def switch_off(self):
        self.switch_on = False

    def card_inserted_state(self):
        self.card_inserted = True

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
        atm = Atm(2023425, 'Lobby', 'Harper Bank', None)
        assert atm.get_ID() == 2023425
        assert atm.get_place() == 'Lobby'
        assert atm.get_bank_name() == 'Harper Bank'
        
        atm.switch_state()
        assert atm.switch_on is True
    
        atm.switch_off()
        assert atm.switch_on is False
        
        atm.card_inserted_state()
        assert atm.card_inserted is True

        return True


if __name__ == "__main__":
    """Run tests if module is executed by name."""
    atm = Atm(2023425, 'Lobby', 'Harper Bank', None)
    if atm.test():
        print("All tests successful!")
