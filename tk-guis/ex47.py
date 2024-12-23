import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title("Tabs App")
root.geometry("800x600")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')
root.mainloop()