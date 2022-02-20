import tkinter as tk
from tkcalendar import DateEntry

def login():
    sid=e1.get()
    dob=e2.get()
    Window.destroy()
    exec("dashboard.py")
    
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
e2=DateEntry(Window,font=("Serif","19"))
e2.grid(row=3,column=1)
        
b1=tk.Button(Window, text="LOGIN",font=("Serif","20"),padx=20, command=login)
b1.grid(row=4,columnspan=2)

Window.mainloop()