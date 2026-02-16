import tkinter as tk
from tkinter import messagebox, simpledialog

# Main To-Do List
todo_list = []

# Functions
def add_task():
    task = simpledialog.askstring("Add Task", "Enter your task:")
    if task:
        todo_list.append(task)
        update_listbox()
        status_label.config(text=f"Task '{task}' added!", fg="green")

def remove_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        removed = todo_list.pop(index)
        update_listbox()
        status_label.config(text=f"Task '{removed}' removed!", fg="red")
    else:
        messagebox.showwarning("Remove Task", "Select a task to remove!")

def update_listbox():
    listbox.delete(0, tk.END)
    for idx, task in enumerate(todo_list, 1):
        listbox.insert(tk.END, f"{idx}. {task}")

def exit_app():
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("🌈 Interactive To-Do List")
root.geometry("400x500")
root.config(bg="#f0f8ff")  # light blue background

# Title Label
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#4b0082")
title_label.pack(pady=10)

# Listbox to display tasks
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)
listbox = tk.Listbox(listbox_frame, width=40, height=15, font=("Arial", 12), bg="#fffacd", fg="#00008b", selectbackground="#ffa500")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=5)
scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Buttons
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=15)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, width=12, bg="#7fffd4", fg="#000", font=("Arial", 12, "bold"))
add_button.grid(row=0, column=0, padx=5, pady=5)

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task, width=12, bg="#ff7f50", fg="#000", font=("Arial", 12, "bold"))
remove_button.grid(row=0, column=1, padx=5, pady=5)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app, width=12, bg="#dc143c", fg="#fff", font=("Arial", 12, "bold"))
exit_button.grid(row=1, column=0, columnspan=2, pady=10)

# Status Label
status_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff")
status_label.pack(pady=5)

# Start the GUI loop
root.mainloop()
