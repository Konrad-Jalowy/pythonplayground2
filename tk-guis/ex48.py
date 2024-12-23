import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog as fd

def clickhandler():
    print("clicked")

root = tk.Tk()
root.title("File Dialog App")
root.geometry("800x600")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame = tk.Frame(root)
main_frame.grid()

btn = ttk.Button(main_frame,text="Upload File", command=clickhandler)
btn.grid()
           

root.mainloop()