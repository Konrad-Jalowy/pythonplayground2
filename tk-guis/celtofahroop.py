import tkinter as tk
from tkinter import ttk

class CelToFahrConverter(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Cel to Fahr Converter")
        self.geometry("800x600")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        frame = UserInputFrame(self)
        frame.grid()

class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.cel_text = tk.StringVar(value="")
        self.converted_text = tk.StringVar(value="")

        label_input = ttk.Label(self, text="Temperature in Celsius: ")
        entry_input = ttk.Entry(self, textvariable=self.cel_text)

        label_output = ttk.Label(self, text="Temperature in Celsius: ")
        entry_output = ttk.Entry(self, textvariable=self.converted_text)
      

        label_input.grid(row=0, column=0)
        entry_input.grid(row=0, column=1)
    
    def greet(self):
        print(f"Hello, {self.user_input.get()}!")



root = CelToFahrConverter()
root.mainloop()