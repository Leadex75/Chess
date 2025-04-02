import pygame as p
import pygame

class ChessPieces():
	def __init__(self, window, square_size):
		self.board = [
			["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
			["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
			["", "", "", "", "", "", "", ""],
			["", "", "", "", "", "", "", ""],
			["", "", "", "", "", "", "", ""],
			["", "", "", "", "", "", "", ""],
			["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
			["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
		]

		self.window = window
		self.square_size = square_size
		self.quality = "png"
		self.type = "alpha"# alpha, book, classic, club, modern, vintage
		self.images = self.load_pieces()

	def load_pieces(self):
		images = {}
		pieces = ["br", "bn", "bb", "bq", "bk", "bp", "wr", "wn", "wb", "wq", "wk", "wp"]
		for piece in pieces:
			images[piece] = p.image.load(f"Pieces/Pieces_{self.type}_{self.quality}/{piece}.{self.quality}").convert_alpha()
			images[piece] = p.transform.smoothscale(images[piece], (self.square_size, self.square_size))
		return images

	def draw_pieces(self, window, square_size):
		for row in range(len(self.board)):
			for col in range(len(self.board)):
				piece = self.board[row][col]
				if piece != "":
					x = col * square_size
					y = row * square_size
					window.blit(self.images[piece], (x, y))
		p.display.flip()