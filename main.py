import pygame as pg

from controller import Controller
from settings import Settings

def run_game():

    #Initilize settings objects
    settings = Settings()

    #Initilize MVC objects
    #models = Models(setting.get_models())
    #view  = View(settings.get_view())
    controller = Controller(settings)

    #Main Loop for game
    while True:
        #models.update(controller.get_output())
        #view.update(models.get_output())
        controller.update()

#Staring Game

# Initialize game and create a screen object
pg.init()
screen = pg.display.set_mode((800, 800))
pg.display.set_caption("Py Eating Snake")

run_game()
