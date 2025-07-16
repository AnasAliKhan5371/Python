# step 1 : import tkinter
from tkinter import *

from pyexpat.errors import messages

# step 2 : GUI interaction
window=Tk()

# step 3 : add input
window.geometry("500x500")
'''
message=Message(window,text="python")
message.pack()

var=StringVar()
message=Message(window,textvariable = var, relief=RAISED,padx=20,pady=20)
var.set("Welcome")
message.pack()
'''
var=StringVar()
ent_var=StringVar()
message=Message(window,textvariable=var,relief=RAISED,padx=50,pady=50)
entry=Entry(window,textvariable=ent_var)

def insert():
    result=ent_var.get()
    var.set(result)

button=Button(window,textvariable="OK", command=insert)
message.pack()
entry.pack()
button.pack()
# step 4 : main loop
mainloop()