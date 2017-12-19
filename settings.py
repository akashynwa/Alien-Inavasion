class Settings():
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship speed settings
        self.ship_speed_factor = 10

        # bullet settings
        self.bullet_speed_factor = 100
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3