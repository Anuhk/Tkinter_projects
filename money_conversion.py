# -*- coding: utf-8 -*-
"""
Created on Sat May 10 22:25:56 2025

@author: Anushka
"""

import tkinter as tk
from tkinter import messagebox


def conv_money():
    try:
        money=float(entry_label.get())
        from_unit=combo_from.get()
        to_unit=combo_to.get()
        
        if from_unit==to_unit:
            result.set(f"Result: {money} {to_unit}")
            return
        
        if from_unit=="INR":
            res=money * 0.012
        else:
            res=money//0.012
        
        result.set(f"Result: {res:.2f} {to_unit}")
        
    except ValueError:
        messagebox.showerror("Invalid Input","Please enter a valid input")
    

window=tk.Tk()
window.title("INR to $ converter")
window.geometry("300x270")
label=tk.Label(window,text="Enter money: ")
label.pack()

entry_label= tk.Entry(window)
entry_label.pack()

from_label=tk.Label(window,text="From unit:")
from_label.pack()

combo_from=tk.StringVar()
combo_from.set("INR")
drop_down_from=tk.OptionMenu(window,combo_from,"INR","$")
drop_down_from.pack()

to_label=tk.Label(window,text="To Unit: ")
to_label.pack()

combo_to=tk.StringVar()
combo_to.set("INR")
drop_down_to=tk.OptionMenu(window,combo_to,"INR","$")
drop_down_to.pack()

btn_convert=tk.Button(window,text="Convert",command=conv_money)
btn_convert.pack()

result=tk.StringVar()
label_res=tk.Label(window,textvariable=result)
label_res.pack()






window.mainloop()

            
        
    
    
        
    