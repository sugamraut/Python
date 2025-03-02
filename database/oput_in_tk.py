from tkinter import *

master=Tk()

#w=Label(master,text="welcome to SDC")
Label(master,text="First Name").grid(row=0)
Label(master,text="last Name").grid(row=1)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

#button=tk.Button(master,Text="login",width='24',Command=master.destory)
button = Button(master, text="Login", width=24, command=master.destroy)  # Corrected Button and text
#button.pack()
button.grid(row=2, column=0, columnspan=2)
master.mainloop() 