import pygame as p #importation de la bibliotheque pygame
from ChessBoard import ChessBoard #importation de la classe ChessBoard
from ChessSquare import ChessSquare #importation de la classe ChessSquare

class main():
	def __init__(self):

		"""Définition des variables"""

		p.init() #initialisation de pygame
		self.running = True #variable pour la boucle principale
		self.font = p.font.Font(None, 32)# police d'écriture
		self.tooltip_color = "black"# couleur du texte
		self.tooltip_background_color = "white" #couleur de fond
		self.window_width = self.window_height = 800 #largeur de la fenetre et hauteur de la fenetre
		self.square_size = self.window_height//8 #taille d'une case
		self.window = p.display.set_mode((self.window_width, self.window_height), p.SRCALPHA) #creation de la fenetre
		p.display.set_caption("Chess Game") #titre de la fenetre
		self.couleur_1 = (46, 52, 63) #couleur 1
		self.couleur_2 = (103, 113, 129) #couleur 2
		self.board = ChessBoard()# instance de la classe ChessBoard
		self.run()# lancement de la boucle principale

	def run(self):

		"""Function qui lance toute les autres et affiche le plateau"""

		liste_square = self.board.draw_board(self.couleur_1, self.couleur_2, self.square_size, self.window)[0]# dessin du plateau et met toutes les cases dans une liste

		"""boucle principale qui récupère les évenements"""

		while self.running:
			for event in p.event.get():
				if event.type == p.QUIT:# si le joueur ferme la fenetre, arrête la boucle donc le programme.
					self.running = False

				elif event.type == p.MOUSEBUTTONDOWN:
					mouse = p.mouse.get_pos()# récupère la position de la souris
					pos_id = ChessSquare.get_pos_id(mouse[0], mouse[1])# récupère l'id de la case sur laquelle la souris est
					print(pos_id)# affiche l'id de la case sur laquelle la souris est
				
			p.display.flip()
		p.quit()
if __name__ == "__main__":
	main()