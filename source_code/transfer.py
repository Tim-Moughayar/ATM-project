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
import sqlite3
import sqlite3
database = "atm_database.db"


class Transfer():
    """Transer class for ATM."""
    def __init__(self, from_pin, to_pin, transfer_amount):
        
        self.from_pin = from_pin
        self.to_pin = to_pin
        self.transfer_amount = transfer_amount

    @property
    def from_pin(self):
        """Gets and sets from_pin"""
        return self._from_pin

    @from_pin.setter
    def from_pin(self, from_pin):
        self._from_pin = from_pin
        
        
    @property
    def to_pin(self):
        """Gets and sets to_pin"""
        return self._to_pin

    @to_pin.setter
    def to_pin(self, to_pin):
        self._to_pin = to_pin
        
        
    @property
    def transfer_amount(self):
        """Gets and sets transfer_amount"""
        return self._transfer_amount

    @transfer_amount.setter
    def transfer_amount(self, transfer_amount):
        self._transfer_amount = transfer_amount
     
    def tesnnnt():
       return 500   
        
    def update_accounts(self):
        """Method for getting account balance"""
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        from_sql = """SELECT AcountId FROM Users
            join Accounts On Users.UserID = Accounts.UserID
            where pin = """ + str(self.from_pin) + """ LIMIT 1"""
        cursor.execute(from_sql)
        from_account = cursor.fetchone()[0]
        
        to_sql = """SELECT AcountId FROM Users
            join Accounts On Users.UserID = Accounts.UserID
            where pin = """ + str(self.to_pin) + """ LIMIT 1"""
        cursor.execute(to_sql)
        to_account = cursor.fetchone()[0]
        
        update_from_sql = """UPDATE Accounts
                        SET Balance = Balance + """ + str(self.transfer_amount) + """ WHERE AcountID = """ + str(from_account)
        
        cursor1 = connection.cursor()
        cursor1.execute(update_from_sql)

        update_to_sql = """UPDATE Accounts
                        SET Balance = Balance - """ + str(self.transfer_amount) + """ WHERE AcountID = """ + str(to_account)
        
        cursor2 = connection.cursor()
        cursor2.execute(update_to_sql)

        connection.commit()
        
        connection.close()
        
        
        
        
        
    
   
    def updateaccountbalance(self,accountid,transferamount):
        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        sql = """UPDATE Accounts""" 
        + """ SET Balance = Balance + """ + str(transferamount) 
        + """ WHERE AcountID = """ + accountid 

        cursor = connection.cursor()
        cursor.execute(sql)

        print("Successfully updated!")

        connection.commit()
        
        

        

                    
    
    
    
        
        
    