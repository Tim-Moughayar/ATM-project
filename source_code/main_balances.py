from customer_console import CustomerConsole
from balances import Balance
from transaction import Transaction

def main():
    my_transaction = Transaction("xyz","abc",0,45)
    my_transaction.perform_transaction()

main()
