import tkinter as tk
from tkinter import *
import customer_console
import main_balances
import deposit
import cash_dispenser
import atm
import balances

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.transaction_log = []    

        self.output_label = Label(text="ATM Output:") # label for output_box
        self.output_box = Text(self, height=15, width=30, bg="light yellow", state=DISABLED) # creates read-only text box for program output
        self.input_label = Label(text="User Input:") # label for input_box
        self.input_box = Entry(self, width=30, textvariable=None, bg="light yellow", show="*") # entry widget for user input
        self.clear_button = Button(self, text="Clear", command=lambda: self.clear_input_box()) # button to clear text from input_box
        self.enter_button = Button(self, text="Enter", command=lambda: self.submit_user_input()) # button to submit user input
        self.login_button = Button(self, text="Login", command=lambda: None)
        self.deposit_button = Button(self, text="Deposit", command=lambda: None)
        self.withdraw_button = Button(self, text="Withdrawal", command=lambda: None)
        self.transfer_button = Button(self, text="Transfer", command=lambda: None)
        self.yes_button = Button(self, text="Yes", command=lambda: None)
        self.no_button = Button(self, text="No", command=lambda: None)

        self.wm_title("Welcome to Ponzi Bank")

        self.output_label.grid(row=0,column=0)
        self.output_box.grid(row=0,column=1)
        self.input_label.grid(row=1,column=0)
        self.input_box.grid(row=1,column=1)
        self.clear_button.grid(row=2,column=0)
        self.enter_button.grid(row=2,column=1)
        self.login_button.grid(row=3, column=1)
        self.deposit_button.grid(row=4, column=1)
        self.withdraw_button.grid(row=5, column=1)
        self.transfer_button.grid(row=6, column=1)
        self.yes_button.grid(row=7, column=1)
        self.no_button.grid(row=8, column=1)


    def update_output_box(self, update_text):
        print("running")
        self.output_box.configure(state=NORMAL) # unlocks output_box so it can be updated
        self.output_box.insert(END, update_text) # inserts update_text at the end of the text in output_box
        self.output_box.insert(END, "\n") # adds a line break after the inserted text
        self.output_box.configure(state=DISABLED) # locks output_box so it can no longer be updated
        self.transaction_log.append(update_text) # adds the updated text to the transaction log
        self.output_box.yview_moveto(1) # scrolls to the bottom of output_box
        self.update_text = update_text


    def clear_input_box(self):
        self.input_box.delete(0,END)

    def insert_input(self, text):
        self.update_output_box(text)

    def get_input_box(self):
        self.user_input = self.input_box.get()
        return self.user_input

    def submit_user_input(self):
        self.user_input = self.get_input_box()
        self.update_output_box(self.user_input)
        self.clear_input_box()
        return self.user_input


if __name__ == "__main__":
    app = Window()
    app.mainloop()
