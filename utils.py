import settings
from tkinter import *
from PIL import ImageTk, Image

# Divide height and with percentage for ease of usage
def height_prct(percentage):
    return (settings.HEIGHT/100)*percentage

def width_prct(percentage):
    return (settings.WIDTH/100)*percentage


