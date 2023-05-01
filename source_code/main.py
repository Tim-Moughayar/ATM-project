from atm import Atm

# bank_address is an ip address and we won't be connecting to an actual bank so removed it for simplicity.
the_atm = Atm(2023425, '1555 Harper Street', 'Harper Bank') 
the_atm.run_atm()
