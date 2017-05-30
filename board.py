

new_board = 'RNBQKBNR\nPPPPPPPP\n\n\n\n\npppppppp\nrnbqkbnr'

# Keeps track of piece positions and game state
class Game:
	def __init__(self):
		self.board = [list(line.ljust(8)) for line in new_board.split('\n')]
		self.en_passant = []
		self.castling = {
			'black': ('O-O', 'O-O-O'),
			'white': ('O-O', 'O-O-O')
		}
	