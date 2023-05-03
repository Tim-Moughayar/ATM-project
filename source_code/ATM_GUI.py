import tkinter
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
root = Tk()
app = Window(root)

output_label = Label(text="ATM Output:")
output_box = Text(root, height=15, width=30, bg="light yellow")
input_label = Label(text="User Input:")
input_box = Entry(root, width=30, textvariable=None, bg="light yellow")
clear_button = Button(root, text="Clear", command=lambda: None)
enter_button = Button(root, text="Enter", command=lambda: None)


root.wm_title("Welcome to Ponzi Bank")

output_label.grid(row=0,column=0)
output_box.grid(row=0,column=1)
input_label.grid(row=1,column=0)
input_box.grid(row=1,column=1)
clear_button.grid(row=2,column=0)
enter_button.grid(row=2,column=1)


root.mainloop()