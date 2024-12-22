import tkinter as tk
from tkinter import ttk




root = tk.Tk()
root.title("Validate ipt")
root.geometry("800x600")
root.resizable(False, False)

some_entry = ttk.Entry(root)
some_entry.pack(side="left", expand=True, fill="x")

root.mainloop()
