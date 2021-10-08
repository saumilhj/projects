from tkinter import Tk, Text, Label, END, WORD, messagebox
from ttkbootstrap import Style
from paragraph import paragraphs
from random import randint

COUNT = -1
TIME_COUNT = FULL_TIME = 10
FIRST_PRESS = 0
CHARS_ENTERED = []

# Functions
def speed_count():
    user_input = "".join(CHARS_ENTERED)
    num_words = len(user_input.split(" "))
    words_per_min = int(num_words // (FULL_TIME / 60))
    messagebox.showinfo(title="Result", message=f"Your typing speed is {words_per_min} wpm.")
    window.destroy()


def start_time():
    global TIME_COUNT
    mnt = TIME_COUNT // 60
    sec = TIME_COUNT % 60
    if sec < 10:
        counter.config(text=f"{mnt}:0{sec}")
    else:
        counter.config(text=f"{mnt}:{sec}")
    TIME_COUNT -= 1
    if TIME_COUNT < 0:
        window.after_cancel(start_time)
        window.unbind("<Key>")
        speed_count()
    else:
        window.after(1000, start_time)


def key_press(event):
    global COUNT, FIRST_PRESS
    FIRST_PRESS += 1
    if FIRST_PRESS == 1:
        start_time()
    special_keys = ["Shift_L", "Shift_R", "Tab", "Alt_L", "Alt_R", "Caps_Lock", "Control_L", "Control_R"]
    if event.keysym in special_keys:
        pass
    elif event.keysym == "BackSpace" and COUNT >= -1:
        type_text.tag_add(f"hlt_{COUNT}", f"1.{COUNT}", f"1.{COUNT + 1}")
        type_text.tag_config(f"hlt_{COUNT}", background="white")
        COUNT -= 1
    else:
        COUNT += 1
        type_text.tag_config(f"hlt_{COUNT}", background="green")
        if event.char == type_text.get(f"1.{COUNT}", f"1.{COUNT + 1}"):
            type_text.tag_add(f"hlt_{COUNT}", f"1.{COUNT}", f"1.{COUNT + 1}")
            type_text.tag_config(f"hlt_{COUNT}", background="green")
            CHARS_ENTERED.append(event.char)
        else:
            type_text.tag_add(f"hlt_{COUNT}", f"1.{COUNT}", f"1.{COUNT + 1}")
            type_text.tag_config(f"hlt_{COUNT}", background="red")


sample_text = paragraphs[randint(0, 2)]

# Window configuration
window = Tk()
style = Style(theme="cosmo")
window.geometry("600x400")
window.title("Typing Test")
window.config(padx=20, pady=20)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=10)
window.grid_columnconfigure(0, weight=1)
window.bind("<Key>", key_press)

# Text
type_text = Text(window, wrap=WORD, font=("Courier", 12))
type_text.insert(END, sample_text)
type_text.config(state="disabled")
type_text.grid(row=1, column=0, pady=4, sticky="EW")

# Counter
counter = Label(window, text="0:00", font=("Courier", 12))
counter.grid(row=0, column=0, pady=4, sticky="E")
window.mainloop()
