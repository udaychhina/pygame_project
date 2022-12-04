import pygame
from random import randint
from .util import GROUND, SCREEN_SIZE


class Barrel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        barrel = pygame.image.load(
            'graphics/obstacles/barrel.png').convert_alpha()
        barrel = pygame.transform.scale(
            barrel, (barrel.get_width()*2, barrel.get_height()*2))
        self.image = barrel
        self.rect = self.image.get_rect(midbottom=(
            randint(SCREEN_SIZE[0]+100, SCREEN_SIZE[0] + 350), GROUND))

    def update(self):
        self.rect.x -= 8
        if self.rect.right < 0:
            self.kill()
