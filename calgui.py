import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sys
import os
import re
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
root = tk.Tk()
root.title("Date")
root.geometry("400x200")
root.resizable(0,0)
root.configure(background="white")
label = tk.Label(root, text="Enter a date in the format YYYYMMDD: ", bg="white")
label.pack()
entry = tk.Entry(root, width=50, bg="white")
d = entry.get()
entry.pack()
button = tk.Button(root, text="Submit", bg="white", command=lambda: date(entry.get()))
def date(d):
    yc = [6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0]
    mc = [1,4,4,0,2,5,0,3,6,1,4,6]
    dc = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    year = int(d[0:4])
    month = int(d[4:6])
    day = int(d[6:8])
    yf= int(d[0:2])
    yl=int(d[2:4])
    year = int(year)
    print (year) 
    y = yc[int(yf)]
    m = mc[int(month)-1]
    a=day+m+y+yl+math.floor(yl/4)
    f=a%7
    print (f)
    s=dc[int(f)]
    #calculate age till date upto date
    age = 2022 - year
    print (age) 
    #show age in the gui
    label = tk.Label(root, text="You are " + str(age) + " years old", bg="white")
    label.pack()
    #show day of the week
    label = tk.Label(root, text="You were born on a " + str(s), bg="white")
    label.pack()
    print (s)
    #messagebox.showinfo("Day", s)
    pass
button.pack()
root.mainloop()

