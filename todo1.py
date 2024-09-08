import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel

class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        # Create and set up the listbox
        self.listbox = tk.Listbox(self.root, height=10, width=40)
        self.listbox.pack(pady=20)

        # Add task button
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task_window)
        self.add_button.pack(pady=5)

        # Remove task button
        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task_window)
        self.remove_button.pack(pady=5)

        # Update task button
        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task_window)
        self.update_button.pack(pady=5)

        # Display task button
        self.display_button = tk.Button(self.root, text="Display Tasks", command=self.display_tasks_window)
        self.display_button.pack(pady=5)

    def add_task_window(self):
        # Creating a new window to add tasks
        add_window = Toplevel(self.root)
        add_window.title("Add Task")

        # Task input
        label = tk.Label(add_window, text="Enter new task:")
        label.pack(pady=10)

        task_entry = tk.Entry(add_window, width=30)
        task_entry.pack(pady=5)

        def add_task_action():
            task = task_entry.get()
            if task:
                self.tasks.append(task)
                self.listbox.insert(tk.END, task)  # Update listbox with new task
                messagebox.showinfo("Success", "Task added successfully!")
                add_window.destroy()
            else:
                messagebox.showwarning("Input Error", "Task cannot be empty!")

        add_button = tk.Button(add_window, text="Add Task", command=add_task_action)
        add_button.pack(pady=5)

    def remove_task_window(self):
        # Creating a new window to remove tasks
        remove_window = Toplevel(self.root)
        remove_window.title("Remove Task")

        label = tk.Label(remove_window, text="Select task to remove:")
        label.pack(pady=10)

        def remove_task_action():
            try:
                selected_index = self.listbox.curselection()[0]
                self.listbox.delete(selected_index)
                del self.tasks[selected_index]
                messagebox.showinfo("Success", "Task removed successfully!")
                remove_window.destroy()
            except IndexError:
                messagebox.showwarning("Error", "Please select a task to remove!")

        remove_button = tk.Button(remove_window, text="Remove Task", command=remove_task_action)
        remove_button.pack(pady=5)

    def update_task_window(self):
        # Creating a new window to update tasks
        update_window = Toplevel(self.root)
        update_window.title("Update Task")

        label = tk.Label(update_window, text="Select task to update:")
        label.pack(pady=10)

        task_entry = tk.Entry(update_window, width=30)
        task_entry.pack(pady=5)

        def update_task_action():
            try:
                selected_index = self.listbox.curselection()[0]
                new_task = task_entry.get()
                if new_task:
                    self.tasks[selected_index] = new_task
                    self.listbox.delete(selected_index)
                    self.listbox.insert(selected_index, new_task)
                    messagebox.showinfo("Success", "Task updated successfully!")
                    update_window.destroy()
                else:
                    messagebox.showwarning("Input Error", "Task cannot be empty!")
            except IndexError:
                messagebox.showwarning("Error", "Please select a task to update!")

        update_button = tk.Button(update_window, text="Update Task", command=update_task_action)
        update_button.pack(pady=5)

    def display_tasks_window(self):
        # Creating a new window to display tasks
        display_window = Toplevel(self.root)
        display_window.title("Display Tasks")

        if self.tasks:
            tasks = "\n".join([f"{i+1}. {task}" for i, task in enumerate(self.tasks)])
            label = tk.Label(display_window, text=tasks)
            label.pack(pady=10)
        else:
            label = tk.Label(display_window, text="Your To-Do List is empty")
            label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()
