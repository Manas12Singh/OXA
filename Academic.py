import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

global Window3

Window3=tk.Tk()
Window3.title("Academic Details")

df1=pd.read_excel("SD.xlsx")
df2=pd.read_excel("SD.xlsx", sheet_name=2)

l1=df2.iat[i,[1,2,3]]
l2=df2.iat[i,[5,6,7]]
l3=df2.iat[i,[8,9,10]]
l4=df2.iat[i,[12,13,14]]
        
l1=tk.Label(Window3,text="Academic Details",font=("Serif","40"))
l1.grid(row=0,columnspan=3)

l2=tk.Label(Window3,text=" ",font=("Serif","40"))
l2.grid(row=1,columnspan=3)
l3=tk.Label(Window3,text="Examination: ", font=("Serif","13"))
l3.grid(row=2,column=0)

Wondow3.mainloop()
