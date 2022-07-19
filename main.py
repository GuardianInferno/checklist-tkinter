#Checklist
import tkinter
from tkinter import END, ANCHOR

#Define Window
root = tkinter.Tk()
root.title("Checklist")
root.geometry("400x400")
root.resizable(0,0)

#Define fonts and colors
my_font = ("Times New Roman", 12)
root_color = "#224870"
button_color = "#d5dfe5"
root.config(bg=root_color)

#Define Functions
def add_item():
    """Add an individual item to the listbox"""
    my_listbox.insert(END, list_entry.get())
    list_entry.delete(0, END)

def remove_item():
    """Remove the selected (ANCHOR) item from the listbox"""
    my_listbox.delete(ANCHOR)

def clear_list():
    pass

def save_list():
    pass

def open_list():
    pass


#Define Layout and Create Frames
input_frame = tkinter.Frame(root, bg=root_color)
output_frame = tkinter.Frame(root, bg=root_color)
button_frame = tkinter.Frame(root, bg=root_color)
input_frame.pack()
output_frame.pack()
button_frame.pack()

#Input frame layout
list_entry = tkinter.Entry(input_frame, width=35, borderwidth=3, font=my_font)
list_add_button = tkinter.Button(input_frame, text="Add Item", borderwidth=2, font=my_font, bg=button_color, command=add_item)
list_entry.grid(row=0, column=0, padx=5, pady=5)
list_add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=5)

#Output Frame Layout
my_scrollbar = tkinter.Scrollbar(output_frame)
my_listbox = tkinter.Listbox(output_frame, height=15, width=45, borderwidth=3, font=my_font, yscrollcommand=my_scrollbar.set)
#Link the scrollbar to the listbox
my_scrollbar.config(command=my_listbox.yview)
my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky="NS")

#BUtton Frame Layout
list_remove_button = tkinter.Button(button_frame, text="Remove Item", borderwidth=2, font=my_font, bg=button_color, command=remove_item)
list_clear_button = tkinter.Button(button_frame, text="Clear List", borderwidth=2, font=my_font, bg=button_color, command=clear_list)
save_button = tkinter.Button(button_frame, text="Save List", borderwidth=2, font=my_font, bg=button_color, command=save_list)
quit_button = tkinter.Button(button_frame, text="Quit", borderwidth=2, font=my_font, bg=button_color, command=root.destroy)
list_remove_button.grid(row=0, column=0, padx=2, pady=10)
list_clear_button.grid(row=0, column=1, padx=2, pady=10, ipadx=10)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=10)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=25)


open_list()


root.mainloop()
