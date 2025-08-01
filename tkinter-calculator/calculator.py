import tkinter as tk

def click(event):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + str(event.widget["text"]))

def evaluate(event):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font="Arial 20")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        b = tk.Button(root, text=btn, font="Arial 20", width=5)
        b.grid(row=i+1, column=j)
        if btn == '=':
            b.bind("<Button-1>", evaluate)
        elif btn == 'C':
            b.config(command=clear)
        else:
            b.bind("<Button-1>", click)

root.mainloop()