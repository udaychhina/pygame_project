import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
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
        self.player_run = [player_run_1, player_run_2,
                            player_run_3, player_run_4, player_run_5, player_run_6]

        self.player_run = [pygame.transform.scale(player, (player
            .get_width()*2, player.get_height()*2)) for player in self.player_run]

        self.player_index = 0
        self.player_jump = pygame.image.load(
            'graphics/player/player_jump.png').convert_alpha()
        self.player_jump = pygame.transform.scale(self.player_jump, (
            self.player_jump.get_width()*2, self.player_jump.get_height()*2))

        self.image = self.player_run[self.player_index]
        self.rect = self.image.get_rect(midbottom=(100, 648))
        self.gravity = 0

        # self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        # self.jump_sound.set_volume(0.5)

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.bottom >= 648:
            self.gravity = -20

    def add_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 648:
            self.rect.bottom = 648

    def animation(self):
        if self.rect.bottom < 648:
            self.image = self.player_jump
        else:
            self.player_index += 0.15
            if self.player_index >= len(self.player_run):
                self.player_index = 0
            self.image = self.player_run[int(self.player_index)]

    def update(self):
        self.jump()
        self.add_gravity()
        self.animation()
