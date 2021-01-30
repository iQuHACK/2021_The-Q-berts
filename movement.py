import pyglet

pyglet.resource.path = ['../images']
pyglet.resource.reindex()

player_image = pyglet.resource.image("qbert.png")

window = pyglet.window.Window()
from pyglet.window import key

class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        x1_change = -10
        y1_change = 0
    elif symbol == key.RIGHT:
        x1_change = 10
        y1_change = 0
    elif symbol == key.DOWN:
        y1_change = -10
        x1_change = 0
    elif symbol == key.UP:
        y1_change = 10
        x1_change = 0
        
pyglet.app.run()
