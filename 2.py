from tkinter import *

bomb = 100
score = 0 
press_return = True

def read_best_score():
    try:
        with open("best_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def write_best_score(score):
    with open("best_score.txt", "w") as file:
        file.write(str(score))

best_score = read_best_score()

def start(event):
    global press_return
    global bomb
    global score
    global best_score

    if not press_return:
        pass
    else:
        bomb = 100
        score = 0
        label.config(text=f"Best Score: {best_score}\nPress [Enter] to start the game")
        update_bomb()
        update_point()
        update_point()
        update_display()
        press_return = False

def update_display():
    global score
    global bomb
    if bomb > 50:
        bomb_label.config(image=normal_photo)
    elif 0 < bomb < 50: 
        bomb_label.config(image=no_photo)
    else:
        bomb_label.config(image=bang_photo)
    fuse_label.config(text="Fuse: " + str(bomb))
    score_label.config(text="Score: " + str(score))
    fuse_label.after(100, update_display)

def update_point():
    global score
    score += 1
    if is_alive(best_score):
        score_label.after(3000, update_point)

def update_bomb():
    global bomb
    bomb -= 5
    if is_alive(best_score):
        fuse_label.after(400, update_bomb)

def click():
    global bomb
    if is_alive(best_score):
        bomb += 1

def is_alive(best_score):
    global bomb
    global press_return
    if bomb <= 0:
        if score > best_score:
            write_best_score(score)
        label.config(text=f"Bang! Bang! Bang!\nBest Score: {read_best_score()}\nPress [Enter] to start a new game")
        press_return = True
        return False
    else:
        return True

root = Tk()
root.title("Bang Bang!!!")
root.geometry("500x550")

label = Label(root, text=f"Best Score: {best_score}\nPress [Enter] to start the game", font=("Comic Sans MS", 12))
label.pack()

fuse_label = Label(root, text="Fuse: " + str(bomb),  font=("Comic Sans MS", 14))
fuse_label.pack()

score_label = Label(root, text="Score: " + str(score), font=("Comic Sans MS", 14))
score_label.pack()

normal_photo = PhotoImage(file="bomb_normal.gif")
no_photo = PhotoImage(file="bomb_no.gif")
bang_photo = PhotoImage(file="pow.gif")

bomb_label = Label(root, image=normal_photo)
bomb_label.pack()

click_button = Button(root, text="Click me", bg="red", command=click, font=("Comic Sans MS", 14), width=20)
click_button.pack()

root.bind('<Return>', start)

root.mainloop()
