import pygame
from .base_screen import BaseScreen
from components.util import SCREEN_SIZE

pygame.font.init()


class GameOverScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.sky = pygame.image.load("graphics/sky/sky.png").convert_alpha()
        self.sky = pygame.transform.scale(self.sky, (1152, self.sky.get_height()*2))
        self.ground = pygame.image.load("graphics/ground/ground.jpg").convert_alpha()
        self.ground = pygame.transform.scale(self.ground, (self.window.get_width(), self.ground.get_height()))
        self.logo = pygame.image.load("graphics/logo.png").convert_alpha()
        self.game_over = pygame.image.load("graphics/gameover.png").convert_alpha()

        self.font = pygame.font.Font("graphics/font/LLPIXEL3.ttf", 30)
        self.score_text = self.font.render("SCORE: " + str(self.score), True, (255, 255, 255))
        self.score_text.get_rect(center=(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2 + 200))

    def draw(self):
        self.window.blit(self.sky, (0, 0))
        self.window.blit(self.logo, (SCREEN_SIZE[0]/2 - self.logo.get_width()/2, 100))
        self.window.blit(self.game_over, (SCREEN_SIZE[0]/2 - self.game_over.get_width()/2, 250))
        self.window.blit(self.score_text, (SCREEN_SIZE[0]/2 - self.score_text.get_width()/2, SCREEN_SIZE[1]/2 - self.score_text.get_height()/2))
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
