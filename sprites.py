import pyglet
import random

avatar_image = pyglet.resource.image("qbert")

def center_image(image):
  image.anchor_x = image.width//2
  image.anchor_y = image.height//2

center_image(avatar_image)

class Avatar(pyglet.window.Window):
  def __init__(self):
    super(Avatar, self).__init__()
    self.scale=1
    self.image=pyglet.resource.image("qbert.png")
    
    
