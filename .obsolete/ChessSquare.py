import pygame as p

class ChessSquare():
	def __init__(self, color, x, y, size, id):
		self.color = color
		self.x = x
		self.y = y
		self.size = size
		self.id = id

	def draw(self, window):
		p.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))

	def get_pos_name(self, px: int, py: int):
		if self.x < px < self.x+self.size:
			if self.y < py < self.y+self.size:
				return self.id
		return None