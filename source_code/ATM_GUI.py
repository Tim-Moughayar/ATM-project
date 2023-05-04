import tkinter
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
root = Tk()
app = Window(root)

def clear_input_box():
    input_box.delete(0,END)

def update_output_box(update_text):
    output_box.configure(state=NORMAL) # unlocks output_box so it can be updated
    output_box.insert(END, update_text) # inserts update_text at the end of the text in output_box
    output_box.insert(END, "\n") # adds a line break after the inserted text
    output_box.configure(state=DISABLED) # locks output_box so it can no longer be updated
    output_box.yview_moveto(1) # scrolls to the bottom of output_box


def get_input_box():
    user_input = input_box.get()
    return user_input

def submit_user_input():
    user_input = get_input_box()
    update_output_box(user_input)
    historical_input.append(user_input)
    clear_input_box()

historical_input = []    

output_label = Label(text="ATM Output:") # label for output_box
output_box = Text(root, height=15, width=30, bg="light yellow", state=DISABLED) # creates read-only text box for program output
input_label = Label(text="User Input:") # label for input_box
input_box = Entry(root, width=30, textvariable=None, bg="light yellow") # entry widget for user input
clear_button = Button(root, text="Clear", command=lambda: clear_input_box()) # button to clear text from input_box
enter_button = Button(root, text="Enter", command=lambda: submit_user_input()) # button to submit user input


root.wm_title("Welcome to Ponzi Bank")

output_label.grid(row=0,column=0)
output_box.grid(row=0,column=1)
input_label.grid(row=1,column=0)
input_box.grid(row=1,column=1)
clear_button.grid(row=2,column=0)
enter_button.grid(row=2,column=1)


root.mainloop()