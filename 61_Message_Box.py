# step 1 : import tkinter
from tkinter import *
import tkinter.messagebox

# step 2 : GUI interaction
window=Tk()

# step 3 : add input
tkinter.messagebox.showerror("Info","Running out of time")
question=tkinter.messagebox.askyesno("Weather","will it rain ?")
if question == True:
    print("take an umbrella.")
else:
    print("ok")

# step 4 : main loop
mainloop()