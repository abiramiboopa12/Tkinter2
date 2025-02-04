from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("400x400")

def handle_keypress(event):
    """print the character"""
    print(event.char)

window.bind("<Key>",handle_keypress)

def handle_click(event):
    print("\n The button was clicked")

button = Button(text="Click Me !")
button.pack()

button.bind("<Button-1>",handle_click)

window.mainloop()