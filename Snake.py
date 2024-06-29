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
		self.head: Block = Block(x, y, color)
		self.body: list[Block] = []
		self.grid_width: int = 1
		self.grid_height: int = 1



	def grow():

		#This method spawns a block at the position of the last block in the list body, or the head if body is empty.
		new_block: Block = None

		if len(body) == 0:

			new_block = Block(self.head.x, self.head.y, self.color)

		else:

			new_block = Block(self.body[-1].x, self.body[-1].y, self.color)

		self.body.append(new_block)

	def move():

		#1. receives direction
		#2. checks if movement is possible 
		#3. moves if possible

	def checkoverlap() -> bool:

		#checks if the snakes head overlaps with its body