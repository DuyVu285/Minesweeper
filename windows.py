from tkinter import *

# Create game window
root = Tk()
root.configure(bg = 'black')
root.geometry('1440x720')
root.title('Minesweeper Game')
root.resizable(True, True)

# Divide the game window into sections
top_frame = Frame(
    root,
    bg = 'red', # Change later to black
    width = 1440,
    height = 180
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg = 'blue', # Change later to black
    width = 360,
    height = 540
)
left_frame.place(x=0, y=200)
# Divide the game window into sections
root.mainloop()
