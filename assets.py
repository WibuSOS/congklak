import pygame.font
from pygame import *
from pygame.sprite import *

class Board(Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/congklakboard.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Background(Sprite):
    def __init__(self, screen, screen_height, screen_width):
        self.screen = screen
        self.image = pygame.image.load('images/batikbground.bmp')
        self.rect = self.image.get_rect()

class Congklak(Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/bijicongklak.png')
        




