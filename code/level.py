import pygame, random
from support import importLayout, importGraphics
from settings import tilesSize
from tiles import Tile, StaticTile, Create, AnimatedTile


class Level:
	def __init__(self,levelData,surface):
		self.displaySurface = surface

		terrainLayout = importLayout(levelData['terrain'])
		self.terrainSprites = self.createTileGroup(terrainLayout, 'terrain')

		treesLayout = importLayout(levelData['trees'])
		self.treesSprites = self.createTileGroup(treesLayout, 'trees')

		stoneLayout = importLayout(levelData['stone'])
		self.stoneSprites = self.createTileGroup(stoneLayout, 'stone')

	def createTileGroup(self,layout,type):
		spriteGroup = pygame.sprite.Group()

		for rowIndex, row in enumerate(layout):
			for colIndex, cell in enumerate(row):
				if cell != '-1':
					x = colIndex * tilesSize
					y = rowIndex * tilesSize

					if type == 'terrain':
						terrainTileList = importGraphics('../assets/terrain/tileset/tileset.png')
						tileSurface = terrainTileList[int(cell)]
						sprite = StaticTile(tilesSize, x, y, tileSurface)
						spriteGroup.add(sprite)
						
					if type == 'trees':
						if cell == '0':
							tileSurface = pygame.image.load('../assets/terrain/trees/tree.png').convert_alpha()
						if cell == '1':
							tileSurface = pygame.image.load('../assets/terrain/trees/tree1.png').convert_alpha()
						sprite = Create(tilesSize, x, y, tileSurface)
						spriteGroup.add(sprite)

					if type == 'stone':
						if cell == '0':
							tileSurface = pygame.image.load('../assets/terrain/stone/stone.png').convert_alpha()
						if cell == '1':
							tileSurface = pygame.image.load('../assets/terrain/stone/stone1.png').convert_alpha()
						sprite = Create(tilesSize, x, y, tileSurface)
						spriteGroup.add(sprite)

		return spriteGroup


	def run(self):
		self.terrainSprites.draw(self.displaySurface)
		self.treesSprites.draw(self.displaySurface)
		self.stoneSprites.draw(self.displaySurface)