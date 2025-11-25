import pygame

class KissyFace:
    """A class to manage the kissieFace screen."""

    def __init__(self, bs_game):
        """initialize the screens size and color class"""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/KissieFace.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Store decimal positions for smooth movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # Movement speed (pixels per frame)
        self.speed = 3

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update position based on movement flags and keep inside screen."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        # Update rect from float positions
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)