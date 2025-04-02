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

def get_pos_id(px: int, py: int):
		if x < px < x+size:
			if y < py < y+size:
				return id
		return None