from PIL import ImageTk
from tkinter import *
from PIL import Image
from cell import Cell
import settings
import utils

class GameWindow():
# Create game window
    def main():
        root = Tk()
        root.configure(bg = 'grey')
        root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
        root.title('Minesweeper Game')
        root.resizable(True, True)

        # Getting the images resources
        mine_img_path = 'images\mine.ico'
        mine_img = Image.open(mine_img_path)
        mine_img = mine_img.resize((37, 35))
        mine_img = ImageTk.PhotoImage(mine_img)
        
        smiley_img_path = 'images\smiley.png'
        smiley_img = Image.open(smiley_img_path)
        smiley_img = smiley_img.resize((37, 35))
        smiley_img = ImageTk.PhotoImage(smiley_img)
        
        flag_img_path = 'images\plag.png'
        flag_img = Image.open(flag_img_path)
        flag_img = flag_img.resize((37, 35))
        flag_img = ImageTk.PhotoImage(flag_img)
        
        check_img_path = 'images\check.jpg'
        check_img = Image.open(check_img_path)
        check_img = check_img.resize((37, 35))
        check_img = ImageTk.PhotoImage(check_img)
        
        # Divide the game window into frame sections
        top_frame = Frame(
            root,
            bg = 'black', 
            width = settings.WIDTH,
            height = utils.height_prct(25)
        )
        top_frame.place(x=0, y=0)

        left_frame = Frame(
            root,
            bg = 'black', 
            width = utils.width_prct(25),
            height = utils.height_prct(75)
        )
        left_frame.place(x=0, y=utils.height_prct(25))

        center_frame = Frame(
            root,
            bg = 'grey', 
            width = utils.width_prct(75),
            height = utils.height_prct(75)
        )
        center_frame.place(x=utils.width_prct(25),y=utils.height_prct(25))

        # Game title
        game_title = Label(
            top_frame,
            bg ='black',
            fg ='white',
            text ='Minesweeper Game',
            font =('', 48)
        )

        game_title.place(
            x=utils.width_prct(25), y= utils.height_prct(5)
            )
        # Desgin the scroll buttons to set difficulty
        no_mines_scale_value = IntVar()
        no_mines_scale = Scale(
            left_frame, 
            label = 'Mines %',
            from_= 5, 
            to_= 90, 
            variable =no_mines_scale_value,
            orient=HORIZONTAL, 
            length= 100
        )
        no_mines_scale.place(x=0, y=0)
        no_mines_scale.set(settings.MINES*100)
        
        rows_scale_value = IntVar()
        rows_scale = Scale(
            left_frame, 
            label = 'Rows',
            from_= 6, 
            to_= 13, 
            variable =rows_scale_value,
            orient=HORIZONTAL, 
            length= 100
        )
        rows_scale.place(x=110, y=0)
        rows_scale.set(settings.ROWS)

        
        cols_scale_value = IntVar()
        cols_scale = Scale(
            left_frame, 
            label = 'Columns',
            from_= 6, 
            to_= 24, 
            variable =cols_scale_value,
            orient=HORIZONTAL, 
            length= 100
        )
        cols_scale.place(x=220, y=0)
        cols_scale.set(settings.COLS)
        
        # Designing the button for New game and Apply changes
        # Apply button
        apply_btn = Button(
            left_frame,
            text = 'Apply',
            command = lambda:settings.apply(
                no_mines_scale_value.get(),
                rows_scale_value.get(),
                cols_scale_value.get(),
            ),
            padx = 70,
            pady = 20
        )
        apply_btn.place(x=0, y=140)
        
        # New game button to refresh mainloop()
        new_game_btn = Button(
            left_frame,
            text = 'New \n Game',
            command=lambda: refresh(root),
            padx = 70,
            pady = 10
        )
        new_game_btn.place(x=0,y=70)

        # Undo button
        undo_btn = Button(
            left_frame,
            text = 'Undo',
            command=lambda: undo(root),
            padx = 70,
            pady = 10
        )
        undo_btn.place(x=0,y=210)
        
        # The cell
        for x in range(settings.COLS):
            for y in range(settings.ROWS):
                c = Cell(x, y)
                c.create_btn_object(center_frame)
                c.cell_btn_object.grid(
                    column=x, row=y
                )

        # Get cell images
        
        Cell.get_images(mine_img, smiley_img, flag_img, check_img)
        # Randomize the mines
        Cell.randomize_mines()

        # Run the window
        root.mainloop()

# Refresh
def refresh(location):
    location.destroy()
    Cell.all = []
    Cell.gameStep = []
    Cell.pressed_btn_list = []
    Cell.images = []
    settings.frame_change()
    GameWindow.main()

# Undo
def undo(location):
    Cell.undo()

