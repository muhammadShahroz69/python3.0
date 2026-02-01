import tkinter as tk

def calculate():
    amt = int(entry.get())

    n2000 = amt // 2000
    amt %= 2000

    n500 = amt // 500
    amt %= 500

    n100 = amt // 100

    result.config(text=f"2000 : {n2000}\n500 : {n500}\n100 : {n100}")

root = tk.Tk()
root.title("Denomination Calculator")

tk.Label(root, text="Enter Amount").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate", command=calculate).pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()
