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

cel = tk.DoubleVar(value=0)
converted_text = tk.StringVar(value="Enter value in Celsius and convert do Fahr")

main_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
main_frame.grid(row=0, column=0)

output_entry = ttk.Entry(main_frame, width=15, textvariable=converted_text)
output_entry.grid(row=0, column=0, padx=(0, 10), ipady=5, sticky="we")

root.mainloop()