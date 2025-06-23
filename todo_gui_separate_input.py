import tkinter as tk
from tkinter import messagebox, ttk
tasks = []
def update_tasks():
    task_listbox.delete(*task_listbox.get_children())
    for task in tasks:
        task_listbox.insert("", "end", values=(task["no"], task["task"], "✔️ Done" if task["done"] else "❌ Pending"))
def add_task():
    try:
        task_no = int(no_entry.get())
        task_text = task_entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Input Error", "Task description cannot be empty.")
            return
        for task in tasks:
            if task["no"] == task_no:
                messagebox.showwarning("Duplicate", "Task number already exists.")
                return
        tasks.append({"no": task_no, "task": task_text, "done": False})
        update_tasks()
        no_entry.delete(0, tk.END)
        task_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Task number must be a valid integer.")
def mark_done():
    selected = task_listbox.focus()
    if not selected:
        messagebox.showinfo("Selection Required", "Please select a task to mark as done.")
        return
    selected_no = task_listbox.item(selected)["values"][0]
    for task in tasks:
        if task["no"] == selected_no:
            task["done"] = True
            break
    update_tasks()
def delete_task():
    selected = task_listbox.focus()
    if not selected:
        messagebox.showinfo("Selection Required", "Please select a task to delete.")
        return
    selected_no = task_listbox.item(selected)["values"][0]
    global tasks
    tasks = [task for task in tasks if task["no"] != selected_no]
    update_tasks()
    messagebox.showinfo("Task Deleted", f"Deleted task number: {selected_no}")
app = tk.Tk()
app.title("📝 To-Do List with Separate Input")
app.geometry("650x450")
app.configure(bg="#f0f4f7")
title_label = tk.Label(app, text="To-Do List Manager", font=("Arial", 20, "bold"), bg="#f0f4f7", fg="#333")
title_label.pack(pady=10)
input_frame = tk.Frame(app, bg="#f0f4f7")
input_frame.pack(pady=10)
no_label = tk.Label(input_frame, text="Task No:", font=("Arial", 12), bg="#f0f4f7")
no_label.grid(row=0, column=0, padx=5)
no_entry = tk.Entry(input_frame, font=("Arial", 12), width=5)
no_entry.grid(row=0, column=1, padx=5)
task_label = tk.Label(input_frame, text="Task Description:", font=("Arial", 12), bg="#f0f4f7")
task_label.grid(row=0, column=2, padx=5)
task_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
task_entry.grid(row=0, column=3, padx=5)
add_button = tk.Button(input_frame, text="➕ Add Task", command=add_task, font=("Arial", 12), bg="#4CAF50", fg="white")
add_button.grid(row=0, column=4, padx=5)
columns = ("No.", "Task", "Status")
task_listbox = ttk.Treeview(app, columns=columns, show="headings", height=10)
for col in columns:
    task_listbox.heading(col, text=col)
    task_listbox.column(col, width=200 if col != "Task" else 250, anchor="center")
task_listbox.pack(pady=10)
btn_frame = tk.Frame(app, bg="#f0f4f7")
btn_frame.pack(pady=10)
done_button = tk.Button(btn_frame, text="✔️ Mark as Done", command=mark_done, font=("Arial", 12), bg="#2196F3", fg="white")
done_button.pack(side=tk.LEFT, padx=10)
delete_button = tk.Button(btn_frame, text="🗑️ Delete Task", command=delete_task, font=("Arial", 12), bg="#f44336", fg="white")
delete_button.pack(side=tk.LEFT, padx=10)
app.mainloop()
