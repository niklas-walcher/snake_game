#@author: niklas-walcher, Paul-Walcher
#29.6.2024
from __future__ import annotations
from typing import Any, Callable

import pygame

from GraphicsEngine import GraphicsEngine

pygame.init()

WIDTH: int = 800
HEIGHT: int = 600
BLOCKSIZE: int = 20
FPS: int = 60
BACKGROUND_COLOR: tuple[int, int, int] = (0xFF, 0xFF, 0xFF)



if __name__ == "__main__":

	#fixing window sizes
	WIDTH -= (WIDTH % BLOCKSIZE)
	HEIGHT -= (HEIGHT % BLOCKSIZE)
	GRID_WIDTH = WIDTH / BLOCKSIZE
	GRID_HEIGHT = HEIGHT / BLOCKSIZE

	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Snake Game")

	quit: bool = False

	#constructing the graphics engine
	graphics_engine: GraphicsEngine = GraphicsEngine(BACKGROUND_COLOR)
	#gameloop
	while not quit:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				quit = True

		#updating the window with the redrawer class

		graphics_engine.draw(screen)


	pygame.quit()