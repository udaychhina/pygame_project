import random
import pygame
from .base_screen import BaseScreen

from components.player import Player
from components.barrel import Barrel
from components.flag import Flag
from components.text_box import TextBox

from components.util import obstacle_timer

from components.util import SCREEN_SIZE


class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Player sprite
        self.player = Player()
        self.character = pygame.sprite.GroupSingle()
        self.character.add(self.player)

        # Objects sprite group
        self.objects = pygame.sprite.Group()

        self.start_time = pygame.time.get_ticks()

        self.score = 0

    def draw(self):
        # Draw background
        self.sky = pygame.image.load("graphics/sky/sky.png").convert_alpha()
        self.sky = pygame.transform.scale(
            self.sky, (1152, self.sky.get_height()*2))
        self.ground = pygame.image.load(
            "graphics/ground/ground.jpg").convert_alpha()
        self.ground = pygame.transform.scale(
            self.ground, (self.window.get_width(), self.ground.get_height()))
        self.window.blit(self.sky, (0, 0))
        self.window.blit(self.ground, (0, self.sky.get_height()))

        # Draw controls text and the score. 
        self.font = pygame.font.Font("graphics/font/LLPIXEL3.ttf", 30)

        self.controls = self.font.render(
            "w: jump over barrel, d: dash through flag", True, (255, 255, 255))
        self.controls.get_rect(center=(SCREEN_SIZE[0]/2, 50))
        
        self.score_text = self.font.render(
            f"SCORE: {self.score}", True, (255, 255, 255))
        self.score_text.get_rect(center=(self.window.get_width() / 2, 200))
        
        self.window.blit(self.controls, (SCREEN_SIZE[0]/2 - self.controls.get_width()/2, 50))
        self.window.blit(
            self.score_text, (SCREEN_SIZE[0]/2 - self.score_text.get_width() / 2, 200))

        self.character.draw(self.window)
        self.objects.draw(self.window)

    def update(self):
        self.character.update()
        self.objects.update()

        self.score += 1

        if pygame.sprite.spritecollide(self.character.sprite, self.objects, False):
            if self.character.sprite.dash_state == True and self.objects.sprites()[0].__class__.__name__ == "Flag":
                destroy = self.objects.sprites()
                destroy[0].kill()
                print(destroy[0].__class__.__name__)
            elif self.character.sprite.dash_state == True and self.objects.sprites()[0].__class__.__name__ == "Barrel":
                self.character.sprite.kill()
                self.running = False
                self.next_screen = "game_over"
            else:
                self.character.sprite.kill()
                self.running = False
                self.next_screen = "game_over"

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.character.update()

        if event.type == obstacle_timer:
            self.objects.add(random.choice(
                [Barrel(), Barrel(), Barrel(), Flag()]))
