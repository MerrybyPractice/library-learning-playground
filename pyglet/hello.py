import pyglet
import os
from pyglet.window import mouse

print(os.getcwd())
window = pyglet.window.Window()
image = pyglet.image.load('assets/salemnoir.jpeg')

label = pyglet.text.Label('Hello, Salem', font_name='Times New Roman', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
label_two = pyglet.text.Label('Goodbye, Space Cat', font_name='Helvetica', font_size=24, x=window.width//1.5, y=window.height//1.5, anchor_x='left', anchor_y='bottom') 

window.push_handlers(pyglet.window.event.WindowEventLogger())

@window.event 
def on_draw(): 
    window.clear()
    image.blit(-20,-500)

@window.event
def on_key_press(symbol, modifiers): 
    on_draw()
    label.draw()
    print('Key Press')

@window.event
def on_mouse_press(x, y, button, modifiers): 
    # not drawing dynamically need to figure out why
    print('Mouse Press')
    if button == mouse.LEFT: 
        image.blit(-20,-500)
    if button == mouse.RIGHT: 
        image.blit(-20,-500)
        label_two.draw()

pyglet.app.run()

