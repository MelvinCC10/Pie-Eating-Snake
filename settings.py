class Settings():
    """ a class to store all settings for Py eating snake."""

    def __init__(self):
        """Initialize the game's settings. """
        # Screen Settings
        self.screen_width =1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Snake settings
        self.snake_width = 10
        self.snake_height = 10
        self.snake_color = 60, 60, 60
        self.snake_speed_factor = 1.5
