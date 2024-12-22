import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Greeter")

first_name = tk.StringVar()
last_name = tk.StringVar()
user_age = tk.StringVar()

first_label = ttk.Label(root, text="First Name:")
first_entry = ttk.Entry(root, width=15, textvariable=first_name)
last_label = ttk.Label(root, text="Last Name:")
last_entry = ttk.Entry(root, width=15, textvariable=last_name)
age_label = ttk.Label(root, text="First Name:")
age_entry = ttk.Entry(root, width=15, textvariable=user_age)

root.mainloop()