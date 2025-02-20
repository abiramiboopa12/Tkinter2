from tkinter import *
import random

def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif user_choice == "Rock" and computer_choice == "Scissors":
        result = "You Win!"
    elif user_choice == "Paper" and computer_choice == "Rock":
        result = "You Win!"
    elif user_choice == "Scissors" and computer_choice == "Paper":
        result = "You Win!"
    else:
        result = "You Lose!"

    label_result["text"] = "Computer: " + computer_choice + "\n" + result

root = Tk()
root.title("Rock Paper Scissors")

Label(root, text="Choose:").pack()

frame = Frame(root)
frame.pack()

btn_rock = Button(frame, text="Rock", command=lambda: play("Rock"))
btn_rock.pack(side=LEFT)

btn_paper = Button(frame, text="Paper", command=lambda: play("Paper")) #reates an anonymous function that calls play("Paper") when the button is clicked.
btn_paper.pack(side=LEFT)

btn_scissors = Button(frame, text="Scissors", command=lambda: play("Scissors"))
btn_scissors.pack(side=LEFT)

label_result = Label(root, text="Make a choice!", font=("Arial", 12))
label_result.pack()

root.mainloop()