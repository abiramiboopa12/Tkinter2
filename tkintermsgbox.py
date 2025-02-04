from tkinter import *
from tkinter import messagebox 

root = Tk()
root.title("Message Box")
root.geometry("350x350")

def msg():
    messagebox.askyesno("Do u wanna continue ?")

button = Button(text="Do not press me !!!",command=msg)
button.place(x=175,y=175)

root.mainloop()