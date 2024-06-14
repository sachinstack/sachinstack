import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def mark_as_completed():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.itemconfig(index, {'bg': 'light grey', 'fg': 'green'})
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Create entry field for adding tasks
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Create "Add Task" button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Create "Remove Task" button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Create "Mark as Completed" button
mark_button = tk.Button(root, text="Mark as Completed", command=mark_as_completed)
mark_button.pack()

# Create listbox to display tasks
task_listbox = tk.Listbox(root, width=50)
task_listbox.pack()

# Start the GUI main loop
root.mainloop()

 