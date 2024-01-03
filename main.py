from tkinter import *

user_text = ""
timer = None


def start(event):
    global timer, user_text

    if timer is not None:
        window.after_cancel(timer)

    if event.keysym == "BackSpace":
        user_text = user_text[0: len(user_text) - 1]

    elif event.char:
        user_text += event.char
        timer = window.after(5000, reset_app)

    return


def reset_app():
    global timer, user_text
    typing_area.delete('1.0', 'end')
    user_text = ""
    timer = None
    return


FG = '#F6F4EB'
BG = "#749BC2"

FONT = ("Arial", 30, "bold")

window = Tk()
window.title('Disappearing Text Desktop App')
window.geometry("1300x600")
window.config(padx=10, pady=10)

typing_area = Text(font=FONT, bg=BG, fg=FG, highlightthickness=0, padx=5, pady=5, width=300)
typing_area.bind('<KeyPress>', start)
typing_area.grid(row=3, column=0, columnspan=3)

window.mainloop()
