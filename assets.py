import pygame.font
from pygame import *
from pygame.sprite import *
from pygame.font import *

class Button(Sprite):
    def __init__(self, imagefile, pos, x_size, y_size, oversize_x, oversize_y):
        Sprite.__init__(self)
        self.position = pos
        self.normalsize_x,self.normalsize_y = [x_size,y_size]
        self.oversize_x,self.oversize_y = [oversize_x,oversize_y]
        self.image = image.load(imagefile)
        self.image = transform.scale(self.image,(self.normalsize_x,self.normalsize_y))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def mouseover(self):
        self.image = transform.scale(self.image,(self.oversize_x,self.oversize_y))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def mouseout(self):
        self.image = transform.scale(self.image,(self.normalsize_x,self.normalsize_y))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def draw(self,screen):
        screen.blit(self.image,self.rect)

class Board(Sprite):
    def __init__(self, screen):
        Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('images/congklakboard.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Seed(Sprite):
    def __init__(self, imagefile, position):
        Sprite.__init__(self)
        self.image = image.load(imagefile)
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.center = self.position
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class SeedScore(Sprite):
    def __init__(self, position, score):
        Sprite.__init__(self)
        self.position = position
        self.font = SysFont(None,30)
        self.score = score
        self.image = self.font.render("Seed: %s" % self.score,True,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = position
    
    def plus(self):
        self.score += 1
        self.image = self.font.render("Seed: %s" % self.score,True,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.position
    
    def minus(self):
        self.score -= 1
        self.image = self.font.render("Seed: %s" % self.score,True,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.position
    
    def reset(self):
        self.score = 0
        self.image = self.font.render("Seed: %s" % self.score,True,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

class Player(Sprite):
    def __init__(self, position, player):
        Sprite.__init__(self)
        self.position = position
        self.font = SysFont(None,30)
        self.player = player
        self.image = self.font.render("Player: %s" % self.player,True,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)
