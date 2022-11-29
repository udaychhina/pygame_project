import pygame
from .base_screen import BaseScreen
from components.text_box import TextBox


class WelcomeScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.button = TextBox(
            (200, 100), "Press SPACE", color=(255, 255, 255), bgcolor=(0, 0, 0)
        )
        self.sprites.add(self.button)

    def draw(self):
        self.sky = pygame.image.load("graphics/sky/sky.png").convert_alpha()
        self.sky = pygame.transform.scale(self.sky, (1152, self.sky.get_height()*2))
        self.ground = pygame.image.load("graphics/ground/ground.jpg").convert_alpha()
        self.ground = pygame.transform.scale(self.ground, (self.window.get_width(), self.ground.get_height()))
        self.window.blit(self.sky, (0, 0))
        self.window.blit(self.ground, (0, self.sky.get_height()))
        self.button.rect.x = 200
        self.button.rect.y = 400
        self.sprites.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        print(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "game"
            self.running = False
