class ATM:
    """ATM class for ATM software"""
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
        """Assigns the ATM the switched on state.
    
        Returns:
            boolean: True if switched on.
    
        """
        switch_on = True
        return switch_on

    def switch_off(self, switch_on):
        """Assigns the ATM the switched off state.
    
        Returns:
            boolean: False if switched off.
    
        """
        switch_on = False
        return switch_on

    def card_inserted_state(self, card_inserted):
        """Checks if the ATM card has been inserted.
    
        Returns:
            boolean: True if ATM card has been inserted.
    
        """
        card_inserted = True
        return card_inserted

    def get_ID(self, id):
        """Gets the ATM ID number.
    
        Returns:
            integer: ID number of the ATM.
    
        """
        return id

    def get_place(self, place):
        """Gets the ATM location.
        
        Returns:
            string: Name of ATM location.
    
        """
        return place

    def get_bank_name(self, bank_name):
        """Gets the name of the bank.
        
        Returns:
            string: Name of the bank.
    
        """
        return bank_name

    def test(self):
        """Tests ATM class properties and methods.

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
