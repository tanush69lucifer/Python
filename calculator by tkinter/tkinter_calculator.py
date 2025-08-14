import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x620")
root.minsize(420, 620)
root.configure(padx=10, pady=10)

dark_mode = False

entry = tk.Entry(root, font=("Arial", 20), bd=5, justify="right", bg="black", fg="#FFA500", insertbackground="#FFA500")
entry.pack(fill="x", pady=(0, 5))

result_label = tk.Label(root, font=("Arial", 18), anchor="e", bg="black", fg="#FFA500", height=2)
result_label.pack(fill="x", pady=(0, 5))

history = tk.Text(root, height=5, font=("Arial", 12), state="disabled", bg="#eee", fg="black")
history.pack(fill="x", pady=(0, 10))

def set_theme():
    bg = "#222" if dark_mode else "#fff"
    fg = "#fff" if dark_mode else "#000"
    history_bg = "#111" if dark_mode else "#eee"
    entry.config(bg=bg, fg="#FFA500", insertbackground="#FFA500")
    result_label.config(bg=bg, fg="#FFA500")
    history.config(bg=history_bg, fg=fg)
    root.config(bg=bg)

def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    set_theme()

def insert_value(val):
    if val in ["sin()", "cos()", "tan()", "log()", "sqrt()"]:
        entry.insert(tk.END, val[:-1] + "(")  # e.g., sin( instead of sin()
    else:
        entry.insert(tk.END, val)

def calculate(event=None):
    try:
        expression = entry.get()
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        result_label.config(text=f"= {result}")
        update_history(expression, result)
    except:
        result_label.config(text="Error")

def update_history(expr, res):
    history.config(state="normal")
    history.insert(tk.END, f"{expr} = {res}\n")
    history.config(state="disabled")
    history.see(tk.END)

def clear(event=None):
    entry.delete(0, tk.END)
    result_label.config(text="")

def delete_last():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Mode toggle button
toggle_btn = tk.Button(root, text="Mode", command=toggle_mode, bg="#FFA500", fg="black", font=("Arial", 12, "bold"))
toggle_btn.pack(pady=(0, 10))

frame = tk.Frame(root)
frame.pack()

buttons = [
    "7", "8", "9", "/", "sqrt()",
    "4", "5", "6", "*", "log()",
    "1", "2", "3", "-", "sin()",
    "0", ".", "+", "=", "cos()",
    "(", ")", "C", "Del", "tan()"
]

row = col = 0
for text in buttons:
    if text == "=":
        cmd = calculate
    elif text == "C":
        cmd = clear
    elif text == "Del":
        cmd = delete_last
    else:
        cmd = lambda t=text: insert_value(t)

    b = tk.Button(frame, text=text, width=6, height=2, font=("Arial", 12), command=cmd)
    b.grid(row=row, column=col, padx=4, pady=4)
    col += 1
    if col > 4:
        col = 0
        row += 1

root.bind("<Return>", calculate)
root.bind("<BackSpace>", lambda e: delete_last())
root.bind("<Escape>", clear)

set_theme()
root.mainloop()
