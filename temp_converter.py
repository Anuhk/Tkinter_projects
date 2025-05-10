# -*- coding: utf-8 -*-
"""
Created on Sat May 10 14:52:23 2025

@author: Anushka
"""

#Design a Temperature conversion application using python Tkinter

import tkinter as tk

from tkinter import messagebox

def temp_conversion():
    
    try:
        temp=float(entry_temp.get())
        from_unit=combo_from.get()
        to_unit=combo_to.get()
        res=0
        if from_unit==to_unit:
            result.set(f"Result is: {temp}{to_unit}")
            return
        
        if from_unit=='Celcius':
            if to_unit=='Faranheit':
                res=(temp * 9/5)+32
            elif to_unit=='Kelvin':
                res=temp+273.15
        
        elif from_unit=='Faranheit':
            if to_unit=='Celcius':
                res=(temp-32)*(5/9)
            elif to_unit=='Kelvin':
                res=(temp-32)*(5/9)+ 273.15
        
        elif from_unit=='Kelvin':
            if to_unit=='Celcius':
                res=temp-273.15
            elif to_unit=='Faranheit':
                res=((temp-273.15) * 9/5)+32
        
        result.set(f"Answer: {res:.4f} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid Input","Please enter valid input")
        
window=tk.Tk()
window.title("Temperature Converter")


label=tk.Label(window,text="Enter Temperature: ")
label.pack()

entry_temp=tk.Entry(window)
entry_temp.pack()

label_from=tk.Label(window,text="From unit: ")
label_from.pack()

combo_from=tk.StringVar()
combo_from.set("Celcius")
drop_down_from=tk.OptionMenu(window, combo_from, "Celcius", "Faranheit","Kelvin")
drop_down_from.pack()

label_to=tk.Label(window,text="To unit: ")
label_to.pack()

combo_to=tk.StringVar()
combo_to.set("Celcius")
drop_down_to=tk.OptionMenu(window, combo_to, "Celcius", "Faranheit","Kelvin")
drop_down_to.pack()

btn_conv=tk.Button(window,text="Convert",command=temp_conversion)
btn_conv.pack()

result=tk.StringVar()
label_result=tk.Label(window,textvariable=result)
label_result.pack()
window.mainloop()