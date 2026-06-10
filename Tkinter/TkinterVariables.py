import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("variables")
root.geometry("300x200")

variable_value = tk.StringVar(value='Welcome')

label = ttk.Label(root,textvariable=variable_value)
label.pack()

entry = ttk.Entry(root,textvariable=variable_value)
entry.pack()

root.mainloop()