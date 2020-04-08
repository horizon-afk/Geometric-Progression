import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("Geometric Progression")
window.geometry('400x500+300+300')
window.resizable(0,0)

arow = tk.Frame(window)
arow.pack(expand = True, fill = "x")

#The Frames
crrow = tk.Frame(window)
crrow.pack(expand = True, fill = "x")

nrow = tk.Frame(window)
nrow.pack(expand = True, fill = "x")

resultrow = tk.Frame(window)
resultrow.pack(expand = True, fill = "x")

btnrow = tk.Frame(window)
btnrow.pack(expand = True, fill = "both")

#The labels
lbla = tk.Label(
    arow,
    text = "Enter First Term",
    font = ("Calibri",16),
)
lbla.grid(row = 0, column = 1)

lblcr = tk.Label(
    crrow,
    text = "Enter Common Ratio",
    font = ("Calibri", 16),
)
lblcr.grid(row = 0, column = 1)

lbln = tk.Label(
    nrow,
    text = "Enter the number of terms",
    font = ("Calibri", 16)
)
lbln.grid(row = 0, column = 1 )

lblr = tk.Label(
    resultrow,
    text = "The required term",
    font = ("Calibri", 16)
)
lblr.grid(row = 0, column = 1)

#Text box designs
a   = tk.StringVar()
cr  = tk.StringVar()
n   = tk.StringVar()
output = tk.StringVar()

#The first term
txta = tk.Entry(
    arow,
    width = 10,
    font = ("Calibri",16),
    textvariable = a
)
txta.place(x = 280, y = 0)

#The common ratio
txtcr = tk.Entry(
    crrow,
    width = 10,
    font = ("Calibri", 16),
    textvariable = cr
)
txtcr.place(x = 280, y = 0)

#The number of terms
txtn = tk.Entry(
    nrow,
    width = 10,
    font = ("Calibri", 16),
    textvariable = n
)
txtn.place(x = 280, y = 0)

#Validation buttons
def result():
    a = (txta.get())
    r = (txtcr.get())
    n = (txtn.get())
    if (a.isdigit() and r.isdigit() and n.isdigit()):
        a = int(a)
        r = int(r)
        n = int(n)
        C = a * r ** (n - 1)
        output.set(C)
        return True
    else:
        tk.messagebox.showwarning("Wrong Data!", "Please enter integer only to proceed.")
        return False
 
def clear():
    a.set("")
    cr.set("")
    n.set("")
    output.set("")
    
#The label to show the output
lblr2 = tk.Label(
    resultrow,
    width = 10,
    textvariable = output,
    bg = "#ffffff",
    fg = "#000000",
    font = ("Calibri", 16,)
)
lblr2.place(x = 280, y = 0 )

#The buttons
btn_findterm = tk.Button(
    btnrow,
    text = "Find the Term",
    font = ("Calibri",16),
    command = result
)
btn_findterm.place(x = 10, y = 10)

btn_clear = tk.Button(
    btnrow,
    text = "Clear",
    font = ("Calibri", 16),
    command = clear
)
btn_clear.place(x = 275, y = 10)

window.mainloop()
