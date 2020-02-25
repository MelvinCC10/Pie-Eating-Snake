import sys

import pygame as pg

class Controller():
    """ Controller Class """

    def __init__(self, settings):
        self.settings = settings


    def check_keydown_events(self,event):
        """ Respond to keypresses """
        if event.key == pg.K_d:
            self.settings.moving_right = True
            self.settings.moving_left = False
            self.settings.moving_up = False
            self.settings.moving_down = False
        elif event.key == pg.K_a:
            self.settings.moving_left = True
            self.settings.moving_up = False
            self.settings.moving_down = False
            self.settings.moving_right = False
        elif event.key == pg.K_w:
            self.settings.moving_up = True
            self.settings.moving_down = False
            self.settings.moving_right = False
            self.settings.moving_left = False
        elif event.key == pg.K_s:
            self.settings.moving_down = True
            self.settings.moving_right = False
            self.settings.moving_left = False
            self.settings.moving_up = False



    def check_keyup_events(self,event):
        """ Respond to keypresses """
        """if event.key == pg.K_d:
            snake.moving_right = False
        elif event.key == pg.K_a:
            snake.moving_left = False
        elif event.key == pg.K_w:
            snake.moving_up = False
        elif event.key == pg.K_s:
            snake.moving_down = False"""


    def update(self):
        """Respond to keypresses and mouse events """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self.check_keyup_events(event)
