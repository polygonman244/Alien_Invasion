import pygame


class Ship:

    def __init__(self, screen):
        """Set starting position for ship."""
        self.screen = screen

        # Load the ship image and get rectangular geometry on the ship.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement flag"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)