import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

def cel_to_fahr(cel):
    return (cel * 1.8) + 32


root = tk.Tk()
root.title("Cel to Fahr Converter")
root.geometry("800x600")
root.resizable(False, False)

fontApp = tkFont.Font(size=16)

main_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
main_frame.grid(row=0, column=0)

root.mainloop()