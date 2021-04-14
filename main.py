from tkinter import *
import math

       # ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 1
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    start_timer()


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    check_count = int(reps/2)+1
    if reps == 0:
        check_mark.config(text=" ")

    if reps == 7 :
        countdown(LONG_BREAK_MIN*60)
        timer.config(text="Break",fg=RED)
        check_mark.config(text=check_count * "✔")
        reps = 0
        return

    elif reps % 2 == 0:
        countdown(WORK_MIN*60)
        timer.config(text="Work",fg=GREEN)

    else:
        countdown(SHORT_BREAK_MIN*60)
        timer.config(text="Break", fg=PINK)
        check_mark.config(text=check_count * "✔")
    reps += 1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minute = int(count/60)
    second = count%60
    if second < 10:
        second = f"0{second}"
    if count > -1:
        canvas.itemconfig(timer_text, text=f"{minute}:{second}")
        canvas.after(1000, countdown, count-1)
    else:
        start_timer()







# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomata_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomata_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white',font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

timer = Label(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
timer.grid(row=1, column=2)




start = Button(text="Start", command=start_timer)
start.grid(row=3, column=1)

reset = Button(text="Reset", command=reset_timer)
reset.grid(row=3, column=3)

check_mark = Label(text="",font=(FONT_NAME, 20) ,fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=2)

window.mainloop()