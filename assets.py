# This File contains the classes for the snake and food objects.

import sys
import random

import pygame as pg
from pygame.sprite import Sprite

import dataStructures

class SnakeNode(Sprite):
    """ Using linked list data structure to model a snake, each portion of the
        snake will be consider a node"""

    def __init__ (self, screen, settings, location = [0,0]):
        """ create square at the center of the screen if this is the head or
            create a square at the end of the last location of the last node
            in the linked list """
        super(SnakeNode, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.inital_location = location

        # create a snake rect at inital_location and then set correct position
        self.rect = pg.Rect(self.inital_location[0], self.inital_location[1], self.settings.snake_width, self.settings.snake_height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Store the snakes position as a decimal value
        self.centerVert = float(self.rect.centery)
        self.centerHort = float(self.rect.centerx)

        # setting intial previous location for tails to follow
        self.prevCenterx = self.rect.centerx
        self.prevCentery = (self.rect.centery) + self.settings.snake_height + self.settings.space_snake_members

        # Color of the snake head
        self.color = settings.snake_color
