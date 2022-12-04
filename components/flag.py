import pygame
from random import randint
from .util import GROUND, SCREEN_SIZE


class Flag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        flag = pygame.image.load(
            'graphics/obstacles/flag.png').convert_alpha()
        flag = pygame.transform.scale(
            flag, (flag.get_width()*1.3, flag.get_height()*1.6))
        self.image = flag
        self.rect = self.image.get_rect(
            midbottom=(randint(SCREEN_SIZE[0]+100, SCREEN_SIZE[0] + 350), GROUND - 20))

    def update(self):
        self.rect.x -= 7
        if self.rect.right < 0:
            self.kill()