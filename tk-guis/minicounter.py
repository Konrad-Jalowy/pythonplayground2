import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

def clickHandler():
    current_sum = int(clicked.get())
    current_sum += 1
    print(current_sum)
    clicked.set(current_sum)

root = tk.Tk()
root.title("Greeter")
root.geometry("800x600")
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

fontApp = tkFont.Font(size=16)

main = ttk.Frame(root, padding=(20, 10, 20, 0))
main.grid(row=0, column=0)

clicked = tk.StringVar(value=0)


first_label = ttk.Label(main, text="Clicks: 0", font=fontApp)
first_label.grid(row=0, column=0, padx=(0, 10))

age_label = tk.Button(main, text="Click me", command=clickHandler, font=fontApp)
age_label.grid(row=1, column=0, padx=(0, 10))

root.mainloop()

