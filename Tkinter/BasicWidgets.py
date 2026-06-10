import tkinter as tk

from tkinter import ttk  #ttk using for the the modern button


root = tk.Tk()

root.title('Basic Widgets')
root.geometry('300x200')
root.resizable(False,False)

#for the text box
entry = ttk.Entry(root)
entry.pack()

#for the modern button  using the ttk
def button_click_func():
    #entry_field_value = entry.get()
    label.configure(text=entry.get())
    button.configure(state='disabled')

button = ttk.Button(root,text='Click Me',command =button_click_func)
button.pack()



label = ttk.Label(root)
label.pack()

root.mainloop()