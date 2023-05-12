"""Balance class for ATM.
Input:
    Customer Pin
Output:
    Display account balance
References: 
    
Created by Ravina
"""
import sqlite3
database = "atm_database.db"

class Balance():
    """Balance class for ATM."""
    def __init__(self, pin = 0):
        """Get pin and display balance"""
        self.pin = pin

        
            
    @property
    def pin(self):
        """Gets and sets pin"""
        return self._pin

    @pin.setter
    def pin(self, pin):
        self._pin = pin
        
    
    @property
    def account_balance(self):
        return self.get_balance()
    
    
    def get_balance(self):
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        sql = """
            SELECT Sum(Balance) From Users
            inner join Accounts on Users.UserID=Accounts.UserID
            where Users.PIN = """ + str(self.pin)
        cursor.execute(sql)
        result = cursor.fetchone()
        connection.close()
        return result[0]
        


        
        
        



        
        
        
        
