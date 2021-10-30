import pygame
from settings import trueTilesSize
from csv import reader
from os import walk

def importFolder(path):
	surfList = []

	for _,__,imgFiles in walk(path):
		for image in imgFiles:
			fullPath = path + '/' + image
			imageSurf = pygame.image.load(fullPath).convert_alpha()
			surfList.append(imageSurf)

	return surfList

def importLayout(path):
	terrainMap = []
	with open(path) as map:
		level = reader(map, delimiter = ',')
		for row in level:
			terrainMap.append(list(row))
		return terrainMap

def importGraphics(path):
	surface = pygame.image.load(path).convert_alpha()
	tileNumX = int(surface.get_size()[0] / trueTilesSize)
	tileNumY = int(surface.get_size()[1] / trueTilesSize)

	cutTiles = []
	for row in range(tileNumY):
		for col in range(tileNumX):
			x = col * trueTilesSize
			y = row * trueTilesSize
			newSurf = pygame.Surface((trueTilesSize,trueTilesSize))
			newSurf.blit(surface,(0,0),pygame.Rect(x,y,trueTilesSize,trueTilesSize))
			cutTiles.append(newSurf)

	return cutTiles