import pandas as pd
import tkinter as tk

Window=tk.Tk()
Window.title("Dashboard")

def student_detail():
    Window.destroy()
    exec(open("SD.py").read())
def fee_detail():
    Window.destroy()
    exec(open("Fee.py").read())
def att_detail():
    Window.destroy()
    exec(open("Attendance.py").read())
def aca_detail():
    Window.destroy()
    exec(open("Academic.py").read())
def blue():
    l6.fg='blue'
def black():
    l6.fg='black'
    
  

df=pd.read_excel("SD.xlsx")

for i in range(len(df)):
    id=df.iat[i,0]
    if sid==id:
        n=df.iat[i,1]
        bc=df.iat[i,3]
    

l2=tk.Label(Window,text=n,font=("Serif","40"))
l2.grid(row=1,columnspan=3)
l2=tk.Label(Window,text="STUDENT ID: "+sid,font=("Serif","20"))
l2.grid(row=2,columnspan=3)
l2=tk.Label(Window,text="BATCH CODE: "+bc,font=("Serif","20"))
l2.grid(row=3,columnspan=3)
l2=tk.Label(Window,text=" ",font=("Serif","40"))
l2.grid(row=4,columnspan=3)

b1=tk.Button(Window,text="STUDENT DETAILS",font=("Serif","15"),command=student_detail)
b1.grid(row=5,column=0)

l3=tk.Label(Window,text="        ")
l3.grid(row=5,column=1)

b2=tk.Button(Window,text="FEE DETAILS",font=("Serif","15"),command=fee_detail)
b2.grid(row=5,column=2)

l4=tk.Label(Window,text=" ",font=("Serif","20"))
l4.grid(row=6,columnspan=3)


b2=tk.Button(Window,text="ATTENDANCE DETAILS",font=("Serif","15"),command=att_detail)
b2.grid(row=7,column=0)

b2=tk.Button(Window,text="ACADEMIC DETAILS",font=("Serif","15"),command=aca_detail)
b2.grid(row=7,column=2)

l5=tk.Label(Window,text=" ",font=("Serif","20"))
l5.grid(row=6,columnspan=3)

l6=tk.Label(Window,text="Bact to home",font='Serif 10 underline')
l6.grid(row=9,column=1)

l6.bind('<Enter>',blue)
l6.bind('<Leave>',black)

Window.mainloop()
