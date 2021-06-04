import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens,sb):
    """Respond to keypresses and mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(play_button,mouse_x,mouse_y,stats,aliens,
                                bullets,ai_settings,screen,ship,sb)
                                
                                
            
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)
        
            
def check_keyup_events(event,ship):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
            
            
def check_play_button(play_button,mouse_x,mouse_y,stats,aliens,bullets,
                        ai_settings,screen,ship,sb):
    """respond to the mouse click on the play button"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        #Hide the mouse cursor when the game is active
        pygame.mouse.set_visible(False)
        #Reset the game statistics
        stats.reset_stats()
        stats.game_active = True
        
        # Rest the scoreborad images
        sb.prep_high_score()
        sb.prep_score()
        sb.prep_level()
        
        #Empty the aliens and bullets list
        aliens.empty()
        bullets.empty()
    
        #Creat a new fleet and center the ship
        creat_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()
 
    
def fire_bullets(ai_settings,screen,ship,bullets):
    """fire bullets by space bar if limit not reached yet"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
    
def update_bullets(ai_settings,screen,ship,bullets,aliens,stats,sb):
    """get rid of the bullets that have disappeard"""
    bullets.update()
    #git rid of the bullets that have dissapeard
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    check_bullet_alien_collisions(ai_settings,screen,ship,bullets,aliens,
        stats,sb)
            

def check_bullet_alien_collisions(ai_settings,screen,ship,bullets,aliens,
    stats,sb):
    """respond to alien-bullet collision"""
    #Remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
        check_high_score(stats,sb)
    
    #check if the fleet is shout down and creat a new one
    if len(aliens) == 0:
        # Destroy existing bullets, speed up game, and create new fleet.
        bullets.empty()
        ai_settings.increase_speed()
        creat_fleet(ai_settings,screen,aliens,ship)
        #increase level
        stats.level += 1
        sb.prep_level()
            
            
def update_screen(ai_settings,screen,ship,bullets,aliens,stats,play_button,sb):
    """Update the images on the screen and flip to the new screen"""
    #Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    sb.show_score()
    
    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_msg()
        
    #make the most recently drawn screen visible
    pygame.display.flip()
    
def get_number_alien_x (ai_settings,alien_width):
    """determine the number of aliens that fit in the row"""
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x /(2 * alien_width))
    return number_aliens_x
    
def get_number_rows (ai_settings,ship_height,alien_height):
    """determine the number of rows of aliens that fit on the screen"""
    available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
    number_rows = int(available_space_y /(2*alien_height))
    return number_rows
    
def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
    """creat an alien and place it in the row"""
    alien = Alien(screen,ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2* alien_width * alien_number
    alien.rect.y = alien_height + 2* alien_height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)

            
def creat_fleet(ai_settings,screen,aliens,ship):
    """creat a fleet of aliens"""
    #creat an alien and find the number of the aliens in the row
    alien = Alien(screen,ai_settings)
    number_aliens_x = get_number_alien_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #spacing between each alien is equal to the alien width
        
    #creat the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings,screen,aliens,alien_number,row_number)
            
def check_fleet_edges(ai_settings,aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
        
def change_fleet_direction(ai_settings,aliens):
    """"Drop the entire fleet and change the fleet direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        #Descrement ships_left
        stats.ships_left -= 1
    
        #Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
    
        #Creat a new fleet and center the ship
        creat_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()
    
        #Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    """check if an alien hit the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Treat this the same as the ship got hit
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break
            
def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    """Check if the fleet is at an edge,
    and then update the postions of all aliens in the fleet"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    
    #Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
    # Look for aliens hitting the bottom of the screen   
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)
    
def check_high_score(stats,sb):
    """check for high scores and call to display them"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
