import random
import pygame
from .base_screen import BaseScreen

from components.player import Player
from components.barrel import Barrel
from components.text_box import TextBox


class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create the paddle
        self.player = Player()
        self.barrel = Barrel()
        self.player.x = 100

        self.character = pygame.sprite.GroupSingle()
        self.character.add(self.player)

        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.barrel)
        # self.sprites.add(self.ball)

    def update(self):
        self.character.update()


    def draw(self):
        self.sky = pygame.image.load("graphics/sky/sky.png").convert_alpha()
        self.sky = pygame.transform.scale(self.sky, (1152, self.sky.get_height()*2))
        self.ground = pygame.image.load("graphics/ground/ground.jpg").convert_alpha()
        self.ground = pygame.transform.scale(self.ground, (self.window.get_width(), self.ground.get_height()))
        self.window.blit(self.sky, (0, 0))
        self.window.blit(self.ground, (0, self.sky.get_height()))

        self.character.draw(self.window)
        self.sprites.draw(self.window)

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
                self.running = False
                self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.character.update()
