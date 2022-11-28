import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_run_1 = pygame.image.load('graphics/player/player_run_1.png').convert_alpha()
		player_run_2 = pygame.image.load('graphics/player/player_run_2.png').convert_alpha()
		player_run_3 = pygame.image.load('graphics/player/player_run_3.png').convert_alpha()
		player_run_4 = pygame.image.load('graphics/player/player_run_4.png').convert_alpha()
		player_run_5 = pygame.image.load('graphics/player/player_run_5.png').convert_alpha()
		player_run_6 = pygame.image.load('graphics/player/player_run_6.png').convert_alpha()
		self.player_walk = [player_run_1, player_run_2, player_run_3, player_run_4, player_run_5, player_run_6]
		self.player_index = 0
		# self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom = (80,128))
		self.gravity = 0

		# self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
		# self.jump_sound.set_volume(0.5)

	# def player_input(self):
	# 	keys = pygame.key.get_pressed()
	# 	if (keys[pygame.K_SPACE] or keys[pygame.K_W]) and self.rect.bottom >= 128:
	# 		self.gravity = -20
	# 		# self.jump_sound.play()

	# def apply_gravity(self):
	# 	self.gravity += 1
	# 	self.rect.y += self.gravity
	# 	if self.rect.bottom >= 128:
	# 		self.rect.bottom = 128

	# def animation_state(self):
	# 	if self.rect.bottom < 128: 
	# 		self.image = self.player_jump
	# 	else:
	# 		self.player_index += 0.1
	# 		if self.player_index >= len(self.player_walk):self.player_index = 0
	# 		self.image = self.player_walk[int(self.player_index)]

	# def update(self):
	# 	self.player_input()
	# 	self.apply_gravity()
	# 	self.animation_state()