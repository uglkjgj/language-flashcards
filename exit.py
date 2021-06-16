from tkinter import *
from translate import Translate
from tkinter import messagebox

ORANGE = "#ffcb91"
BACKGROUND_COLOR = "#B1DDC6"


class Exit(object):

    def __init__(self, lang, skill, data, right, done, score):
        self.complete = False
        self.lang = lang
        self.skill = skill
        self.data = data
        self.right_list = right

        self.window = Tk()
        self.window.title(f'{lang.capitalize()} {skill.capitalize()} Practice Complete')
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

        self.equalizer = Canvas(width=80, height=80, highlightthickness=0, bg=BACKGROUND_COLOR)
        equalizer = PhotoImage(file="images/equalizer.png")
        self.equalizer.create_image(40, 40, image=equalizer)
        self.equalizer.grid(row=0, column=0)

        self.home = Canvas(width=80, height=80, highlightthickness=0, bg=BACKGROUND_COLOR)
        home = PhotoImage(file="images/home.png")
        home_img = self.home.create_image(40, 40, image=home)
        self.home.grid(row=0, column=2)
        self.home.tag_bind(home_img, "<Button-1>", lambda home: self.go_home(True))

        self.canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
        self.card_front = PhotoImage(file="images/card_front.png")
        self.canvas_img = self.canvas.create_image(400, 263, image=self.card_front)
        self.canvas.create_text(400, 200,text=f"You got {score}/{done}.", font=("Courier", 40), fill=ORANGE)
        self.canvas.create_text(400, 300, text="Click on the trash can to", font=("Courier", 20), fill=ORANGE)
        self.canvas.create_text(400, 350, text="remove words you got from the database.", font=("Courier", 20), fill=ORANGE)

        self.canvas.grid(row=1, column=1)

        self.trash = Canvas(width=80, height=80, highlightthickness=0, bg=BACKGROUND_COLOR)
        trash = PhotoImage(file="images/trash.png")
        trash_img = self.trash.create_image(40, 40, image=trash)
        self.trash.grid(row=2, column=1)
        self.trash.tag_bind(trash_img, "<Button-1>", lambda remove: self.remove(True))

        self.window.mainloop()

    def remove(self, do):
        if do:
            new_dict = self.data
            for i in self.right_list:
                if self.lang == "mandarin":
                    del new_dict["Character"][str(i)]
                    del new_dict["Pinyin"][str(i)]
                    del new_dict["English"][str(i)]

                else:
                    del new_dict["French"][str(i)]
                    del new_dict["English"][str(i)]

            Translate(self.lang, self.skill).reset_data(new_dict)
            messagebox.showinfo('Database Updated', 'The words you know have been removed from the database')

    def go_home(self, do):
        if do:
            self.complete = True
            self.window.destroy()
