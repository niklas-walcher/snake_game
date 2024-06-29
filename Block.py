#@author: niklas-walcher 
#@date: 29-6-2024

"""
These are the blocks used in snake game.
"""

class Block:

	def __init__(self, x:int, y:int, color: tuple[int,int,int])

		self.x: int = x
		self.y: int = y
		self.color: tuple[int,int,int] = color

