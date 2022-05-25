from ctypes import util
from tkinter import *
import settings
import utils

# Create game window
root = Tk()
root.configure(bg = 'black')
root.geometry(f'{settings.width}x{settings.height}')
root.title('Minesweeper Game')
root.resizable(True, True)

# Divide the game window into sections
top_frame = Frame(
    root,
    bg = 'red', # Change later to black
    width = settings.width,
    height = utils.height_prct(25)
)
top_frame.place(x=0, y=0)


left_frame = Frame(
    root,
    bg = 'blue', # Change later to black
    width = utils.width_prct(25),
    height = utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg = 'green', # Change later to black
    width = utils.width_prct(75),
    height = utils.height_prct(75)
)
center_frame.place(x=utils.width_prct(25),y=utils.height_prct(25))

# Designing the button (click on the cells)
btn1 = Button(
    center_frame,
    bg = 'blue',
    text = 'First Button'
)
btn1.place(x=0,y=0)

# Run the window
root.mainloop()

