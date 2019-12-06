import pygame
from pygame.sprite import Sprite

class Board(Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images')

