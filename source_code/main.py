from atm import Atm
from gui_class import Window

# bank_address is an ip address and we won't be connecting to an actual bank so removed it for simplicity.

gui = Window()
gui.mainloop()
the_atm = Atm(gui, 2023425, '1555 Harper Street', 'Harper Bank')
the_atm.run_atm()
