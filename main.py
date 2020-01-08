import pygame
import sys
import time
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
    single = Button("images/button_single.png",[100,300],*[93,46],*[100,56])
    multi = Button("images/button_multi.png",[100,400],*[93,46],*[100,56])
    AI = Button("images/button_ai.png",[100,500],*[93,46],*[100,56])
    terminate = Button("images/button_quit.png",[100,600],*[95,46],*[102,56])
    menu = Group(single,multi,AI,terminate)
    
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
                if single.rect.collidepoint(mouse.get_pos()):
                    try:
                        game(screen, game_settings.screen_width, game_settings.screen_height, mode="single") #execute game function
                    except (TypeError,AttributeError):
                        pass
                    # music.set_volume(0.2) #set bg music back to normal
                if multi.rect.collidepoint(mouse.get_pos()):
                    try:
                        game(screen, game_settings.screen_width, game_settings.screen_height, mode="multi") #execute game function
                    except (TypeError,AttributeError):
                        pass
                if AI.rect.collidepoint(mouse.get_pos()):
                    try:
                        game(screen, game_settings.screen_width, game_settings.screen_height, mode="AI") #execute game function
                    except (TypeError,AttributeError):
                        pass

                elif terminate.rect.collidepoint(mouse.get_pos()):
                    running = False
                    pygame.quit()

        if single.rect.collidepoint(mouse.get_pos()):
            single.mouseover()
        else:
            single.mouseout()
        if multi.rect.collidepoint(mouse.get_pos()):
            multi.mouseover()
        else:
            multi.mouseout()
        if AI.rect.collidepoint(mouse.get_pos()):
            AI.mouseover()
        else:
            AI.mouseout()
        if terminate.rect.collidepoint(mouse.get_pos()):
            terminate.mouseover()
        else:
            terminate.mouseout()

        display.update()

if __name__ == "__main__":
    main()
