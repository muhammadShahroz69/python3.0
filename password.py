import tkinter as tk
import random
import string

def generate():
    length = int(entry.get())
    password = ""

    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits)

    result.config(text=password)

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Generate").pack(command=generate)

result = tk.Label(root, text="")
result.pack()

root.mainloop()
