import pandas as pd
import tkinter as tk

Window=tk.Tk()
Window.title("Dashboard")

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

b1=tk.Button(Window,text="STUDENT DETAILS",font=("Serif","15"))
b1.grid(row=5,column=0)

l3=tk.Label(Window,text="        ")
l3.grid(row=5,column=1)

b2=tk.Button(Window,text="FEE DETAILS",font=("Serif","15"))
b2.grid(row=5,column=2)

l4=tk.Label(Window,text=" ",font=("Serif","35"))
l4.grid(row=6,columnspan=3)


b2=tk.Button(Window,text="ATTENDANCE DETAILS",font=("Serif","15"))
b2.grid(row=7,column=0)

b2=tk.Button(Window,text="ACADEMIC DETAILS",font=("Serif","15"))
b2.grid(row=7,column=2)

Window.mainloop()
