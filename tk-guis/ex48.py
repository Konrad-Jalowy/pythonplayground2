import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

def clickhandler():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

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