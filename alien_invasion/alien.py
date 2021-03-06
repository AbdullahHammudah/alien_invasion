import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """creating an alien and controling it"""
    def __init__(self,screen,ai_settings):
        """defining the alien's attriutes and loading it's image"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #loading the alien image and get its rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        #start each new alitn near the left top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #store the alien's exact position
        self.x = float(self.rect.x)
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def check_edges(self):
        """check if the alien reaches the screen edges"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """move the aliens right"""
        self.x += (self.ai_settings.alien_speed_factor *
            self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
