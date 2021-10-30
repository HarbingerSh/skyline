import pygame
from support import importFolder

class Tile(pygame.sprite.Sprite):
	def __init__(self,size,x,y):
		super().__init__()
		self.image = pygame.Surface((size,size))
		self.rect = self.image.get_rect(topleft = (x,y))

	def update(self,shift):
		pass

class StaticTile(Tile):
	def __init__(self,size,x,y,surface):
		super().__init__(size,x,y)
		self.image = pygame.transform.scale2x(surface)

class Create(StaticTile):
	def __init__(self,size,x,y,surface):
		super().__init__(size,x,y,surface)
		offset = y + size
		self.rect = self.image.get_rect(bottomleft = (x,offset))

class AnimatedTile(Tile):
	def __init__(self,size,x,y,path):
		super().__init__(size,x,y)
		self.frames = importFolder(path)
		self.frameIndex = 0
		self.image = self.frames[self.frameIndex]

	def animate(self):
		self.frameIndex += 0.15
		if self.frameIndex >= len(self.frames):
			self.frameIndex = 0
		self.image = self.frames[int(self.frameIndex)]

	def update(self,shift):
		self.animate()