import tkinter as tk
import random

def play(choice):
    computer = random.choice(["Rock", "Paper", "Scissors"])

    if choice == computer:
        result = "Draw"
    elif (choice == "Rock" and computer == "Scissors") or \
         (choice == "Paper" and computer == "Rock") or \
         (choice == "Scissors" and computer == "Paper"):
        result = "You Win"
    else:
        result = "Computer Wins"

    label.config(text="You: " + choice + "\nComputer: " + computer + "\n" + result)

root = tk.Tk()
root.title("Rock Paper Scissors")

tk.Button(root, text="Rock", command=lambda: play("Rock")).pack()
tk.Button(root, text="Paper", command=lambda: play("Paper")).pack()
tk.Button(root, text="Scissors", command=lambda: play("Scissors")).pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
