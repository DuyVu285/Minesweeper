# DSAProject
The DSA project- Minesweeper Game by Vu Nhat Duy IT IU

DSA project of designing Minesweeper Game with OOP using python.

  	What is Minesweeper?
  
Minesweeper is a single-player puzzle video game. The objective of the game is to clear a rectangular board containing hidden "mines" or bombs without detonating any of them, with help from clues about the number of neighboring mines in each field.

	How to play Minesweeper
	
- The principles behind Minesweeper: each Minesweeper game starts with a grid of unmarked squares(or in this case we call it cells). After clicking one of these squares, it is either a safe cell which holds a number or a “mine” cell that indicates player’s loss. It's player job to make use of the numbers to figure out which of the blank cells have mines and which are safe to click.
- Mouse's left and right buttons: the mouse is the only tool that player needs in order to play Minesweeper. The left mouse button is used to click squares to show whether it is a mine or a safe square, while the right mouse button is used to flag cells that contain mines.
- The meaning of the numbers: a number on a cell refers to the number of mines that are currently neighboring that cell. For example, if there the cell has the number 1 on it, you know that the cells surrounding it has a mine hidden beneath one of them.
- Win condition: player have clicked all the safe cells without triggering any mines.
- 
	Features:
	
- Clear unnecessary cells: When the left click event occurs, the open property is set to true, and the surrounding mines are also checked. If the value is 0, then use recursion to open the surrounding cells. The recursion stops when the value is not 0. For example, the player hits a 0 cell, unimportant cells are opened. To find the code, find surrounded_cells functions in cell.py.
- Flagging mines: If player is not sure of a specific cell, you can flag with right-click to avoid it until later. Player can undo by right-clicking it once again to make it becomes a normal cell. To find the code, find create_flag function in cell.py.
- Undo feature: For undo feature, the properties of Stack are considered, which take advantages of the “last in first out” property to undo the player’s most recent steps by “popping” it out of the Stack. When the user left-clicks a number or an empty cell, the "push" method is used to add step to the Stack, which reflects the player's most recent move. The player can undo an unlimited number of movements for any sort of move, including clicking on marked cells, empty cells, and neighbor cells. Especially, the player can even loss games. As the game is coded with python, list offers similar functions to a stack which is used in the game. To find the code, find undo function in cell.py.
