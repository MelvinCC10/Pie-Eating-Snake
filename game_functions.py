import sys

import pygame as pg
from snake import Snake
from snake import Tail

def check_keydown_events(event,settings,screen,snake):
    """ Respond to keypresses """
    if event.key == pg.K_d:
        snake.moving_right = True
    elif event.key == pg.K_a:
        snake.moving_left = True
    elif event.key == pg.K_w:
        snake.moving_up = True
    elif event.key == pg.K_s:
        snake.moving_down = True


def check_keyup_events(event,snake):
    """ Respond to keypresses """
    if event.key == pg.K_d:
        snake.moving_right = False
    elif event.key == pg.K_a:
        snake.moving_left = False
    elif event.key == pg.K_w:
        snake.moving_up = False
    elif event.key == pg.K_s:
        snake.moving_down = False


def check_event(settings, screen, snake):
    """Respond to keypresses and mouse events """
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event,settings, screen, snake)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, snake)


def update_screen(settings,screen, snake,tail):
    """ Update images on the screen and flip to the new screen """
    # Redraw the screen dring each pass through the loop
    screen.fill(settings.bg_color)

    #draw snake to screen
    snake.update()
    tail.update(snake)
    snake.draw_snake()
    tail.draw_snake()

    # Make the most recently drawn screen visible
    pg.display.flip()
