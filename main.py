import sys

import pygame as pg
from pygame.sprite import Group

from settings import Settings
import game_functions as gf
from snake import Snake
from snake import Tail
from snake import Food




def run_game():

    # Initialize game and create a screen object
    pg.init()
    settings = Settings()
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption("Py Eating Snake")

    # Creating the snake head, tail, and food objects
    snake = Snake(settings,screen)
    food = Food(settings, screen)
    food.setPos()
    tail = []

    """ prototype code for creating memberers of the tail and storing them in alist """
    tail.append(Tail(settings,screen,snake))

    # Start main loop of game.



    while True:

        # setting frame rate
        clock = pg.time.Clock()
        clock.tick_busy_loop(30)


        # Watch for keyboard and mouse events.
        gf.check_event(settings, screen, snake)
        gf.update_screen(settings, screen, snake, tail, food)

#Staring Game
run_game()
