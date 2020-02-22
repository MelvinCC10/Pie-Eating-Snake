import sys

import pygame as pg
from pygame.sprite import Group

from settings import Settings
import game_functions as gf
from Classes import Snake




def update_screen(settings,screen,snake):
    """ Update images on the screen and flip to the new screen """
    # Redraw the screen dring each pass through the loop
    screen.fill(settings.bg_color)

    #draw snake to screen
    print('Hello')
    snake.draw()

    # Make the most recently drawn screen visible
    pg.display.flip()





def run_game():

    # Initialize game and create a screen object
    pg.init()
    settings = Settings()
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption("Py Eating Snake")

    # Creating the snake head, tail, and food objects
    snake = Snake(settings,screen)

    while True:

        # setting frame rate
        clock = pg.time.Clock()
        clock.tick_busy_loop(30)


        # Watch for keyboard and mouse events.
        update_screen(settings, screen, snake)

#Staring Game
run_game()
