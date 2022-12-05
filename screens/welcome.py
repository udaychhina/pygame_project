import pygame
from .base_screen import BaseScreen
from components.util import SCREEN_SIZE

pygame.font.init()

class WelcomeScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Text
        self.font = pygame.font.Font("graphics/font/LLPIXEL3.ttf", 30)
        self.start_info = self.font.render("PRESS SPACE TO START", True, (255, 255, 255))
        self.credit_info = self.font.render("by UDAY CHHINA", True, (255, 255, 255))
        self.high_score = self.font.render("HIGH SCORE: " + str(self.score.scores["highest"]), True, (255, 255, 255))
        self.start_info.get_rect(center=(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2 + 200))
        self.credit_info.get_rect(center=(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2 + 250))
        self.high_score.get_rect(center=(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2 + 150))

        # Images
        self.sky = pygame.image.load("graphics/sky/sky.png").convert_alpha()
        self.sky = pygame.transform.scale(self.sky, (1152, self.sky.get_height()*2))
        self.ground = pygame.image.load("graphics/ground/ground.jpg").convert_alpha()
        self.ground = pygame.transform.scale(self.ground, (self.window.get_width(), self.ground.get_height()))
        self.logo = pygame.image.load("graphics/logo.png").convert_alpha()
        # self.sprites.add(self.button)


    def draw(self):
        self.window.blit(self.sky, (0, 0))
        self.window.blit(self.logo, (SCREEN_SIZE[0]/2 - self.logo.get_width()/2, 100))
        self.window.blit(self.ground, (0, self.sky.get_height()))
        self.window.blit(self.high_score, (SCREEN_SIZE[0]/2 - self.high_score.get_width()/2, SCREEN_SIZE[1]/2 - self.high_score.get_height()/2 - 50))
        self.window.blit(self.start_info, (SCREEN_SIZE[0]/2 - self.start_info.get_width()/2, SCREEN_SIZE[1]/2 - self.start_info.get_height()/2))
        self.window.blit(self.credit_info, (SCREEN_SIZE[0]/2 - self.credit_info.get_width()/2, SCREEN_SIZE[1]/2 - self.credit_info.get_height()/2+ 50) )

    def update(self):
        pass

    def manage_event(self, event):
        print(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "game"
            self.running = False
