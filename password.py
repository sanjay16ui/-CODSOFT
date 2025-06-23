import random
import string
import tkinter as tk
from tkinter import messagebox
def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be positive!")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg="#F0F0F0")
label_title = tk.Label(root, text="🔐 Strong Password Generator", font=("Arial", 16, "bold"), bg="#F0F0F0")
label_title.pack(pady=10)
frame_input = tk.Frame(root, bg="#F0F0F0")
frame_input.pack(pady=10)
label_length = tk.Label(frame_input, text="Enter Password Length:", font=("Arial", 12), bg="#F0F0F0")
label_length.pack(side=tk.LEFT)
entry_length = tk.Entry(frame_input, width=10, font=("Arial", 12))
entry_length.pack(side=tk.LEFT, padx=5)
btn_generate = tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#4CAF50", fg="white", command=generate_password)
btn_generate.pack(pady=10)
entry_password = tk.Entry(root, font=("Arial", 14), width=30, justify='center')
entry_password.pack(pady=10)
root.mainloop()
