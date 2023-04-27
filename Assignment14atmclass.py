class ATM:
    OFF_STATE = 0
    IDLE_STATE = 1
    SERVING_CUSTOMER_STATE = 2

    state = OFF_STATE
    switch_on = False
    card_inserted = False

    def __init__(self, id, place, bank_name, bank_address):
        """
        Creates an ATM object.

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

    def switch_state(self, switch_on):
        switch_on = True
        return switch_on

    def switch_off(self, switch_on):
        switch_on = False
        return switch_on

    def card_inserted_state(self, card_inserted):
        card_inserted = True
        return card_inserted

    def get_ID(self, id):
        return id

    def get_place(self, place):
        return place

    def get_bank_name(self, bank_name):
        return bank_name

    def test(self):
        """
        Tests ATM class properties and methods.

        Returns:
            True if tests assert successfully.

        Raises:
            AssertionError if any of the asserts fail.
        """
        atm = ATM()
        atm.id = 2023425
        assert atm.get_ID == 2023425
        atm.place = 'Lobby'
        assert atm.get_place == 'Lobby'
        atm.bank_name = 'Harper Bank'
        assert atm.get_bank_name == 'Harper Bank'
        atm.bank_address = '1555 Harper Street'
        assert atm.bank_address == '1555 Harper Street'
        assert atm.get_bank_name == 'Harper Bank'
        assert atm.switch_state is True
        assert atm.switch_off is False
        assert atm.card_inserted_state is True
