# step 1 : import tkinter
from tkinter import *

# step 2 : GUI interaction
window=Tk()

# step 3 : add input
window.geometry("500x500")
check1=IntVar()
check2=IntVar()
check3=IntVar()
chk_button_1=Checkbutton(window,text="apple",onvalue=1,offvalue=0,height=2,width=10)
chk_button_2=Checkbutton(window,text="mango",onvalue=1,offvalue=0,height=2,width=10)
chk_button_3=Checkbutton(window,text="plum",onvalue=1,offvalue=0,height=2,width=10)

chk_button_1.pack()
chk_button_2.pack()
chk_button_3.pack()

# step 4 : main loop
mainloop()