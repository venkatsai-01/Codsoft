import tkinter as tk
import random
def choice_generate():
    return random.choice(["rock", "paper", "scissors"])
def game_logic(x,y):
    if(x==y):
        return "tie"
    elif(x=="rock" and y=="scissors") or \
        (x=="paper" and y=="rock") or \
        (x=="scissors" and y=="paper"):
        return "user"
    else:
        return "computer"
def game(user_input):
    global score_user, score_computer
    choice_user = user_input
    choice_computer = choice_generate()
    result = game_logic(choice_user, choice_computer)

    label_choice_computer.config(text=f"Computer chose: {choice_computer}")
    if result == "tie":
        label_result.config(text="It's a tie!")
    elif result == "user":
        label_result.config(text="You win!")
        score_user += 1
    else:
        label_result.config(text="Computer wins!")
        score_computer += 1

    label_score.config(text=f"Score - You: {score_user} | Computer: {score_computer}")

score_user = 0
score_computer = 0

window = tk.Tk()
# window.geometry("1200x500")
window.title("Rock Paper Scissors")
#Buttons
btn_rock = tk.Button(window, text="Rock", font=("Arial",14), command=lambda: game("rock"))
btn_paper = tk.Button(window, text="Paper", font=("Arial",14), command=lambda: game("paper"))
btn_scissors = tk.Button(window, text="Scissors", font=("Arial",14), command=lambda: game("scissors"))
#Labels
label_instruction = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Arial", 12))
label_choice_computer = tk.Label(window, text="Computer chose: ?", font=("Arial", 12))
label_result = tk.Label(window, text="", font=("Arial", 14))
label_score = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
#Placing Widgets
label_instruction.pack()
btn_rock.pack(pady=5)
btn_paper.pack(pady=5)
btn_scissors.pack(pady=5)
label_choice_computer.pack(pady=10)
label_result.pack()
label_score.pack(pady=10)
window.mainloop()