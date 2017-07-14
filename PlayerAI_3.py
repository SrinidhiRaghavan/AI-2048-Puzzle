#AIM: PLAYER_AI GETS THE NEXT MOVE FOR THE PLAYER 


from BaseAI_3 import BaseAI
from Helper import *
from Minimaxab import *
from Grid_3 import *
import numpy as np

class PlayerAI(BaseAI):
	def getMove(self, grid):
		moves = grid.getAvailableMoves()
		maxUtility = -np.inf
		nextDir = -1

		for move in moves:
			child = getChild(grid, move)

			utility = Decision(grid=child, max=False) 

			if utility >= maxUtility:
				maxUtility = utility
				nextDir = move

		return nextDir


