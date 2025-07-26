# TKINTER is a module that helps to create GUI applications

# step 1 : import tkinter
from tkinter import *

# step 2 : GUI interaction
window=Tk()

# step 3 : add input
inp=Label(window , text="Hello World!")
inp.pack()

# step 4 : main loop
window.mainloop()  # without main loop - no error, no execution