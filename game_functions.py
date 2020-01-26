import sys

import pygame as pg
from snake import Snake
from snake import Tail

def check_keydown_events(event,settings,screen,snake):
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


def check_keyup_events(event,snake):
    """ Respond to keypresses """
    """if event.key == pg.K_d:
        snake.moving_right = False
    elif event.key == pg.K_a:
        snake.moving_left = False
    elif event.key == pg.K_w:
        snake.moving_up = False
    elif event.key == pg.K_s:
        snake.moving_down = False"""


def check_event(settings, screen, snake):
    """Respond to keypresses and mouse events """
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event,settings, screen, snake)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, snake)


def update_screen(settings,screen,snake,tail,food):
    """ Update images on the screen and flip to the new screen """
    # Redraw the screen dring each pass through the loop
    screen.fill(settings.bg_color)

    #draw snake to screen
    snake.update(tail)
    snake.draw_snake()
    food.update(tail,settings,screen,snake)
    food.draw_food()

    tail[0].update(snake,snake)
    tail[0].draw_snake()
    for i in range(len(tail)-1):
        tail[i+1].update(tail[i],snake)
        tail[i+1].draw_snake()



    # Make the most recently drawn screen visible
    pg.display.flip()
