import pygame
import sys
from heart import draw_heart_bullet

pygame.init()
WIDTH, HEIGHT = 80, 80
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart Bullets")  

BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()

scale = 1
growing = True
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if growing:
        scale += 0.02
        if scale >= 1.3:
            growing = False
    else:
        scale -= 0.02
        if scale <= 1.0:
            growing = True
    draw_heart_bullet(screen, (WIDTH // 2, HEIGHT // 2), 0, scale, RED)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()