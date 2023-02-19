from tkinter import *
from tkinter import messagebox
import re

login= Tk()
login.title("Calculator By Omkar")
login.resizable(0,0)

frame=Frame(login, background="cyan",bd=2, width=400, height=500, relief=RAISED)
frame.pack()
frame.propagate(0)
name=Label(frame, text="Calculator", background="black", width=400, font="times 30", fg="#00ECFF", relief=RAISED).pack()
displ=Entry(frame,width=400, bd=8, font="arial 20", fg="red",bg="black", relief=GROOVE, justify=RIGHT)
displ.pack(ipadx=20, ipady=20)
keypad=Frame(frame, width=400, height=500)
keypad.pack()
keypad.propagate(0)

#buttons
b0=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="CLEAR", command=lambda:clear())
b0.grid(row=0, column=0)

b1=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="2√", command=lambda:symbols("√"))
b1.grid(row=0, column=1)

b2=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="X^Y", command=lambda:symbols("^"))
b2.grid(row=0, column=2)

b3=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="+", command=lambda:symbols("+"))
b3.grid(row=0, column=3)

b4=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="7", command=lambda:symbols(7))
b4.grid(row=1, column=0)

b5=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="8", command=lambda:symbols(8))
b5.grid(row=1, column=1)

b6=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="9", command=lambda:symbols(9))
b6.grid(row=1, column=2)

b7=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="-", command=lambda:symbols("-"))
b7.grid(row=1, column=3)

b8=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="4", command=lambda:symbols(4))
b8.grid(row=2, column=0)

b9=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="5", command=lambda:symbols(5))
b9.grid(row=2, column=1)

b10=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="6", command=lambda:symbols(6))
b10.grid(row=2, column=2)

b11=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="*", command=lambda:symbols("*"))
b11.grid(row=2, column=3)

b12=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="1", command=lambda:symbols(1))
b12.grid(row=3, column=0)

b13=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="2", command=lambda:symbols(2))
b13.grid(row=3, column=1)

b14=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="3", command=lambda:symbols(3))
b14.grid(row=3, column=2)

b15=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="/", command=lambda:symbols("/"))
b15.grid(row=3, column=3)

b16=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text=".", command=lambda:symbols("."))
b16.grid(row=4, column=0)

b17=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="0", command=lambda:symbols(0))
b17.grid(row=4, column=1)

b18=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="<--", command=lambda:displ.delete(len(displ.get())-1,END))
b18.grid(row=4, column=2)

b19=Button(keypad, bg="black", fg="#00FF00", activebackground="#00FF00", activeforeground="black", width=13, height=4, text="=", command=lambda:process())
b19.grid(row=4, column=3)

#functions
def symbols(var):
    displ.insert(END, str(var))
def clear():
    displ.delete(0,END)
def process():
    a=displ.get()
    if (".." in a) or ("++" in a) or ("--" in a) or ("**" in a) or ("//" in a) or ("√√" in a) or ("^^" in a):
        messagebox.showerror("Input Error","There should be number before or after (. + - * / % √ ^)")
        clear()
        return None
    if "+" in a:
        b=list(map(float, a.split(sep="+")))
        c=sum(b)
    if "-" in a:
        b=list(map(float, a.split(sep="-")))
        c=b[0]-sum(b[1:])
    if "*" in a:
        b=list(map(float, a.split(sep="*")))
        c=1
        for i in b:
            c*=i
    if "/" in a:
        b=list(map(float, a.split(sep="/")))
        c=b[0]
        for i in range(1,len(b)):
            c/=b[i]
    if "%" in a:
        b=list(map(float, a.split(sep="+")))
        c=b[0]/100
    if "√" in a:
        b=re.sub(r'.', '', a, count = 1)
        b=float(b)
        c=pow(b, 0.5)
    if "^" in a:
        b=list(map(float, a.split(sep="^")))
        c=pow(b[0],b[1])
    clear()
    messagebox.showinfo("Answer",str(a)+" = "+"{:.3f}".format(c))
    

login.mainloop()