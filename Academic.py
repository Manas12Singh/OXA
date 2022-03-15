import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
global Window3

def plot():
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
    y = [i**2 for i in range(101)]
    plot1 = fig.add_subplot(111)
    plot1.plot(y)
    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
    canvas.get_tk_widget().pack()

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
c1=ttk.Combobox(Window3,textvariable=n)
c1.grid(row=2,column=1)
c1['values']=['Term 1','Term 2','Term 3','Term 4']
c1.current(0)

b1=tk.Button(Window3,text='Show',comman=plot)
b1.grid(row=3,column=1)

Window3.mainloop()
