from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk 

root = Tk()
root.title("Denomination Calcualtor")
root.geometry("650x400")
root.configure(bg="light blue")
a = Image.open("app_img.jpeg")
a = a.resize((300,300))
i = ImageTk.PhotoImage(a)
l1 = Label(root,image=i,bg="light pink")
l1.place(x=180,y=20)
l2 = Label(root,text="Hey Welcome To Denomination Calculator",bg="light green")
l2.place(relx=0.5,y=340,anchor=CENTER)
def msg():
    m = messagebox.showinfo("Alert !!!","Do you want to calculate the denomination ?")
    if m=="ok":
        topwin()
b1 = Button(root,text="Let's Start",command=msg,bg="brown",fg="white")
b1.place(x=260,y=360)
def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")
    top.mainloop()
root.mainloop()