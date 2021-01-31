#insert code here
import numpy as np
import ipywidgets as widgets
from IPython.display import display
import Pyglet
import random

window=pyglet.window.Window()

  

pyglet
pyglet.resource.path = ["images"]
pyglet.resource.reindex()


@window.event
def on_draw():
  window.clear()
  
 

def on_close():
  window.close()
  quit()

  
  
  
pyglet.app.run()
