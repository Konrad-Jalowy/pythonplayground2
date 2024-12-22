import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

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

root.mainloop()