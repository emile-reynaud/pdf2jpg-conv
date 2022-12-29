from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import os

master = Tk()
master.title("Convert PDF to JPG")
master.geometry("300x150")

Label(master, text="PDF Location:").grid(row=0, sticky=W)

e1 = Entry(master)
e1.grid(row=0, column=1)
def select_file():
    filetypes = (('PDF files', '*.pdf'),('All files', '*.*'))

    filename = fd.askopenfilename(title='Open file', initialdir=os.path.expanduser('~/Documents/'), filetypes=filetypes)

    e1.delete(0, len(str(e1.get())))
    e1.insert(0, filename)

def pdf2img():
	try:
		images = convert_from_path(str(e1.get()))

	except :
		Result = "NO pdf found"
		messagebox.showinfo("Result", Result)

	else:
		f = fd.asksaveasfilename(initialfile='Untitled.jpg', defaultextension=".jpg", filetypes=[("JPEG Documents","*.jpg"),("All Files","*.*")])
		for img in images:
			img.save(f, 'JPEG')
		Result = "Success"
		messagebox.showinfo("Result", Result)

conv_button = Button(master, text="Convert", command=pdf2img)
conv_button.grid(row=3, column=1, columnspan=2, rowspan=1, padx=5, pady=5)

open_button = Button(master,text='Open file',command=select_file)
open_button.grid(row=0, column=2, columnspan=2, rowspan=1, padx=5, pady=5)

mainloop()