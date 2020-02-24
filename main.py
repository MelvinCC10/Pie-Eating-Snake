
def run_game():

    #Initilize settings objects
    settings = Settings()

    #Initilize MVC objects
    models = Models(setting.get_models())
    view  = View(settings.get_view())
    controller = Controller(settings.get_controller())

    #Main Loop for game
    while True:
        models.update(controller.get_output())
        view.update(models.get_output())
        controller.update()

#Staring Game
run_game()
