# step 1 : import trinter
from tkinter import *

# step 2 : GUI interaction
window=Tk()

# step 3 : add input
window.title("Simple")          # title
window.geometry("250x50")      #dimension

label1=Label(window,text="Mail")
label2=Label(window,text="Password")

e1=Entry(window,width=40,borderwidth=5)
e2=Entry(window,width=40,borderwidth=5)

label1.grid(row=0,column=1)
label2.grid(row=1,column=1)
e1.grid(row=0,column=2)
e2.grid(row=1,column=2)

# step 4 : main loop
mainloop()