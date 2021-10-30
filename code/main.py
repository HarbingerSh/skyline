import pygame, sys
from settings import *
from level import Level
from game_data import island

pygame.init()
screen = pygame.display.set_mode((screenWidth,screenHeight))
clock = pygame.time.Clock()
level = Level(island,screen)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill((135,206,250))
	level.run()

	pygame.display.update()
	clock.tick(fps)