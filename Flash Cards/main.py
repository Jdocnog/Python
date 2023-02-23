from tkinter import *
import pandas
import random

#---------------------------------Functional Code----------------------------------------
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


#creates new card, changing the words chosen from the data frame.
def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer) #Cancels the flip timer when a new_word is pulled
    current_card = random.choice(to_learn) # Shape gets num rows
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card) # after 3 seconds will run Flip Card which changes shows the English
                                                    # version of the french word.
#below was my code that worked, but took up a lot of space, commented out once I saw the Orient Records option
    # random_french_word = df["French"][random_card]
    # english_word = df["English"][random_card]
    # french_eng_words = (random_french_word, english_word)
    # canvas.delete("french_word")
    # canvas.create_text(400, 263, text=random_french_word, font=("Ariel", 60, "bold"), tags="french_word")
    # return french_eng_words

#Will update the flash card to the english side
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def word_known():
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    new_word()

#-----------------------------------UI SETUP----------------------------------


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#creates the canvas we use
canvas = Canvas(width=800, height=526)
canvas.configure(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0, columnspan=2)

#creates all the images needed for the flash cards
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

#choose initial words to display
# both_words = new_word()

#Creates Initial Card
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), tags="french_word")

#Creates Checkmark button
correct_button = Button(image=right_img, highlightthickness=0, command=word_known)
correct_button.grid(column=1, row=1)

#Creates X button
incorrect_button = Button(image=wrong_img, highlightthickness=0, command=new_word)
incorrect_button.grid(column=0, row=1)

#Adds first word to initial card
new_word()



window.mainloop()