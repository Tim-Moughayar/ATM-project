"""Transfer class for ATM.
Input:
    From PIN
    To PIN
Output:
    Return customer balances after transfer
References: 
    
Created by Ravina
"""

from balances import Balance


class Transfer():
    """Transer class for ATM."""
    def __init__(self, from_pin, to_pin, transfer_amount):
        
        self.from_pin = from_pin
        self.to_pin = to_pin
        self.transfer_amount = transfer_amount

    @property
    def from_pin(self):
        """Gets and sets from_pin"""
        return self.from_pin

    @from_pin.setter
    def from_pin(self, from_pin):
        self._from_pin = from_pin
        
        
    @property
    def to_pin(self):
        """Gets and sets to_pin"""
        return self.to_pin

    @to_pin.setter
    def to_pin(self, to_pin):
        self._to_pin = to_pin
        
        
    @property
    def transfer_amount(self):
        """Gets and sets transfer_amount"""
        return self.transfer_amount

    @transfer_amount.setter
    def transfer_amount(self, transfer_amount):
        self._transfer_amount = transfer_amount
        
        
    def update_accounts():
        """Method for getting account balance"""
        #create_connection()
        #sql = UPDATE Accounts SET Balance = Balance - (transfer_amount) WHERE AccountID = from_pin
        #sql = UPDATE Accounts SET Balance = Balance + (transfer_amount) WHERE AccountID = to_pin
        #run and commit sql
        
    
    
    
        
        
    