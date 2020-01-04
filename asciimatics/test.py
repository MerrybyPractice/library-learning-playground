from asciimatics.screen import ManagedScreen, Screen
from time import sleep


def test(screen): 
    screen.clear()
    screen.print_at('Starting', 0, 0)
    screen.refresh()
    sleep(2)
    # screen.clear()
    screen.print_at('RED', 1, 1, Screen.COLOUR_RED)
    screen.refresh()
    sleep(2)
    # screen.clear()
    screen.print_at('YELLOW', 2, 2, Screen.COLOUR_YELLOW)
    screen.refresh()
    sleep(2)
    # screen.clear()
    screen.print_at('GREEN', 3, 3, Screen.COLOUR_GREEN)
    screen.refresh()
    sleep(2)
    # screen.clear()
    screen.print_at('CYAN', 4, 4, Screen.COLOUR_CYAN)
    screen.refresh()
    sleep(2)
    # screen.clear()
    screen.print_at('BLUE', 5, 5, Screen.COLOUR_BLUE)
    screen.refresh()
    sleep(2)
    # screen.clear()
    screen.print_at('MAGENTA', 6, 6, Screen.COLOUR_MAGENTA)
    screen.refresh()
    sleep(2)
    # screen.clear()
    screen.print_at('BLACK', 7, 7, Screen.COLOUR_BLACK)
    screen.refresh()
    
    screen.print_at('THAT WAS BLACK', 7, 7, Screen.COLOUR_MAGENTA)
    screen.refresh()
    sleep(2)
    # screen.clear()
    screen.print_at('WHITE', 8, 8, Screen.COLOUR_WHITE)
    screen.refresh()
    sleep(2)

    screen.print_at('BOLD', 9, 9, Screen.COLOUR_WHITE, Screen.A_BOLD)
    screen.refresh()
    sleep(2)

    screen.print_at('NORMAL', 10, 10, Screen.COLOUR_WHITE, Screen.A_NORMAL)
    screen.refresh()
    sleep(2)

    screen.print_at('REVERSE', 11, 11, Screen.COLOUR_WHITE, Screen.A_REVERSE)
    screen.refresh()
    sleep(2)

    screen.print_at('Underline', 12, 12, Screen.COLOUR_WHITE, Screen.A_UNDERLINE)
    screen.refresh()
    sleep(2)

    screen.print_at(u'☠️🧟☔︎ Testing out unicode output', 13, 13)
    screen.refresh()

    sleep(10)
    screen.clear()

Screen.wrapper(test)