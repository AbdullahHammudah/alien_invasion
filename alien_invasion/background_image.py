import pygame

class BackgroundImage():
    """displaying an image as part of the background"""
    
    def __init__(self,screen):
        self.screen = screen
        #load the image and get its rect    
        self.image = pygame.image.load('images/back_image.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
    
        #postining the image
        self.rect.center = self.screen_rect.center
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    
