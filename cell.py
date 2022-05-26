from tkinter import Button

# Creating the cells
class Cell:
    all = []
    # Constructor
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        
        # Append the object to Cell.all list
        Cell.all.append(self)
    # Create the button for cell object
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text = f'{self.x},{self.y}'
        )
        btn.bind('<Button-1>',self.left_click_actions)  # Left Click
        btn.bind('<Button-3>',self.right_click_actions) # Right Click
        self.cell_btn_object = btn
        
    # Assign an event to the button
    def left_click_actions(self, event):
        print(event)
        print("I am left clicked!") 
        
    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")
        
    # Turn some cells into mines
    @staticmethod
    def randomize_mines():
        pass
    def __repr__(self):
        return f'Cell({self.x},{self.y}'