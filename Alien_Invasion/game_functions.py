import sys

import pygame


def check_events(ship):
    """Respond to key presses and mouse events """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move ship to the right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # Move ship to the left
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to new screen"""
    # Redraw the screen during each pass on the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make most recently drawn screen visible.
    pygame.display.flip()