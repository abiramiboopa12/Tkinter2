from tkinter import *  #

def calculate_interest():  
    try:
        P = float(principal.get())  # Get the principal amount and turn it into a number
        R = float(rate.get())  
        T = float(time.get()) 
        SI = (P * R * T) / 100  # (Principal * Rate * Time) / 100
        CI = P * ((1 + R / 100) ** T) - P  # P * ((1 + Rate / 100) ^ Time) - P
        simple_interest_result_label['text'] = "Simple Interest: " + str(round(SI, 2))  # Display the Simple Interest in the label, rounded to 2 decimals
        compound_interest_result_label['text'] = "Compound Interest: " + str(round(CI, 2))  # Display the Compound Interest in the label, rounded to 2 decimals
    except ValueError:  # This runs if there's an error, like if the user types something that isn't a number
        simple_interest_result_label['text'] = "Invalid Input! Enter numbers only."  # Show an error message for invalid input
        compound_interest_result_label['text'] = ""  # Clear the Compound Interest label
window = Tk()
window.title("Interest Calculator")  # Set the title of the window
principal_label = Label(window, text="Principal Amount:")  # Label for principal amount
principal_label.grid(row=0, column=0)  # Place the label in the grid
principal = Entry(window)  # Create a box where the user will enter the principal amount
principal.grid(row=0, column=1)  # Place the box next to the label
rate_label = Label(window, text="Rate of Interest (% per annum):")  # Label for interest rate
rate_label.grid(row=1, column=0)  # Place the label in the grid
rate = Entry(window)  # Create a box where the user will enter the rate of interest
rate.grid(row=1, column=1)  # Place the box next to the label
time_label = Label(window, text="Time Period (years):")  # Label for time period
time_label.grid(row=2, column=0)  # Place the label in the grid
time = Entry(window)  # Create a box where the user will enter the time period
time.grid(row=2, column=1)  # Place the box next to the label
calculate_button = Button(window, text="Calculate", command=calculate_interest)  # Create the button
calculate_button.grid(row=3, column=0, pady=10)  # Place the button in the grid
simple_interest_result_label = Label(window, text="", fg="blue")  # Label for showing the simple interest result
simple_interest_result_label.grid(row=4, column=0)  # Place it below the input fields

compound_interest_result_label = Label(window, text="", fg="green")  # Label for showing the compound interest result
compound_interest_result_label.grid(row=5, column=0)  # Place it below the simple interest result
window.mainloop()