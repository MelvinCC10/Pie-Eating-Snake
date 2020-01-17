import pygame as pg
from pygame.sprite import Sprite

class Snake(Sprite):
    """ A class to create the head of the snake """

    def __init__ (self,settings,screen):
        """ create a snake object at the center of the screen """
        super(Snake, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        # create a snake rect at (0,0) and then set correct position
        self.rect = pg.Rect(0, 0, self.settings.snake_width, self.settings.snake_height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # setting intial previous location for tails to follow
        self.prevCenterx = self.rect.centerx
        self.prevCentery = (self.rect.centery) + 1#(self.settings.snake_height)

        # Store the snakes position as a decimal value
        self.centerVert = float(self.rect.centery)
        self.centerHort = float(self.rect.centerx)

        # Color of the snake head
        self.color = settings.snake_color

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def previous_location(self):
        self.prevCenterx = self.rect.centerx
        self.prevCentery = self.rect.centery

    def update(self):
        """ Move the snakes location """
        #Update the decimal position of the snake.
        if self.moving_right and self.rect.right< self.screen_rect.right:
            self.previous_location()
            self.centerHort += self.settings.snake_speed_factor
            self.rect.centerx = self.centerHort
        if self.moving_left and self.rect.left > 0:
            self.previous_location()
            self.centerHort -= self.settings.snake_speed_factor
            self.rect.centerx = self.centerHort

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.previous_location()
            self.centerVert -= self.settings.snake_speed_factor
            self.rect.centery = self.centerVert
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.previous_location()
            self.centerVert += self.settings.snake_speed_factor
            self.rect.centery = self.centerVert

    def draw_snake(self):
        """ Draw the bullet to the screen """
        pg.draw.rect(self.screen,self.color,self.rect)


class Tail(Snake):

    def __init__(self,settings,screen,lead):
        super().__init__(settings, screen)

        self.lead = lead
        # Setting intial location for this portion of the tail
        self.rect.centerx = lead.prevCenterx
        self.rect.centery = lead.prevCentery + 1

        # Setting intial location for this portion of the tail previous location
        self.prevCenterx = self.rect.centerx
        self.prevCentery = (self.rect.centery) #+ (self.settings.snake_height)



    def update(self,lead):


        if (self.rect.centery != lead.prevCentery):
            self.previous_location()
            self.rect.centery = lead.prevCentery

        if (self.rect.centerx != lead.prevCenterx):
            self.previous_location()
            self.rect.centerx = lead.prevCenterx
