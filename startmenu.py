import pygame 
from gamewindow import GameWindow
import sys

class Menu:
    def menu():
        # Initializing the constructor 
        pygame.init() 
        pygame.display.set_caption("Minesweeper")
        
        # Screen resolution 
        res = (1440,720) 
        
        # Opens up a window 
        screen = pygame.display.set_mode(res) 
        
        # White color 
        color = (255,255,255) 
        
        # Light shade of the button 
        color_light = (170,170,170) 
        
        # Dark shade of the button 
        color_dark = (100,100,100) 
        
        # Stores the width of the 
        # Screen into a variable 
        width = screen.get_width() 
        
        # Stores the height of the 
        # Screen into a variable 
        height = screen.get_height() 
        
        # Defining a font 
        smallfont = pygame.font.SysFont('Corbel',35) 
        
        # Divide height and with percentage for ease of usage
        def height_prct(percentage):
            return (height/100)*percentage

        def width_prct(percentage):
            return (width/100)*percentage
        # Rendering a text written in 
        # This font 
        quittext = smallfont.render('Quit' , True , color) 
        starttext = smallfont.render('Start' , True , color)
        creditstext = smallfont.render('A game project made by:', True, color)
        nametext = smallfont.render('Vũ Nhật Duy', True, color)
        # Image
        image = pygame.image.load(r'images\start2.png')
        image = pygame.transform.scale(image, (1440,500))
        while True: 
            
            for ev in pygame.event.get(): 
                
                if ev.type == pygame.QUIT: 
                    pygame.quit() 
                    sys.exit()
                # Checks if a mouse is clicked 
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    
                    # If the mouse is clicked on the 
                    # Button the game is terminated 
                    if width_prct(45) <= mouse[0] <= width_prct(45)+200 and height_prct(75) <= mouse[1] <= height_prct(75)+40:
                        pygame.quit()
                        GameWindow.main()
                        sys.exit()
                    if width_prct(45) <= mouse[0] <= width_prct(45)+200 and height_prct(85) <= mouse[1] <= height_prct(85)+40:
                        pygame.quit()
                        sys.exit()
            # Fills the screen with a color 
            screen.fill((0,160,0,255)) 
            
            # Stores the (x,y) coordinates into 
            # The variable as a tuple 
            mouse = pygame.mouse.get_pos() 
            
            # If mouse is hovered on a button it 
            # Changes to lighter shade 
            if width_prct(45) <= mouse[0] <= width_prct(45)+200 and height_prct(75) <= mouse[1] <= height_prct(75)+40: 
                pygame.draw.rect(screen,color_light,[width_prct(45),height_prct(75),200,40]) 
                
            else: 
                pygame.draw.rect(screen,color_dark,[width_prct(45),height_prct(75),200,40]) 
            
            if width_prct(45) <= mouse[0] <= width_prct(45)+200 and height_prct(85) <= mouse[1] <= height_prct(85)+40: 
                pygame.draw.rect(screen,color_light,[width_prct(45),height_prct(85),200,40]) 
                
            else: 
                pygame.draw.rect(screen,color_dark,[width_prct(45),height_prct(85),200,40]) 
                
            # Superimposing the text onto our button 
            screen.blit(starttext , (width_prct(45)+60,height_prct(75))) 
            screen.blit(quittext , (width_prct(45)+60,height_prct(85)))
            screen.blit(creditstext, (width_prct(0),height_prct(90)))
            screen.blit(nametext, (width_prct(0),height_prct(90)+35))
            screen.blit(image, (0,0)) 
            
            # Updates the frames of the game 
            pygame.display.update()
            
Menu.menu()