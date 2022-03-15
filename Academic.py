import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

global Window3

Window3=tk.Tk()
Window3.title("Academic Details")

df1=pd.read_excel("SD.xlsx")
df2=pd.read_excel("SD.xlsx", sheet_name=2)

l1=df2.iloc[i,1:]
        
l1=tk.Label(Window3,text="Academic Details",font=("Serif","40"))
l1.grid(row=0,columnspan=3)

l2=tk.Label(Window3,text=" ",font=("Serif","40"))
l2.grid(row=1,columnspan=3)
l3=tk.Label(Window3,text="Examination: ", font=("Serif","13"))
l3.grid(row=2,column=0)

n = tk.StringVar()
c1=tk.Combobox(Window3,textvariable=n)
c1.grid(row=2,column=1)
c1['values']=['Term 1','Term 2','Term 3','Term 4']
c1.current(1)

Window3.mainloop()
