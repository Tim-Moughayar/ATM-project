class ATM:
    OFF_STATE = 0
    IDLE_STATE = 1
    SERVING_CUSTOMER_STATE = 2

    id = 2023425
    place = 'Lobby'
    bank_name = 'Harper Bank'
    bank_address = '1555 Harper Street'

    state = OFF_STATE
    switch_on = False
    card_inserted = False

    def __init__(self, id, place, bank_name, bank_address):
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
