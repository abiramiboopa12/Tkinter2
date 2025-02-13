from tkinter import *
root = Tk()
root.title("Root Window")
root.geometry("400x300")

def topwin():
    top = Toplevel()
    top.title("mango")
    top.geometry("180x100")
    l = Label(top,text="Mango is the best fruit")
    l.pack()
    top.mainloop()
l1 = Label(root,text="This is apple")
b = Button(root,text="click me",command=topwin)
l1.pack()
b.pack()
root.mainloop()