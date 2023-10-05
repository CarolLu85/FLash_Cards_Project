import random
from tkinter import *
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

# reading csv
try:
    data = pandas.read_csv("word_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # do a comparison with data.to_list and data.to_dict(orient="records")
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(f_words, text=current_card["French"])
    canvas.itemconfig(title_word, text="French")
    canvas.itemconfig(image, image=f_card)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(f_words, text=current_card["English"])
    canvas.itemconfig(image, image=b_card)
    canvas.itemconfig(title_word, text="English")


def remove_data():
    to_learn.remove(current_card)
    # save to a new file after known items removed as a csv file called "word_to_learn" for next time reading this file.
    data = pandas.DataFrame(to_learn)
    data.to_csv("word_to_learn.csv", index=False)



# window setup
window = Tk()
window.title("Flash Cards")
# window.minsize(width=800, height=526)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
f_card = PhotoImage(file="card_front.png")
b_card = PhotoImage(file="card_back.png")
image = canvas.create_image(400, 263, image=f_card)
title_word = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
f_words = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "italic"))
canvas.grid(column=0, row=0, columnspan=2)


cross_image = PhotoImage(file="wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)

tick_image = PhotoImage(file="right.png")
tick_button = Button(image=tick_image, highlightthickness=0,command=remove_data)
tick_button.grid(column=1, row=1)






next_card()
window.mainloop()



# my code
# raw_data = pandas.read_csv("french_words.csv")
# french_data = raw_data["French"].to_list()
# english_data = raw_data["English"].to_list()

# def french_word():
#     word = random.choice(french_data)
#     canvas.itemconfig(f_words, text=word)
#     canvas.itemconfig(title_word, text="French")
#     window.after(3000, english_word)


# def english_word():
#     canvas.create_image(400, 264, image=b_card)
#     canvas.grid(column=0, row=0, columnspan=2)
#     e_word = random.choice(english_data)
#     canvas.itemconfig(f_words, text=e_word)
#     canvas.itemconfig(image, image=b_card)
#     canvas.itemconfig(title_word, text="English")