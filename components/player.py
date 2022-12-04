import pygame
from .util import GROUND


class Player(pygame.sprite.Sprite):
    def __init__(self):
        """_summary_: constructor for player
        """
        super().__init__()
        # add run photos
        player_run_1 = pygame.image.load(
            'graphics/player/player_run_1.png').convert_alpha()
        player_run_2 = pygame.image.load(
            'graphics/player/player_run_2.png').convert_alpha()
        player_run_3 = pygame.image.load(
            'graphics/player/player_run_3.png').convert_alpha()
        player_run_4 = pygame.image.load(
            'graphics/player/player_run_4.png').convert_alpha()
        player_run_5 = pygame.image.load(
            'graphics/player/player_run_5.png').convert_alpha()
        player_run_6 = pygame.image.load(
            'graphics/player/player_run_6.png').convert_alpha()

        # list of run photos for animation
        self.player_index = 0

        self.player_run = [player_run_1, player_run_2,
                           player_run_3, player_run_4, player_run_5, player_run_6]
        self.player_run = [pygame.transform.scale(player, (player
                                                           .get_width()*2, player.get_height()*2)) for player in self.player_run]

        # add jump photo
        self.player_jump = pygame.image.load(
            'graphics/player/player_jump.png').convert_alpha()
        self.player_jump = pygame.transform.scale(self.player_jump, (
            self.player_jump.get_width()*2, self.player_jump.get_height()*2))

        # add dash photo
        self.player_dash = pygame.image.load(
            'graphics/player/player_dash.png').convert_alpha()
        self.player_dash = pygame.transform.scale(self.player_dash, (
            self.player_dash.get_width()*2, self.player_dash.get_height()*2))

        # player states
        self.gravity = 0
        self.speed = 0
        self.default_pos = (100, GROUND)
        self.dash_state = False
        self.jump_state = False

        # image and rect for sprite
        self.image = self.player_run[self.player_index]
        self.rect = self.image.get_rect(bottomleft=self.default_pos)

    def jump(self):
        """_summary_: jump function for player
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.bottom >= GROUND and self.dash_state == False:
            self.jump_state = True
            self.gravity = -16

    def dash(self):
        """_summary_: dash function for player
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.rect.left <= 100 and self.jump_state == False:
            self.dash_state = True
            self.image = self.player_dash
            self.speed = 20

    def add_speed(self):
        """_summary_: add speed to player to reduce the position of the player
        back to the default position
        """
        self.speed -= 1
        self.rect.left += self.speed
        if self.rect.left <= 100:
            self.rect.left = 100
            self.dash_state = False

    def add_gravity(self):
        """_summary_: add gravity to player
        """
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= GROUND:
            self.rect.bottom = GROUND
            self.jump_state = False

    def animation(self):
        """_summary_: animation for player
        """
        if self.dash_state:
            self.image = self.player_dash
        else:
            if self.rect.bottom < GROUND:
                self.image = self.player_jump
            else:
                self.player_index += 0.15
                if self.player_index >= len(self.player_run):
                    self.player_index = 0
                self.image = self.player_run[int(self.player_index)]

    def update(self):
        """_summary_: update function for player
        """
        self.jump()
        self.dash()
        self.add_speed()
        self.add_gravity()
        self.animation()
