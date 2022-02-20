import pandas as pd
import tkinter as tk

Window=tk.Tk()
Window.title("Dashboard")



l2=tk.Label(Window,text="STUDENT_NAME",font=("Serif","40"))
l2.grid(row=1,columnspan=3)
l2=tk.Label(Window,text="STUDENT_ID",font=("Serif","20"))
l2.grid(row=2,columnspan=3)
l2=tk.Label(Window,text="BATCH CODE: "+"BA01",font=("Serif","20"))
l2.grid(row=3,columnspan=3)
l2=tk.Label(Window,text=" ",font=("Serif","40"))
l2.grid(row=,columnspan=3)

b1=tk.Button(Window,text="STUDENT DETAILS",font=("Serif","15"))
b1.grid(row=4,column=0)

l3=tk.Label(Window,text="        ")
l3.grid(row=4,column=1)

b2=tk.Button(Window,text="FEE DETAILS",font=("Serif","15"))
b2.grid(row=4,column=2)

b2=tk.Button(Window,text="ATTENDANCE DETAILS",font=("Serif","15"))
b2.grid(row=5,column=0)

b2=tk.Button(Window,text="ACADEMIC DETAILS",font=("Serif","15"))
b2.grid(row=5,column=2)

Window.mainloop()