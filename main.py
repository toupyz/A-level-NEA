from tkinter import *
from tkinter import ttk

def button_event():
    print("Button clicked")



root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="click me", command=button_event).grid(column=2, row=0)

root.mainloop()