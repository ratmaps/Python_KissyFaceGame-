import pygame
import math

class HeartBullet:
    """A class to manage heart bullet rendering."""
    
    def __init__(self, surface, position, angle, scale, color):
        """Initialize the heart bullet with display parameters."""
        self.surface = surface
        # store position as floats for smooth movement
        self.x, self.y = float(position[0]), float(position[1])
        self.position = (self.x, self.y)
        self.angle = angle
        self.scale = scale
        self.color = color
        # movement speed (pixels per frame) — scale it so larger hearts move slightly faster
        self.speed = 3 * self.scale
    
    def draw(self):
        """Draw the heart shape on the surface."""
        x, y = self.x, self.y
        points = []
        for t in range(0, 360):
            rad = math.radians(t)
            x_val = 16 * (math.sin(rad) ** 3)
            y_val = 13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad)
            points.append((x + x_val * self.scale, y - y_val * self.scale))
        pygame.draw.polygon(self.surface, self.color, points)

    def update(self):
        """Move the heart bullet upward by its speed."""
        self.y -= self.speed
        self.position = (self.x, self.y)

def draw_heart_bullet(surface, position, angle, scale, color):
    """Convenience function to draw a heart bullet (uses HeartBullet class)."""
    heart = HeartBullet(surface, position, angle, scale, color)
    heart.draw()
