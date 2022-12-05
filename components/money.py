import pygame
from random import randint
from .util import GROUND, SCREEN_SIZE


class Money(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        money = pygame.image.load(
            'graphics/obstacles/money.png').convert_alpha()
        money = pygame.transform.scale(
            money, (money.get_width()*1.3, money.get_height()*1.6))
        self.image = money
        self.rect = self.image.get_rect(
            midbottom=(randint(SCREEN_SIZE[0]+100, SCREEN_SIZE[0] + 350), GROUND - 50))

    def update(self):
        self.rect.x -= 7
        if self.rect.right < 0:
            self.kill()