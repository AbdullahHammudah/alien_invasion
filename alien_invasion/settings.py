class Settings():
    """A class to store all the settings gor Alien Invasion"""
    def __init__(self):
        """initalize the game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230,230,230)
        #ship settings
        self.ships_limit = 3
        #bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 20
        #alien settings
        self.fleet_drop_speed = 10
        #How quickly the game speeds up
        self.speedup_scale = 1.1
        #How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """initialize settings that changes throughout the game"""
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 5
        self.alien_speed_factor = .7
        self.fleet_direction = 1
        
        #Scoring
        self.alien_points = 50
        
    def increase_speed(self):
        """increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        

