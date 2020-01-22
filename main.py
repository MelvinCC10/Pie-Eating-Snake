import sys

import pygame as pg
from pygame.sprite import Group

from settings import Settings
import game_functions as gf
from snake import Snake
from snake import Tail


def run_game():

    # Initialize game and create a screen object
    pg.init()
    settings = Settings()
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption("Py Eating Snake")

    # Creating the snake head and tail classes
    snake = Snake(settings,screen)
    tail = []
    """ prototype code for creating memberers of the tail and storing them in alist """
    tail.append(Tail(settings,screen,snake))
    for i in range(100):
        tail.append(Tail(settings,screen,tail[-1]))

    # Start main loop of game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_event(settings, screen, snake)
        gf.update_screen(settings, screen, snake, tail)

#Staring Game
run_game()
