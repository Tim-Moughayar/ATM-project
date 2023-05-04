"""Balance class for ATM.
Input:
    Customer Pin
Output:
    Display account balance
References: 
    
Created by Ravina
"""

class Balance():
    """Balance class for ATM."""
    def __init__(self, pin = 0):
        """Get pin and display balance"""
        self.pin = pin

    @property
    def pin(self):
        """Gets and sets pin"""
        return self.pin

    @pin.setter
    def pin(self, pin):
        self._pin = pin
        
    
    def balance(self):
        """Gets account balance"""
        return self.get_balance()
    
    
    def get_balance(self):
        """Method for getting account balance"""
        #create_connection()
        #sql = Select * From Where PIN = 'xyz'
        #run and commit sql
        return 500
        



        
        
        
        
