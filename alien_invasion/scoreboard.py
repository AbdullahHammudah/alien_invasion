import pygame.font

class Scoreboard ():
    """A class to report scoring information"""
    
    def __init__(self,screen,ai_settings,stats):
        """Initializing scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        #Font settings for scoring information
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        
    def prep_score(self):
        """Converting the score to str and then image, to display 
        & position it on the screen(top-right)"""
        score_rounded = int(round(self.stats.score,-1))
        score_str = "Score: " + "{:,}".format(score_rounded)
        self.score_image = self.font.render(score_str,True,
            self.text_color,self.ai_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20
        
    def prep_high_score(self):
        """prepare the high score to be displayed in a neat way"""
        #get the high score rounded and format with ',' 
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "High Score: " + "{:,}".format(high_score)
        #render the high score(turn thr str into image)
        self.high_score_image = self.font.render(high_score_str,True,
            self.text_color,self.ai_settings.bg_color)
        
        #poistion the high score in the top center
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_image_rect.top
        
        
    def prep_level(self):
        """prepare the level num to be displayed"""
        self.level_image = self.font.render("L: " + str(self.stats.level),True,
            self.text_color,self.ai_settings.bg_color)
            
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_image_rect.right
        self.level_image_rect.top = self.score_image_rect.bottom + 10
        
    
    def show_score(self):
        """Draw the score to the screen"""
        self.screen.blit(self.score_image,self.score_image_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_image_rect)
