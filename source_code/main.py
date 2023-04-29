from atm import Atm

the_atm = Atm(2023425, 'Lobby', 'Harper Bank', None) # bank_address is an ip address and we
the_atm.run_atm()                                    # won't be connecting to an actual bank.
