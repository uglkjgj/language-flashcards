from home_page import HomePage
from practice import Practice
from translate import Translate
from exit import Exit

running = True

def reset():
    home = HomePage()
    if home.clicked:
        data = Translate(home.open_sesime()[0], home.open_sesime()[1]).get_info()
        practice = Practice(data, home.open_sesime()[0], home.open_sesime()[1])

    if practice.complete:
        ex = Exit(practice.done()[0], practice.done()[1], practice.done()[2], practice.done()[3], practice.done()[4],
                  practice.done()[5])

    if ex.complete:
        reset()

while running:
    home = HomePage()

    if home.exit:
        running = False

    if home.clicked:
        data = Translate(home.open_sesime()[0], home.open_sesime()[1]).get_info()
        practice = Practice(data, home.open_sesime()[0], home.open_sesime()[1])

    if practice.complete:
        ex = Exit(practice.done()[0], practice.done()[1], practice.done()[2], practice.done()[3], practice.done()[4], practice.done()[5])

    if ex.complete:
        reset()

