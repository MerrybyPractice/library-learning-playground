from asciimatics.screen import ManagedScreen
from asciimatics.scene import Scene
from time import sleep

@ManagedScreen
def demo(screen=None): 
    screen.print_at('Hello world!', 0, 0)
    screen.refresh()
    sleep(10)

demo()

def demo_two(): 
    with ManagedScreen() as screen: 
        screen.print_at('Hello world!', 0, 0)
        screen.refresh()
        sleep(10)
demo_two()
