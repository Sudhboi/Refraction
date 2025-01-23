import pygame
import numpy

pygame.init()

pygame.display.set_mode((500, 500))
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)


pygame.quit()