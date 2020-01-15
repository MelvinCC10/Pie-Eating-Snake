import pygame as pg
from pygame.sprite import Sprite

class Snake(Sprite):
    """ A class to create the head of the snake """

    def __init__ (self,settings,screen):
        """ create a bullet object at the ships current position """
        super(Snake, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        print('hello')

        # create a bullet rect at (0,0) and then set correct position
        self.rect = pg.Rect(0, 0, settings.snake_width, settings.snake_height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Store the bullets position as a decimal value
        self.y = float(self.rect.y)

        self.color = settings.snake_color

    def update(self):
        """ Move the bullet up the screen """
        #Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_snake(self):
        """ Draw the bullet to the screen """
        pg.draw.rect(self.screen,self.color,self.rect)
