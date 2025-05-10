# -*- coding: utf-8 -*-
"""
Created on Sat May 10 16:38:53 2025

@author: Anushka
"""

import tkinter as tk

from tkinter import messagebox


def conv_unit():
    
    try:
        unit=float(entry.get())
        from_unit=entry_From.get().lower()
        to_unit=entry_To.get().lower()
        
        if from_unit==to_unit:
            result.set(f"Answer {unit} {to_unit}")
            return
        
        if from_unit=="metre":
            res=(unit *100)
        
        else:
            res=unit/100
        
        result.set(f"Answer {res} {to_unit}")
        
    except ValueError:
        messagebox.showerror("Invalid input","Please enter valid input")

window=tk.Tk()
window.title("Unit Converter")
window.geometry("300x270")
label=tk.Label(window,text="Enter unit value: ")
label.pack()

entry=tk.Entry(window)
entry.pack()

label_from=tk.Label(window,text="From ")
label_from.pack()
entry_From=tk.Entry(window)
entry_From.pack()



label_to=tk.Label(window,text="To ")
label_to.pack()
entry_To=tk.Entry(window)
entry_To.pack()



btn_convert=tk.Button(window,text="Convert",command=conv_unit)
btn_convert.pack()


result=tk.StringVar()
label_result=tk.Label(window,textvariable=result)
label_result.pack()

window.mainloop()