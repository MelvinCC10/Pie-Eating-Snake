import sys

import pygame as pg

def update_screen(settings,screen):
    """ Update images on the screen and flip to the new screen """
    # Redraw the screen dring each pass through the loop
    screen.fill(settings.bg_color)

    # Make the most recently drawn screen visible
    pg.display.flip()
