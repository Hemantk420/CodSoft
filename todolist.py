from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

def main():
    win = tk.Tk()
    app = TodoList(win)
    win.mainloop()

class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.maxsize(1000, 700)
        self.root.minsize(990, 700)
        self.root.title('TO-DO-LIST')
        self.root.config(bg='white')
        self.tasks = []

        img = Image.open('Slide1.JPG')
        img_resized = img.resize((1000, 800))
        self.img_lbl = ImageTk.PhotoImage(img_resized)

        logo = tk.Label(self.root, image=self.img_lbl, bg='white')
        logo.pack(padx=5, pady=5)

        self.task_entry = tk.Entry(logo, width=47, bg='white', font=('times new roman', 14), bd=2)
        self.task_entry.place(x=500, y=220, height=40)

        self.frame = tk.Frame(logo, width=450, bg='white')
        self.frame.place(x=520, y=280, height=40)

        self.add_button = tk.Button(self.frame, text="Add Task", bg='aqua', font=('arial', 10), command=self.add_task)
        self.add_button.place(x=50, y=10)

        self.edit_button = tk.Button(self.frame, text="Edit Task", bg='aqua', font=('arial', 10),
                                     command=self.edit_task)
        self.edit_button.place(x=170, y=10)

        self.delete_button = tk.Button(self.frame, text="Delete Task", bg='aqua', font=('arial', 10),
                                       command=self.delete_task)
        self.delete_button.place(x=290, y=10)

        self.task_listbox = tk.Listbox(logo, width=70, bg='WHITE', bd=2)
        self.task_listbox.place(x=500, y=350, height=260)

        self.load_tasks()

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text.strip():
            self.tasks.append(task_text)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            tk.messagebox.showwarning("Warning", "Task cannot be empty!")

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            selected_task = self.task_listbox.get(selected_task_index)
            edited_task_text = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=selected_task)
            if edited_task_text and edited_task_text.strip():
                self.tasks[selected_task_index] = edited_task_text
                self.update_task_listbox()
            else:
                tk.messagebox.showwarning("Warning", "Task cannot be empty!")
        else:
            tk.messagebox.showwarning("Warning", "No task selected for editing.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            del self.tasks[selected_index]
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def load_tasks(self):
        self.tasks = ["Buy groceries", "Finish project", "Call mom"]
        self.update_task_listbox()


if __name__ == '__main__':
    main()
