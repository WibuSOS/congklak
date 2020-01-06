import pygame
import sys
from pygame.mixer import *
from settings import Settings
from assets import *
from game import *

def main():
    pygame.init()
    game_settings = Settings()
    pygame.display.set_caption("Congklak")
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))

    #Music & sound effects
        #your codes here

    #Background
    background = pygame.image.load('images/menubag.png')

    #Buttons & signs
    start = Button("images/play.png",[100,500],*[93,46],*[100,56])
    terminate = Button("images/quit.png",[100,600],*[95,46],*[102,56])
    menu = Group(start,terminate)
    
    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        menu.draw(screen)
        for command in event.get():
            if command.type == QUIT:
                running = False
                pygame.quit()
            
            if command.type == MOUSEBUTTONDOWN and command.button == 1:
                if start.rect.collidepoint(mouse.get_pos()):
                    try:
                        game(screen, game_settings.screen_width, game_settings.screen_height) #execute game function
                    except (TypeError,AttributeError):
                        pass
                    # music.set_volume(0.2) #set bg music back to normal
                
                elif terminate.rect.collidepoint(mouse.get_pos()):
                    running = False
                    pygame.quit()
        
        if start.rect.collidepoint(mouse.get_pos()):
            start.mouseover()
        else:
            start.mouseout()
        if terminate.rect.collidepoint(mouse.get_pos()):
            terminate.mouseover()
        else:
            terminate.mouseout()
        
        display.update()

if __name__ == "__main__":
    main()