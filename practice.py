from tkinter import *
import random
from exit import Exit

BACKGROUND_COLOR = "#B1DDC6"
ORANGE = "#ffcb91"


class Practice:

    def __init__(self, data, lang, skill):

        self.complete = False
        self.data = data
        self.lang = lang
        self.skill = skill
        self.right_list = []

        self.the_item = None
        self.right_count = 0
        self.count = 0
        self.num = 0

        self.window = Tk()
        self.window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)
        self.window.title(f"Practice {lang.capitalize()}")

        self.exit = Canvas(width=80, height=80, highlightthickness=0, bg=BACKGROUND_COLOR)
        close_image = PhotoImage(file="images/close.png")
        self.exit_image = self.exit.create_image(40, 40, image=close_image)
        self.exit.grid(row=0, column=0)
        self.exit.tag_bind(self.exit_image, "<Button-1>", lambda close: self.close(True))

        self.canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

        self.card_front = PhotoImage(file="images/card_front.png")
        self.card_back = PhotoImage(file="images/card_back.png")

        self.canvas_img = self.canvas.create_image(400, 263, image=self.card_front)
        self.canvas_text = self.canvas.create_text(400, 200, font=("Courier", 45), fill=ORANGE)
        self.canvas.grid(row=1, column=1)

        self.next_card(False)

        self.tick = Canvas(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR)
        tick_image = PhotoImage(file="images/right.png")
        self.tick_image = self.tick.create_image(50, 50, image=tick_image)
        self.tick.grid(row=2, column=2)
        self.tick.tag_bind(self.tick_image, "<Button-1>", lambda right: self.next_card(True))

        self.cross = Canvas(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR)
        cross_image = PhotoImage(file="images/wrong.png")
        self.cross_image = self.cross.create_image(50, 50, image=cross_image)
        self.cross.grid(row=2, column=0)
        self.cross.tag_bind(self.cross_image, "<Button-1>", lambda wrong: self.next_card(False))

        self.window.mainloop()

    def flip_card(self):
        self.canvas.itemconfig(self.canvas_img, image=self.card_back)
        self.canvas.itemconfig(self.canvas_text, text=self.back_text)

    def next_card(self, solution):
        if solution is True:
            self.right_count += 1
            self.count += 1
            self.right_list.append(self.num)

        if solution is False and self.the_item is not None:
            self.count += 1

        self.num = random.randint(1, len(self.data['English']))
        if self.lang == "mandarin":
            self.the_item = {
                "Character": self.data["Character"][str(self.num)],
                "Pinyin": self.data["Pinyin"][str(self.num)],
                "English": self.data["English"][str(self.num)]
            }
            self.front_text = f"{self.the_item['Character']} - {self.the_item['Pinyin']}"
            self.back_text = f"{self.the_item['English']}"
        else:
            self.the_item = {
                "French": self.data["French"][str(self.num)],
                "English": self.data["English"][str(self.num)]
            }
            self.front_text = f"{self.the_item['French']}"
            self.back_text = f"{self.the_item['English']}"

        self.canvas.itemconfig(self.canvas_img, image=self.card_front)
        self.canvas.itemconfig(self.canvas_text, text=self.front_text)

        self.window.after(5000, self.flip_card)

    def close(self, do):
        if do:
            self.complete = True
            self.window.destroy()
            #ex = Exit(self.lang, self.skill, self.data, self.right_list, self.count, self.right_count)

    def done(self):
        return [self.lang, self.skill, self.data, self.right_list, self.count, self.right_count]