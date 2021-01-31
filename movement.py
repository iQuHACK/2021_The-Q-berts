import sys
!{sys.executable} -m pip install pyglet

import pyglet

pyglet.resource.path = ["images"]
pyglet.resource.reindex()

player_image = pyglet.resource.image("qbert.PNG")

window = pyglet.window.Window()
from pyglet.window import key
from window import resources

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
    
center_image(player_image)

@window.event
def on_draw():
    player_qbert = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)

x1_change = 0
y1_change = 0

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
