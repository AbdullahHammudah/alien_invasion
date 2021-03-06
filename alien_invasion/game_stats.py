class GameStats():
    """Track statistics for Alien Invasion."""
    def __init__(self,ai_settings):
        """initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        #High score sohuld be never changed
        self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ships_limit
        self.score = 0
        self.level = 1
           
