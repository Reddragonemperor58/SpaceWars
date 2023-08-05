import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Space_ship
import game_functions as gf

def run_game():
    #Initializengame and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigth))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    Play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard."""
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a  Space_ship, a group of bullets, and a group of aliens.
    ship =Space_ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)


    #start main loop
    while True:
        #loop to check the keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, Play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)


        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, Play_button)








run_game( )
