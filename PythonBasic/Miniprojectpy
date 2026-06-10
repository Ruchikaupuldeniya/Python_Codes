import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Success", "File saved successfully!")

root = tk.Tk()
root.title("Modern Text Editor")
root.geometry("900x600")
root.config(bg="#1e1e1e")

# Top bar
top_frame = tk.Frame(root, bg="#252526", height=50)
top_frame.pack(fill=tk.X)

title_label = tk.Label(
    top_frame,
    text=" Text Editor",
    bg="#252526",
    fg="white",
    font=("Segoe UI", 16, "bold")
)
title_label.pack(side=tk.LEFT, padx=20, pady=10)

# Button style
button_style = {
    "bg": "#3a3d41",
    "fg": "white",
    "activebackground": "#007acc",
    "activeforeground": "white",
    "font": ("Segoe UI", 10),
    "bd": 0,
    "padx": 15,
    "pady": 8,
    "cursor": "hand2"
}

btn_new = tk.Button(top_frame, text="New", command=new_file, **button_style)
btn_new.pack(side=tk.RIGHT, padx=5)

btn_open = tk.Button(top_frame, text="Open", command=open_file, **button_style)
btn_open.pack(side=tk.RIGHT, padx=5)

btn_save = tk.Button(top_frame, text="Save", command=save_file, **button_style)
btn_save.pack(side=tk.RIGHT, padx=5)

btn_exit = tk.Button(top_frame, text="Exit", command=root.quit, **button_style)
btn_exit.pack(side=tk.RIGHT, padx=5)

# Text area
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Consolas", 13),
    bg="#1e1e1e",
    fg="#d4d4d4",
    insertbackground="white",
    selectbackground="#264f78",
    padx=15,
    pady=15,
    bd=0
)
text.pack(expand=True, fill=tk.BOTH, padx=15, pady=15)

root.mainloop()