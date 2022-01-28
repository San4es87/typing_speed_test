from tkinter import *
import math
import tkinter as tk


WORK_MIN = 1
FONT_NAME = "Courier"
reps = 1
timer = None

# ---------------------------- Create Text ------------------------------- #

text_word = "after, again, air, also, America, animal, another, answer, any, around, ask, away, back, because, before," \
            " big, boy, came, change, different, does, end, even, follow, form, found, give, good, great, hand, help, " \
            "here, home, house, just, kind, know, land, large, learn, letter, line, little, live, man, me, means, men, " \
            "most, mother, move, much, must, name, need, new, off, old, only, our, over, page, picture, place, play, " \
            "point, put, read, right, same, say, sentence, set, should, show, small, sound, spell, still, study, such," \
            " take, tell, things, think, three, through, too, try, turn, us, very, want, well, went, where, why, work, " \
            "world, years"

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():

    work_sec = WORK_MIN * 60
    count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_words():
    inp = text.get(1.0, "end-1c")
    count = len(inp.split())
    lbl.config(text="words-per-minute (WPM): " + str(count) + " / minute")

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = root.after(1000, count_down, count - 1)
    if count == 0:
        count_words()


# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Typing Speed Test")
root.config(padx=50, pady=50)
root.geometry("1000x800")

logo_label = Label(root,
                   text="Typing Speed Test", font=("Arial", 25))
logo_label.pack()

var = StringVar()
label = Label( root, underline = 2, wraplength = 550, textvariable = var, font=("Arial", 12),fg='blue')
var.set(text_word)
label.pack()
variable1=StringVar() # Value saved here


text = Text(root, width=50, height=10,
           font="Arial 14",
           wrap=WORD)

text.pack()

start_button = Button(text="Start", width=8, command=start_timer)
start_button.pack()

canvas = Canvas(width=100, height=100)
timer_text = canvas.create_text(55, 20, text="1:00", fill="black", font=(FONT_NAME, 15, "bold"))
canvas.pack()

# Label Creation
lbl = tk.Label(root, text="")
lbl.pack()

root.mainloop()
