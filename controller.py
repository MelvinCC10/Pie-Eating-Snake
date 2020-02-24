import sys

import pygame as pg
from snake import Snake
from snake import Tail

class controller():
    """docstring for ."""

    def __init__(self, settings):
        self.settings = settings

    def check_keydown_events(event):
        """ Respond to keypresses """
        if event.key == pg.K_d:
            snake.moving_right = True
            snake.moving_left = False
            snake.moving_up = False
            snake.moving_down = False
        elif event.key == pg.K_a:
            snake.moving_left = True
            snake.moving_up = False
            snake.moving_down = False
            snake.moving_right = False
        elif event.key == pg.K_w:
            snake.moving_up = True
            snake.moving_down = False
            snake.moving_right = False
            snake.moving_left = False
        elif event.key == pg.K_s:
            snake.moving_down = True
            snake.moving_right = False
            snake.moving_left = False
            snake.moving_up = False


    def check_keyup_events(event):
        """ Respond to keypresses """
        """if event.key == pg.K_d:
            snake.moving_right = False
        elif event.key == pg.K_a:
            snake.moving_left = False
        elif event.key == pg.K_w:
            snake.moving_up = False
        elif event.key == pg.K_s:
            snake.moving_down = False"""


    def check_event():
        """Respond to keypresses and mouse events """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                check_keydown_events(event)
            elif event.type == pg.KEYUP:
                check_keyup_events(event)
