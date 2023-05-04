from customer_console import CustomerConsole
from balances import Balance

def main():
    my_console = CustomerConsole()
    my_choice_list = ['Deposit', 'Withdraw', 'Balance']
    my_console.read_menu_choices('Choice: ', my_choice_list)
    #if input() == '3':
    pin = my_console.read_pin()
    my_balance = Balance()
    my_balance.pin = pin
    account_balance = my_balance.balance()
    print("Balance: $" + str(account_balance))

    

main()