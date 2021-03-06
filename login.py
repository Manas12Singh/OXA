import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import pandas as pd

global e2
global e1
global Window

def login():
    sid=e1.get()
    dob=str(e2.get())
    df=pd.read_excel("SD.xlsx")
    
    for i in range(len(df)):
        id=df.iat[i,0]
        if sid==id:
            d= (df.iat[i,4]).strftime("%d-%m-%Y")
            if dob==d:
                print("Yes")
                Window.destroy()
                exec(open("Dashboard.py").read())
                break
    else:
        messagebox.showerror("Error","Inavalid Credentials!")

def dash(n):
    l=e2.get()
    if len(l) in [2,5]:
        e2.insert(len(l),'-')
    
Window=tk.Tk()
Window.title("Student Login")

l1 = tk.Label(Window, text="Student Login",font=('castellar','50','underline'),padx=20)
l1.grid(row=0,columnspan=2)
        
l2=tk.Label(Window,text="")
l2.grid(row=1,column=0)
l3=tk.Label(Window,text="Student ID:",font=("Serif","20"))
l3.grid(row=2,column=0)
e1=tk.Entry(Window,font=("Serif","20"))
e1.grid(row=2,column=1)

l4=tk.Label(Window,text="Date Of Birth:",font=("Serif","20"))
l4.grid(row=3,column=0)
e2=DateEntry(Window,font=("Serif","19"),date_pattern="dd-mm-yyyy")
e2.grid(row=3,column=1)

e2.bind('1',dash)
e2.bind('2',dash)
e2.bind('3',dash)
e2.bind('4',dash)
e2.bind('5',dash)
e2.bind('6',dash)
e2.bind('7',dash)
e2.bind('8',dash)
e2.bind('9',dash)
e2.bind('0',dash)

b1=tk.Button(Window, text="LOGIN",font=("Serif","20"),padx=20, command=login)
b1.grid(row=4,columnspan=2)

Window.mainloop()
