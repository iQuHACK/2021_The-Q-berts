import pyglet

pyglet.resource.path = ['../images']
pyglet.resource.reindex()

player_image = pyglet.resource.image("q.png")
bullet_image = pyglet.resource.image("bullet.png")
asteroid_image = pyglet.resource.image("asteroid.png")

window = pyglet.window.Window()
from pyglet.window import key

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        print("The left arrow key was pressed")
    else:
        print('A key was pressed')
        
pyglet.app.run()
