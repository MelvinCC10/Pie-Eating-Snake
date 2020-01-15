class Settings():
    """ a class to store all settings for Py eating snake."""

    def __init__(self):
        """Initialize the game's settings. """
        # Screen Settings
        self.screen_width =1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Snake settings
        self.snake_width = 5
        self.snake_height = 5
        self.snake_color = 60, 60, 60
