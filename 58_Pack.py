# step 1 : import trinter
from tkinter import *

# step 2 : GUI interaction
window=Tk()

# step 3 : add input
window.title("Simple")          # title
window.geometry("500x500")      #dimension

label1=Label(window,text="Label 1", bg="red",fg="white")
label2=Label(window,text="Label 2", bg="blue",fg="white")
label3=Label(window,text="Label 3", bg="green",fg="white")

label1.pack(side=TOP,fill = X,expand=False)
label2.pack(side=LEFT,fill = Y,expand=False)
label3.pack(side=RIGHT,fill = Y,expand=True)

# step 4 : main loop
mainloop()