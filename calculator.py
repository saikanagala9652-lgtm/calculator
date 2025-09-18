import tkinter as tk

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry_var.get())  # Evaluate the expression
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")  # Handle invalid input
    elif text == "C":
        entry_var.set("")  # Clear screen
    else:
        entry_var.set(entry_var.get() + text)  # Add clicked button text

# Create main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

# Entry box to display numbers
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for text in row:
        b = tk.Button(frame, text=text, font="Arial 18", relief="ridge", height=2, width=5)
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>", click)

# Run the application
root.mainloop()
