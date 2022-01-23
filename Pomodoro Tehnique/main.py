from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetition = 0
check = '✓'
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text='00:00')
    # title_label 'Timer'
    text_label.configure(text='Timer')
    # reset check_marks
    check_text.configure(text='')
    global repetition, check
    repetition = 0
    check = '✓'
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repetition, check
    repetition += 1
    if repetition == 8:
        count_down(LONG_BREAK_MIN * 60)
        text_label.config(text='BREAK',fg=RED)
        print('hello')
        check += '\n'
        check_text.configure(text=check)
        print('hy', check, repetition)
        check += '✓'
    elif repetition%2==0:
        count_down(SHORT_BREAK_MIN * 60)
        text_label.config(text='BREAK',fg=PINK)
        check_text.configure(text=check)
        print('hy', check,repetition)
        check += '✓'
    else:
        count_down(WORK_MIN * 60)
        text_label.config(text='WORK',fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_sec = count%60
    count_min = int((count-count_sec)/60)

    if count_sec in range(0, 10):
        count_sec = '0{}'.format(count_sec)

    canvas.itemconfig(timer_text, text='{}:{}'.format(count_min, count_sec))

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)

text_label = Label(text='Timer',font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
text_label.grid(row=0,column=1)

check_text = Label(font=(FONT_NAME,20,'bold'),fg=GREEN,bg=YELLOW)
check_text.grid(row=3,column=1)

start_button = Button(text='Start',highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text='Reset',highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)

canvas= Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img =PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)

window.mainloop()