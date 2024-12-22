import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

def cel_to_fahr(cel):
    return (cel * 1.8) + 32


root = tk.Tk()
root.title("Cel to Fahr Converter")
root.geometry("800x600")
root.resizable(False, False)

root.mainloop()