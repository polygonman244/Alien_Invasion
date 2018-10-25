import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # Initialize game and make a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(screen)

    # Make main loop for game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make most recently drawn screen visible
        pygame.display.flip()


run_game()


