import pandas as pd
import tkinter as tk

global l8
global Window2

Window2=tk.Tk()
Window2.title("Dashboard")

def student_detail():
    Window2.destroy()
    exec(open("SD.py").read())
def fee_detail():
    Window2.destroy()
    exec(open("Fee.py").read())
def att_detail():
    Window2.destroy()
    exec(open("Attendance.py").read())
def aca_detail():
    Window2.destroy()
    exec(open("Academic.py").read())
def blue(n):
    l6.config(fg='#0000FF')
def black(n):
    l6.config(fg='#000000')
def login(n):
    Window2.destroy()
    exec(open("Login.py").read())
  

df=pd.read_excel("SD.xlsx")

for i in range(len(df)):
    id=df.iat[i,0]
    if sid==id:
        n=df.iat[i,1]
        bc=df.iat[i,3]
    

l1=tk.Label(Window2,text=n,font=("Serif","40"))
l1.grid(row=1,columnspan=3)
l2=tk.Label(Window2,text="STUDENT ID: "+sid,font=("Serif","20"))
l2.grid(row=2,columnspan=3)
l3=tk.Label(Window2,text="BATCH CODE: "+bc,font=("Serif","20"))
l3.grid(row=3,columnspan=3)
l4=tk.Label(Window2,text=" ",font=("Serif","40"))
l4.grid(row=4,columnspan=3)

b1=tk.Button(Window2,text="STUDENT DETAILS",font=("Serif","15"),command=student_detail)
b1.grid(row=5,column=0)

l5=tk.Label(Window2,text="        ")
l5.grid(row=5,column=1)

b2=tk.Button(Window2,text="FEE DETAILS",font=("Serif","15"),command=fee_detail)
b2.grid(row=5,column=2)

l6=tk.Label(Window2,text=" ",font=("Serif","20"))
l6.grid(row=6,columnspan=3)


b3=tk.Button(Window2,text="ATTENDANCE DETAILS",font=("Serif","15"),command=att_detail)
b3.grid(row=7,column=0)

b4=tk.Button(Window2,text="ACADEMIC DETAILS",font=("Serif","15"),command=aca_detail)
b4.grid(row=7,column=2)

l7=tk.Label(Window2,text=" ",font=("Serif","20"))
l7.grid(row=6,columnspan=3)

l8=tk.Label(Window2,text="Back to home",font='Serif 10 underline')
l8.grid(row=9,column=1)

l8.bind('<Enter>',blue)
l8.bind('<Leave>',black)
l8.bind('<Button-1>',login)

Window2.mainloop()
