import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title("Tabs App")
root.geometry("800x600")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

frame1 = tk.Frame(notebook)
frame2 = tk.Frame(notebook)
frame3 = tk.Frame(notebook)

frame1.pack()
frame2.pack()
frame3.pack()

notebook.add(frame1, text="Tab 1")
notebook.add(frame2, text="Tab 2")
notebook.add(frame3, text="Tab 3")

root.mainloop()