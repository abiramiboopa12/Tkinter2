import tkinter  
from tkinter import messagebox  
def convert_to_cm(event):  
    try:  
        inches = float(entry_box.get())  
        cm = inches * 2.54  
        result_label["text"] = str(round(cm, 2)) + " cm"  # Updates the label with the converted value
    except ValueError:  # Handles cases where input is not a valid number
        messagebox.showerror("Invalid Input", "Please enter a valid number")  # Shows an error message if input is invalid
root = tkinter.Tk()  # Creates the main window for the GUI
root.title("Inches to Centimeters Converter")  # Sets the window title
frame = tkinter.Frame(root, relief="sunken", borderwidth=3)  # Creates a frame with a sunken border for visual structure
frame.pack()  # Packs the frame into the window
label = tkinter.Label(frame, text="Enter length (in inches):")  # Creates a label with instructions
label.pack()  # Places the label inside the frame
entry_box = tkinter.Entry(frame)  # Creates an entry field for the user to input inches
entry_box.pack()  # Places the entry field inside the frame
convert_button = tkinter.Button(frame, text="Convert")  # Creates a button labeled "Convert"
convert_button.pack() 
convert_button.bind("<Button-1>", convert_to_cm)  # Binds the left mouse button click event to the convert_to_cm function
result_label = tkinter.Label(frame, text="")  # Creates an empty label to show the converted value
result_label.pack()  #
root.mainloop() 