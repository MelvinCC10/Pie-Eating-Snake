import sys

import pygame as pg
from snake import Snake

def update_screen(settings,screen, snake):
    """ Update images on the screen and flip to the new screen """
    # Redraw the screen dring each pass through the loop
    screen.fill(settings.bg_color)

    snake.draw_snake()

    # Make the most recently drawn screen visible
    pg.display.flip()
