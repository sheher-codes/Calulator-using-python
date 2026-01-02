import tkinter as tk

def press(key):
    entry.insert(tk.END, str(key))

def clear():
    entry.delete(0, tk.END)

def backspace():
    text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, text[:-1])

def calculate():
    expr = entry.get()

    if not expr or expr[-1] in "+-*/.":
        return

    try:
        if '+' in expr:
            a, b = expr.split('+')
            result = float(a) + float(b)

        elif '-' in expr:
            a, b = expr.split('-')
            result = float(a) - float(b)

        elif '*' in expr:
            a, b = expr.split('*')
            result = float(a) * float(b)

        elif '/' in expr:
            a, b = expr.split('/')
            if float(b) == 0:
                raise ZeroDivisionError
            result = float(a) / float(b)
        else:
            return

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def key_handler(event):
    if event.char.isdigit() or event.char in "+-*/.":
        press(event.char)
        return "break"

    if event.keysym == "Return":
        calculate()
        return "break"

    if event.keysym == "BackSpace":
        backspace()
        return "break"

    if event.keysym == "Escape":
        clear()
        return "break"

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10)
entry.focus()

# 🔑 Bind keyboard ONLY to entry
entry.bind("<KeyPress>", key_handler)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

frame = tk.Frame(root)
frame.pack()

row = col = 0
for btn in buttons:
    if btn == "=":
        cmd = calculate
    else:
        cmd = lambda x=btn: press(x)

    tk.Button(
        frame,
        text=btn,
        width=5,
        height=2,
        font=("Arial", 14),
        command=cmd
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(
    root,
    text="Clear",
    width=20,
    height=2,
    font=("Arial", 12),
    command=clear
).pack(pady=10)

root.mainloop()
