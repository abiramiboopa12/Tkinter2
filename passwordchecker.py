from tkinter import *

def check_password():  
    password = entry.get()  
    length = len(password)  
    
    if length == 0: 
        strength_label['text'] = "Enter a password"  # Show a message to enter a password
        strength_label['fg'] = "black"  # Set text color to black
    else:
        if length < 6:  
            strength_label['text'] = "Weak"  # Show "Weak" message
            strength_label['fg'] = "red"  # Set text color to red
        else:
            if length < 10: 
                strength_label['text'] = "Medium"  # Show "Medium" message
                strength_label['fg'] = "orange"  # Set text color to orange
            else: 
                strength_label['text'] = "Strong"  # Show "Strong" message
                strength_label['fg'] = "green"  # Set text color to green

root = Tk()
root.title("Password Strength Checker") 

label = Label(root, text="Enter Password:") 
label.pack()  

entry = Entry(root, show="*") 
entry.pack()  

check_button = Button(root, text="Check Strength", command=check_password) #check password strength
check_button.pack()  

strength_label = Label(root, text="")  # strength message
strength_label.pack()  

root.mainloop()  