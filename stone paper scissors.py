import tkinter as tk
import random
choices = ['Rock', 'Paper', 'Scissors']
user_score = 0
computer_score = 0
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    result = ""
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Rock') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1
    label_user.config(text=f"You: {user_choice}")
    label_computer.config(text=f"Computer: {computer_choice}")
    label_result.config(text=result)
    label_score.config(text=f"Score → You: {user_score}  |  Computer: {computer_score}")
def reset_game():
    label_user.config(text="You:")
    label_computer.config(text="Computer:")
    label_result.config(text="")
    label_score.config(text=f"Score → You: {user_score}  |  Computer: {computer_score}")
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")
root.configure(bg="#E8F0FE")
tk.Label(root, text="🪨 Rock ✋ Paper ✂️ Scissors", font=("Arial", 16, "bold"), bg="#E8F0FE").pack(pady=10)
button_frame = tk.Frame(root, bg="#E8F0FE")
button_frame.pack(pady=10)
for choice in choices:
    btn = tk.Button(button_frame, text=choice, width=10, font=("Arial", 12), bg="#4CAF50", fg="white",
                    command=lambda c=choice: play(c))
    btn.pack(side=tk.LEFT, padx=10)
label_user = tk.Label(root, text="You:", font=("Arial", 12), bg="#E8F0FE")
label_user.pack(pady=5)
label_computer = tk.Label(root, text="Computer:", font=("Arial", 12), bg="#E8F0FE")
label_computer.pack(pady=5)
label_result = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="#333", bg="#E8F0FE")
label_result.pack(pady=10)
label_score = tk.Label(root, text="Score → You: 0  |  Computer: 0", font=("Arial", 12), bg="#E8F0FE")
label_score.pack(pady=10)
btn_reset = tk.Button(root, text="Play Again", font=("Arial", 12), bg="#2196F3", fg="white", command=reset_game)
btn_reset.pack(pady=10)
root.mainloop()
