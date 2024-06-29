#@author Paul-Walcher
#29.6.2024
from __future__ import annotations
from typing import Any, Callable

import pygame

#class for rendering the stuff
class GraphicsEngine:

	def __init__(self, background_color: tuple[int, int, int]):

		#color for drawing the background
		self.background_color = background_color

	def draw(self, screen):

		screen.fill(self.background_color)

		pygame.display.flip()