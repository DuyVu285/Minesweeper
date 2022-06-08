from msilib.schema import Property
from tkinter import Button
import random
from sympy import true
import settings
import ctypes

# Creating the cells
class Cell:
    all = []
    pressed_btn_list = []
    images = []
    removeChunk = []
    gameStep = []   # Keep track of player's move
    colour = {1: "blue", 2: "green", 3:"brown", 4:"purple", 5:"red", 6:"pink"}
    endgameflag = False
    
    # Constructor
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        self.is_opened = False
        self.is_flagged = False
        
        # Append the object to Cell.all list
        Cell.all.append(self)
        
    # Create the button for cell object
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=5,
            height=2,
        )
        btn.bind('<Button-1>',self.left_click_actions)  # Left Click
        btn.bind('<Button-3>',self.right_click_actions) # Right Click
        self.cell_btn_object = btn
        
    # Assign an event to the button
    def left_click_actions(self, event):
        if self.cell_btn_object['state'] == 'disabled':
            return
        if self.is_mine:
            Cell.gameStep.append(self)
            self.show_mine()
        else:
            self.show_cell()
            if (Cell.removeChunk):
                Cell.gameStep.append(Cell.removeChunk)
                Cell.removeChunk = []
            # If Mines count is equal to the cells left count, player won
            if ((settings.ROWS * settings.COLS) - int(len(Cell.all)*settings.MINES)) == len(list(set(Cell.pressed_btn_list))):
                self.end_game_phase()
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the game', 'Game Over', 0)
                
        # Cancel all events if cell is already opened:
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')
        
    def right_click_actions(self, event):
            self.create_flag()
    
    # Create flag
    def create_flag(self):
        if self not in Cell.pressed_btn_list:
            if self.cell_btn_object['state'] == 'normal':
                # Set flag img
                self.cell_btn_object.config(
                    image = Cell.images[2],
                    width= 37,
                    height= 35,
                    state ='disabled'
                )
                self.is_flagged = True
            elif self.cell_btn_object['state'] == 'disabled':
                # Disable flag img
                self.cell_btn_object.config(
                    image = '',
                    width= 5,
                    height= 2,
                    bg = 'SystemButtonFace',
                    state ='normal'
                )
                self.is_flagged = False
        else:
            pass

    # Display cell as mine    
    def show_mine(self):
        # A logic to interrupt the game and display a message that player lost
        for x in Cell.all:
            if x.is_mine == True:
                if(x.is_flagged == False):
                    x.cell_btn_object.config(
                        image=Cell.images[0],
                        width = 37,
                        height = 35,
                    )
                else:
                    x.cell_btn_object.config(
                        image=Cell.images[3],
                        width = 37,
                        height = 35,
                    )
            x.cell_btn_object.unbind('<Button-1>')
            x.cell_btn_object.unbind('<Button-3>')
            x.cell_btn_object.config(state = 'disabled')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine!', 'Game Over!', 0)

    # The undo function
    def undo():
        print(Cell.gameStep)
        if(not Cell.gameStep):
            ctypes.windll.user32.MessageBoxW(0, 'You cannot undo anymore!','Warning', 0)
        elif(Cell.endgameflag == True):
            ctypes.windll.user32.MessageBoxW(0, 'You has already won the game!','Warning', 0)
        else:
            if(isinstance(Cell.gameStep[-1],list)):
                for x in Cell.gameStep[-1]:
                    if(x.is_opened):
                        x.cell_btn_object.config(
                            text =""
                        )
                        x.is_opened = False
                        # Rebind the clicks
                        x.cell_btn_object.bind('<Button-1>',x.left_click_actions)
                        x.cell_btn_object.bind('<Button-3>',x.right_click_actions)
                        Cell.pressed_btn_list.remove(x)
                Cell.gameStep.pop()
            else:
                x = Cell.gameStep[-1]
                if(not x.is_mine):
                    if(x.is_flagged == False):
                        x.cell_btn_object.config(
                            text =""
                        )
                        x.is_opened = False
                        # Rebind the clicks
                        x.cell_btn_object.bind('<Button-1>',x.left_click_actions)
                        x.cell_btn_object.bind('<Button-3>',x.right_click_actions)
                        Cell.gameStep.pop()
                        Cell.pressed_btn_list.pop()
                else:
                    for x in Cell.all:
                        x.cell_btn_object.config(state = 'normal')
                        if x.is_mine == True:
                            if(x.is_flagged == False): 
                                x.cell_btn_object.config(
                                    image = '',
                                    width = 5,
                                    height = 2,
                                    bg = 'SystemButtonFace',
                                )
                                x.is_opened = False
                            else:
                                x.cell_btn_object.config(
                                    image = Cell.images[2],
                                    width = 37,
                                    height = 35,
                                )
                                x.is_opened = False
                                x.cell_btn_object.config(state = 'disabled')
                        else:
                            if(x.is_flagged == True):
                                x.cell_btn_object.config(
                                    image = Cell.images[2],
                                    width = 37,
                                    height = 35,
                                )
                                x.is_opened = False
                                x.cell_btn_object.config(state = 'disabled')
                        x.cell_btn_object.bind('<Button-1>',x.left_click_actions)
                        x.cell_btn_object.bind('<Button-3>',x.right_click_actions)
                    Cell.gameStep.pop()
            
    # Surrounded cells
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        # Remove all None in the list
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    # Surrounded mines
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        
        return counter
        
    # Show cell
    def show_cell(self):
        if self.surrounded_cells_mines_length == 0:
            self.cascade()
        else:
            self.cell_btn_object.config(
                text = self.surrounded_cells_mines_length,
                fg = Cell.colour.get(self.surrounded_cells_mines_length),
            )
            self.is_opened = True
            if (self not in Cell.removeChunk):
                Cell.gameStep.append(self)
            Cell.pressed_btn_list.append(self)
            
    # Cascade
    def cascade(self):
        if self not in Cell.pressed_btn_list:
            if (self not in Cell.removeChunk):
                Cell.removeChunk.append(self)
            Cell.pressed_btn_list.append(self)
            self.cell_btn_object.config(
                        text=self.surrounded_cells_mines_length,
                        fg = Cell.colour.get(self.surrounded_cells_mines_length),
            )
            self.is_opened = True
            for cell in self.surrounded_cells:
                if (cell not in Cell.removeChunk):
                    if(cell not in Cell.gameStep):
                        Cell.removeChunk.append(cell)
                        cell.show_cell()
                
    
    # Check if the adjacent cells are mines
    def get_cell_by_axis(self,x,y):
        # Return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    
    # Turn some cells into mines
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, int(len(Cell.all)*settings.MINES)
            )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        
    def __repr__(self):
        return f'Cell({self.x},{self.y})'
    
    # Getting images
    def get_images(a, b, c, d):
        Cell.images.append(a)
        Cell.images.append(b)
        Cell.images.append(c)
        Cell.images.append(d)

    # End game  
    def end_game_phase(self):
        Cell.endgameflag = True
        for x in Cell.all:
            if x.is_mine == True:
                    x.cell_btn_object.config(
                        image = Cell.images[1],
                        width = 37,
                        height = 35
                    )
            x.cell_btn_object.config(state = 'disabled')