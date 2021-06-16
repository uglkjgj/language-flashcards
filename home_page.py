from tkinter import *
from tkinter import messagebox


YELLOW = "#ffefa1"
ORANGE = "#ffcb91"
BLUE = "#94ebcd"
GREEN = "#6ddccf"
BACKGROUND_COLOR = "#B1DDC6"


class HomePage(object):

    def __init__(self):
        self.exit = False
        self.clicked = False
        self.window = Tk()
        self.window.title('Home')
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

        self.exit = Canvas(width=60, height=40, highlightthickness=0, bg=BACKGROUND_COLOR)
        exit = PhotoImage(file="images/smallclose.png")
        exit_img = self.exit.create_image(15, 15, image=exit)
        self.exit.grid(row=0, column=0)
        self.exit.tag_bind(exit_img, "<Button-1>", lambda remove: self.close_whole(True))


        self.heading = Label(text="Languages", font=("Courier", 40), fg=GREEN, bg=BACKGROUND_COLOR, padx=20, pady=20)
        self.heading.grid(row=0, column=0, columnspan=2)

        self.language_cards()

        self.selected_language = ""

        self.window.mainloop()

    def language_cards(self):
        self.french_button = Button(text="French", highlightbackground=ORANGE, fg=GREEN, height=5, width=30,
                                    highlightthickness=0, command=lambda: self.open_lang("french"))
        self.french_button.grid(row=1, column=0)

        self.french_options = Frame(self.window)
        self.french_nouns = Button(self.french_options, text="French nouns", highlightbackground=ORANGE, fg=BLUE,
                                   height=3, width=20,
                                   highlightthickness=0, command=lambda: self.open_new_window("french", "nouns"))
        self.french_nouns.grid(row=0, column=0)
        self.french_1000 = Button(self.french_options, text="1000 French words", fg=BLUE, height=3, width=20,
                                  highlightthickness=0,
                                  command=lambda: self.under_construction("French 1000 most frequent words"))
        self.french_1000.grid(row=0, column=1)
        self.french_options.grid_forget()

        self.mandarin_button = Button(text="Mandarin", highlightbackground=ORANGE, fg=GREEN, height=5, width=30,
                                      highlightthickness=0, command=lambda: self.open_lang("mandarin"))
        self.mandarin_button.grid(row=1, column=1)

        self.mandarin_options = Frame(self.window)
        self.mandarin_begineer = Button(self.mandarin_options, text="Begineer Mandarin", highlightbackground=ORANGE,
                                        fg=BLUE, height=3, width=20,
                                        highlightthickness=0,
                                        command=lambda: self.open_new_window("mandarin", "beginner"))
        self.mandarin_begineer.grid(row=0, column=0)
        self.mandarin_elementary = Button(self.mandarin_options, text="Elementary Mandarin", highlightbackground=ORANGE,
                                          fg=BLUE, height=3, width=20,
                                          highlightthickness=0,
                                          command=lambda: self.open_new_window("mandarin", "elementary"))
        self.mandarin_elementary.grid(row=0, column=1)
        self.mandarin_nouns = Button(self.mandarin_options, text="Mandarin nouns", highlightbackground=ORANGE, fg=BLUE,
                                     height=3, width=40,
                                     highlightthickness=0, command=lambda: self.open_new_window("mandarin", "nouns"))
        self.mandarin_nouns.grid(row=1, column=0, columnspan=2)
        self.mandarin_options.grid_forget()

    def open_lang(self, lang):
        if lang == "mandarin":
            self.french_options.grid_forget()
            self.hide_skills("mandarin")
        elif lang == "french":
            self.mandarin_options.grid_forget()
            self.hide_skills("french")

    def open_new_window(self, lang, skill):
        self.clicked = True
        self.lang = lang
        self.skill = skill
        messagebox.showinfo('Start Practice', '100 words would be used for practice click exit when you dont want to continue')
        self.window.destroy()

        #data = Translate(lang, skill).get_info()
        #practice = Practice(data, lang, skill)

    def open_sesime(self):
        return [self.lang, self.skill]

    def under_construction(self, lang):
        messagebox.showinfo("Under Construction", f"The {lang} page is still under construction.")

    def hide_skills(self, lang):
        if lang == "french":
            required = self.french_options
            row, column = 2, 0
        else:
            required = self.mandarin_options
            row, column = 2, 1
        if not required.winfo_viewable():
            required.grid(row=row, column=column)
        else:
            required.grid_forget()

    def close_whole(self, do):
        if do:
            self.exit = True
            self.window.destroy()
