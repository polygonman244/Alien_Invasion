import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """Set starting position for ship."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get rectangular geometry on the ship.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ships center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement flag"""
        
        # Update the center value, not the rect
        # Also make it so the ship doesnt move past the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0
            self.center -= self.ai_settings.ship_speed_factor
        
        # Update rect object from self.center
        self.rect.centerx = self.center


    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)