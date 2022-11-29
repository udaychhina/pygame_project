import pygame

class Barrel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        barrel = pygame.image.load('graphics/obstacles/barrel.png').convert_alpha()
        barrel = pygame.transform.scale(barrel, (barrel.get_width()*2, barrel.get_height()*2))
        self.image = barrel
        self.rect = self.image.get_rect(midbottom=(200, 648))
