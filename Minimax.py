#AIM: IMPLEMENTS THE VANILLA MINIMAX ALGORITHM

from Helper import *
import numpy as np
import time 


#Returns the maximum value of the utility function
def Decision(grid, max=True):
	limit = 4
	start = time.clock()

	if max:
		return Maximize(grid=grid, depth=limit, start=start)
	else:
		return Minimize(grid=grid, depth=limit, start=start)
		

#Finds the largest utility for the Max Player(Computer playing the game)
def Maximize(grid, depth, start):
	if terminal(grid) or depth==0 or (time.clock()-start)>0.04:
		return Eval(grid)

	maxUtility =  -np.inf
	
	#The children for the Max player are the neighboring tiles 
	for child in children(grid):
		maxUtility = max(maxUtility, Minimize(grid=child, depth=depth-1, start=start))

	return maxUtility


#Finds the smallest utility for the Min Player(Computer placing the random tiles)
def Minimize(grid, depth, start):
	if terminal(grid)  or depth==0 or (time.clock()-start)>0.04:
		return Eval(grid)

	minUtility = np.inf 

	empty = grid.getAvailableCells();

	children = []

	for pos in empty:
		current_grid2 = grid.clone()
		current_grid4 = grid.clone()

		current_grid2.insertTile(pos, 2)
		current_grid4.insertTile(pos, 4)

		children.append(current_grid2)
		children.append(current_grid4)

	#The children for the Min player include all random tile possibilities for the current state 
	for child in children:
		minUtility = min(minUtility, Maximize(grid=child, depth=depth-1, start= start))

	return minUtility
