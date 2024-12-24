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

        label_output = ttk.Label(self, text="Temperature in Fahr: ")
        entry_output = ttk.Entry(self, textvariable=self.converted_text, state="readonly")
        
        btn = tk.Button(self, text="Convert", command=self.clickhandler)

        label_input.grid(row=0, column=0, sticky="W")
        entry_input.grid(row=0, column=1)

        label_output.grid(row=1, column=0, sticky="W")
        entry_output.grid(row=1, column=1)

        
        btn.grid(row=2, column=0, columnspan=2, sticky="ew")
    
    def clickhandler(self):
        print("Click handler called")

    def cel_to_fahr(self, cel):
        return (cel * 1.8) + 32
    



root = CelToFahrConverter()
root.mainloop()