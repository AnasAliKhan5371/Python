# step 1 : import trinter
from tkinter import *

# step 2 : GUI interaction
window=Tk()

# step 3 : add input
window.title("Simple")          # title
window.geometry("500x500")      #dimension

def log_entry():
    print("Logged In")

buttton=Button(window,text="LOGIN", command = log_entry,width=12,bg="red",fg="white",font=("bold",12),activebackground="black", activeforeground="white")

buttton.pack()

# step 4 : main loop
mainloop()