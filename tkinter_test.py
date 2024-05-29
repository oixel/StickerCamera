from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('100x100')

def c():
    print("Button pressed!")
    root.destroy()

button = Button(root, text = 'Click me !', 
                command = c) 

# Set the position of button on the top of window 
button.pack(side = 'top')     

root.mainloop() 