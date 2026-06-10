import tkinter as tk

#creat a window

root = tk.Tk()

root.title("Hello world")
root.resizable(True,False)
root.iconbitmap("favicon.ico")
width,height=500,500

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenwidth()


left=int(display_width/2 - width/2)
top=int(display_height/2 - height/2)

root.geometry(f'{width}x{height}+{left}+{top}')   #width * height+left+top


# run the window
root.mainloop()

print("heloo")
