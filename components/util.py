import pygame

pygame.init()

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1700)

SCREEN_SIZE = (1152, 776)
GROUND = 648