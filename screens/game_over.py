import pygame
from .base_screen import BaseScreen
from components.text_box import TextBox
from components.util import SCREEN_SIZE


class GameOverScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.sky = pygame.image.load("graphics/sky/sky.png").convert_alpha()
        self.sky = pygame.transform.scale(self.sky, (1152, self.sky.get_height()*2))
        self.ground = pygame.image.load("graphics/ground/ground.jpg").convert_alpha()
        self.ground = pygame.transform.scale(self.ground, (self.window.get_width(), self.ground.get_height()))
        self.logo = pygame.image.load("graphics/logo.png").convert_alpha()
        self.game_over = pygame.image.load("graphics/gameover.png").convert_alpha()

    def draw(self):
        self.window.blit(self.sky, (0, 0))
        self.window.blit(self.logo, (SCREEN_SIZE[0]/2 - self.logo.get_width()/2, 100))
        self.window.blit(self.game_over, (SCREEN_SIZE[0]/2 - self.game_over.get_width()/2, 300))
        self.window.blit(self.ground, (0, self.sky.get_height()))

    def update(self):
        pass

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button1.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "welcome"
            elif self.button2.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = False
