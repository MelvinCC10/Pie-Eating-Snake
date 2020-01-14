import sys

import pygame as pg

from settings import Settings
import game_functions as gf
from snake import Snake


def run_game():
    # Initialize game and create a screen object
    pg.init()
    settings = Settings()
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption("Py Eating Snake")

    # Make snake
    snake = Snake(settings,screen)

    # Start main loop of game.
    while True:

        # Watch for keyboard and mouse events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        gf.update_screen(settings, screen)
        snake.update()



run_game()