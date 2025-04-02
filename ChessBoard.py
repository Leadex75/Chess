import pygame as p
from ChessSquare import ChessSquare
from ChessPieces import ChessPieces

class ChessBoard():
	def __init__(self):
		pass
	
	def draw_board(self, couleur_1, couleur_2, square_size, window):
		list_square = []
		self.pieces = ChessPieces(window, square_size) #instancie les pieces
		lettres = "ABCDEFGH" #lettres pour les colonnes
		number = "87654321" #chiffres pour les lignes
		counter = 0
		for row in range(len(lettres)):
			for col in range(len(lettres)):
				color = couleur_1 if (row + col) % 2 == 0 else couleur_2 #alternance des couleurs
				id = f"{lettres[col ]}{number[row]}" #id de la case
				x = col * square_size #position x de la case
				y = row * square_size #position y de la case
				square = ChessSquare(color, x, y, square_size, id)# instancie la case
				square.draw(window)
				list_square.append(square) #ajout de la case dans la liste
				counter += 1
				self.pieces.draw_pieces(window, square_size) #creation des pieces
				name_piece = self.pieces.draw_pieces(window, square_size)
		p.display.flip() #rafraichissement de l'ecran
		return list_square, name_piece #retourne la liste des cases et le nom de la piece