from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title("Age Calculator")
root.geometry("400x300")

# Add Labels
Label(root, text="Enter your Date of Birth", font=("Arial", 14)).pack(pady=10)
Label(root, text="Day:", font=("Arial", 12)).place(x=50, y=60)
Label(root, text="Month:", font=("Arial", 12)).place(x=50, y=100)
Label(root, text="Year:", font=("Arial", 12)).place(x=50, y=140)

# Add Entry Widgets
day_entry = Entry(root, width=10)
day_entry.place(x=150, y=60) #.place is used to place the widget on the window

month_entry = Entry(root, width=10)
month_entry.place(x=150, y=100)

year_entry = Entry(root, width=10)
year_entry.place(x=150, y=140)

# Label for displaying results
result_label = Label(root, text="", font=("Arial", 12), fg="green")
result_label.place(x=50, y=220)

def calculate_age():
    result_label.config(text="") #.config is used to change the properties of the widget
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    today = date.today()
    birth_date = date(year, month, day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)) #is to check if the birth date has already passed this year. If it has, then the age will be calculated as (today.
    result_label.config(text="You are " + str(age) + " years old.")
Button(root, text="Calculate Age", command=calculate_age, bg="blue", fg="white", font=("Arial", 12)).place(x=140, y=180)
root.mainloop()