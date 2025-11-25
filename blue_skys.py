import pygame
import sys, os
from kissyface import KissyFace
from heart import HeartBullet

class screen_color:
    """"Creates a full screen window with a specified background color."""
    def __init__(self):
        """initialize the screens size and color class"""
        pygame.init()
        #set the screen size
        self.screen = pygame.display.set_mode((1200, 800))
        #set the background color   
        self.bg_color = (135, 206, 235)  # RGB for sky blue

        pygame.display.set_caption("Blue Skys")        
        self.clock = pygame.time.Clock()

        self.kissyface = KissyFace(self)
        self.bullets = []  # List to store active heart bullets
        self.scale = 1
        self.growing = True

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.kissyface.update()
            # bullets is a list of HeartBullet instances; update handled elsewhere if needed
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        """Respond to keypresses."""                
        if event.key == pygame.K_RIGHT:
            self.kissyface.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.kissyface.moving_left = True
        elif event.key == pygame.K_UP:            
            self.kissyface.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.kissyface.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.kissyface.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.kissyface.moving_left = False
        if event.key == pygame.K_UP:
            self.kissyface.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.kissyface.moving_down = False

    def _fire_bullet(self):
        """Create a new heart bullet and add it to the bullets list."""        
        if len(self.bullets) < 100:  # Limit bullets on screen
            mx, my = self.kissyface.rect.midleft
            heart = HeartBullet(self.screen, (mx - 10, my), 0, 0.5, (255, 0, 0))
            self.bullets.append(heart)
    
    def _update_bullets(self):
        """Update and remove old heart bullets."""
        # Update bullets and remove those that have gone off the top of the screen
        alive = []
        for bullet in self.bullets:
            # move the bullet
            if hasattr(bullet, 'update'):
                bullet.update()
            # estimate the top of the heart shape (approx max y extent ~21 units scaled)
            top = bullet.y - 21 * getattr(bullet, 'scale', 1)
            if top > 0:
                alive.append(bullet)
        self.bullets = alive

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.bg_color)
        # Draw all heart bullets
        for heart in self.bullets:
            heart.draw()
        self.kissyface.blitme()

        pygame.display.flip()
        
if __name__ == '__main__':
    os.chdir('G:\\Python\\invasion_ex')
    bs = screen_color()
    bs.run_game()

    