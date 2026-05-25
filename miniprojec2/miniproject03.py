from tkinter import *
from PIL import Image, ImageTk
import random

#  WINDOW 
root = Tk()
root.title("Rock Paper Scissor Game")
root.geometry("1100x700")
root.config(bg="#0F172A")
root.resizable(False, False)

#  MAIN FRAME 
main = Frame(root, bg="#1E293B")
main.place(x=50, y=50, width=1000, height=600)

title = Label(main, text="ROCK PAPER SCISSOR GAME",
              font=("Arial", 26, "bold"),
              bg="#1E293B", fg="cyan")
title.pack(pady=15)

#  IMAGE FUNCTION 
size = (180, 180)

def load(path):
    img = Image.open(path)
    img = img.resize(size)
    return ImageTk.PhotoImage(img)

#  IMAGES 
rock_img = load(r"C:\Users\2021icts80\Desktop\ScissorPaperRock\image\right.jpg")
paper_img = load(r"C:\Users\2021icts80\Desktop\ScissorPaperRock\image\paper.jpg")
scissor_img = load(r"C:\Users\2021icts80\Desktop\ScissorPaperRock\image\Scissor.jpg")
cpu_img = load(r"C:\Users\2021icts80\Desktop\ScissorPaperRock\image\left.jpg")

#  SCORE 
player_score = 0
computer_score = 0
WIN_SCORE = 5

#  GAME AREA 
game = Frame(main, bg="#1E293B")
game.pack(pady=10)

Label(game, text="COMPUTER", bg="#1E293B", fg="white",
      font=("Arial", 14, "bold")).grid(row=0, column=0)

Label(game, text="PLAYER", bg="#1E293B", fg="white",
      font=("Arial", 14, "bold")).grid(row=0, column=2)

cpu_label = Label(game, image=cpu_img, bg="#1E293B")
cpu_label.grid(row=1, column=0, padx=20)

player_label = Label(game, image=scissor_img, bg="#1E293B")
player_label.grid(row=1, column=2, padx=20)

# score labels
cpu_score_lbl = Label(game, text="0", font=("Arial", 35),
                      bg="#0F172A", fg="red", width=3)
cpu_score_lbl.grid(row=1, column=1)

player_score_lbl = Label(game, text="0", font=("Arial", 35),
                         bg="#0F172A", fg="green", width=3)
player_score_lbl.grid(row=1, column=3)

#  MESSAGE 
msg = Label(main, text="First to 5 wins",
            font=("Arial", 18, "bold"),
            bg="#1E293B", fg="yellow")
msg.pack(pady=10)

#  FUNCTIONS 
def update_score():
    cpu_score_lbl.config(text=str(computer_score))
    player_score_lbl.config(text=str(player_score))


def stop_game():
    rock_btn.config(state=DISABLED)
    paper_btn.config(state=DISABLED)
    scissor_btn.config(state=DISABLED)


def show(text):
    msg.config(text=text)


def computer_choice():
    r = random.randint(0, 2)

    if r == 0:
        cpu_label.config(image=rock_img)
        return "rock"
    elif r == 1:
        cpu_label.config(image=paper_img)
        return "paper"
    else:
        cpu_label.config(image=scissor_img)
        return "scissor"


def set_player(choice):
    if choice == "rock":
        player_label.config(image=rock_img)
    elif choice == "paper":
        player_label.config(image=paper_img)
    else:
        player_label.config(image=scissor_img)


def play(user):
    global player_score, computer_score

    set_player(user)
    cpu = computer_choice()

    if user == cpu:
        show("Tie Match ")

    elif (user == "rock" and cpu == "scissor") or \
         (user == "paper" and cpu == "rock") or \
         (user == "scissor" and cpu == "paper"):

        player_score += 1
        show("You Win This Round ")

    else:
        computer_score += 1
        show("Computer Wins This Round ")

    update_score()

    if player_score == WIN_SCORE:
        show(" YOU WIN THE GAME ")
        stop_game()

    elif computer_score == WIN_SCORE:
        show(" COMPUTER WINS THE GAME!!!! ")
        stop_game()


#  BUTTONS 
btn_frame = Frame(main, bg="#1E293B")
btn_frame.pack(pady=20)

rock_btn = Button(btn_frame, text="Rock", width=12,
                  font=("Arial", 14),
                  command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = Button(btn_frame, text="Paper", width=12,
                   font=("Arial", 14),
                   command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissor_btn = Button(btn_frame, text="Scissor", width=12,
                     font=("Arial", 14),
                     command=lambda: play("scissor"))
scissor_btn.grid(row=0, column=2, padx=5)

#  RUN 
root.mainloop()