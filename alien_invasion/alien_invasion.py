import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from background_image import BackgroundImage
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #initialize pygame,settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(ai_settings)
    sb = Scoreboard(screen,ai_settings,stats)
    #make a ship, a group to store bullets and a group for aliens
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    # Make the Play button.
    play_button = Button(ai_settings,screen,"Play")
    #creat a fleet of aliens
    gf.creat_fleet(ai_settings,screen,aliens,ship)
    #start the main loop in the game
    
    while True:
        
        #watch for the keyboard and mouse events.
        gf.check_events(ai_settings,screen,ship,bullets,stats,play_button,
                        aliens,sb)
        
        if stats.game_active == True:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,bullets,aliens,stats,sb)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            
        gf.update_screen(ai_settings,screen,ship,bullets,
            aliens,stats,play_button,sb)
    
run_game()
    
