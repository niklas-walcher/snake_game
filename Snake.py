#@author: niklas-walcher 
#@date: 29-6-2024

"""
These are the blocktypes used in snake game.
"""
from __future__ import annotations
from Block import Block

class Snake:

	def __init__(self, head:Block, body:Block, grid_width: int, grid_height: int, x:int, y:int, color: tuple[int,int,int]) 
		
		self.color: tuple[int,int,int] = color
		self.head: Block = 0
		self.body: Block = 0
		self.grid_width: int = 1
		self.grid_height: int = 1



	def grow():

		#This method spawns a block at the position of the last block in the list body, or the head if body is empty.

	def move():

		#1. receives direction
		#2. checks if movement is possible 
		#3. moves if possible

	def checkoverlap() -> bool:

		#checks if the snakes head overlaps with its body