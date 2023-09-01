import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.config(bg='#FF3030')
root.minsize(335,520)
root.maxsize(335,520)
root.config(border=5)


# Create an entry widget
entry = tk.Entry(root, width=35, borderwidth=6,font=('arial'),bg='#FFEBCD')
entry.grid(row=0, column=0, columnspan=4,ipady=12,pady=5)

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 3)
]

# Create buttons and add them to the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=10,  command=lambda t=text: button_click(t), foreground='#FF3030',bd=5, bg='white',font=('arial',24,'bold'))
    button.grid(row=row, column=col,pady=10)

# Bind "=" button to the equal function
equal_button = tk.Button(root, text="=", padx=10, command=button_equal, fg='#FF3030',bd=5, bg='white', font=('arial', 24,'bold'))
equal_button.grid(row=4, column=1, columnspan=4)

# Create a clear button
clear_button = tk.Button(root, text="Clear", padx=15, pady=10,command=button_clear,bd=5, fg='#FF3030', bg='white',font=('arial'))
clear_button.grid(row=5, column=0, columnspan=4,pady=10)



# Start the main loop
root.mainloop()
