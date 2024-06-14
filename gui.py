import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List App")

        self.tasks = []

        self.task_entry = tk.Entry(self.master, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.tasks_listbox = tk.Listbox(self.master, width=50, height=15)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.update_button = tk.Button(self.master, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

        self.show_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.show_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.task_entry.delete(0, tk.END)
                self.show_tasks()
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            del self.tasks[selected_task_index]
            self.show_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def show_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)


def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
