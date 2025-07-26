# step 1 : import trinter
from tkinter import *

# step 2 : GUI interaction
window=Tk()

# step 3 : add input
window.title("Simple")          # title
window.geometry("500x700")      #dimension
window.config(bg="yellow")      #background

frame1=Frame(window,width=300,height=300,cursor="dot")
frame2=Frame(window,width=300,height=300,cursor="dotbox")

button1=Button(frame1,text="Button1",bg="blue")
button2=Button(frame2,text="Button2",bg="green")
button3=Button(frame1,text="Logged",fg="red")

frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button1.pack()
button2.pack()
button3.pack()
# step 4 : main loop
mainloop()