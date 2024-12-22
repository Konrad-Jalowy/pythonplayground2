import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Greeter")

first_name = tk.StringVar()
last_name = tk.StringVar()
user_age = tk.StringVar()

first_label = ttk.Label(root, text="First Name:")
last_label = ttk.Label(root, text="Last Name:")
age_label = ttk.Label(root, text="First Name:")

root.mainloop()