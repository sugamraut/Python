import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root=tk.Tk()
root.geometry('600x600')
root.resizable(False,False)
root.title('Image Button Demo')


def download_clicked():
    showinfo(
        title='Information',
        message='download button clicked!'
    )

download_icon= tk.PhotoImage(file='./unnamed.png')

download_button=ttk.Button(
   root,
   image=download_icon,
   text='Download',
   compound=tk.LEFT,
   command=download_clicked
)

download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()
