# Solving 2048 intelligently using Minimax Algorithm #

## Introduction ##

Here, an instance of 2048 is played in a 4x4 grid, with numbered tiles that slide in all four directions. In every turn, a new tile will randomly appear in an empty slot on the board, with a value of either 2 or 4. The player can slide the tiles in all the four directions (Up, Down, Left and Right). As per the input direction given by the player, all tiles on the grid slide as far as possible in that direction, until (1) they either collide with another tile or (2) collide with the edge of the grid. If two tiles with the same number collide, then they merge into a single tile with value twice as that of the individual tiles. It has to be noted that the resulting tile will not collide with another tile in the same move. In this project, the game of 2048 is solved using the Minimax algorithm. Here, 2048 is treated as an adversarial game where the player is the computer which is attempting to maximize the value of the highest tile in the grid and the opponent is the computer which randomly places tiles in the grid to minimize the maximum score. Minimax algorithm would be suitable in this case as the game is played between opponents with a known motive of maximizing/minimizing a total score



## Minimimax Algorithm Overview ##

A strategy has to be employed in every game playing algorithm. With the minimax algorithm, the strategy assumes that the computer opponent is perfect in minimizing player's outcome. This is done irrespective of whether or not the opponent is perfect in doing so. 

This algorithm assumes that there are two players. One is named the Min and the other one is the Max. Both the players alternate in turms. The Max moves first. The aim of max is to maximize a heuristic score and that of min is to minimize the same. For every player, a minimax value is computed. This value is the best achievable payoff against his play. The move with the optimum minimax value is chosen by the player. 

Usually, the number of nodes to be explored by this algorithm is huge. In order to optimize it, pruning is used. 


Here, the 4x4 grid with a randomly placed 2/4 tile is the initial scenario. The computer player (MAX) makes the first move. This move is chosen by the minimax algorithm. After his play, the opponent randomly generates a 2/4 tile. The entire process continues until the game is over. 

While using the minimax algorithm, the MAX uses his move (UP, DOWN, RIGHT and LEFT) for finding the possible children nodes. Whereas the MIN will have the 2/4 tiles placed in all the empty cells for finding its children. Hence, for every max, there will be at most 4 children corresponding to each and every direction. And for MIN, the number of children will be 2*n where n is the number of empty cells in the grid. 


## Heuristic Function Used ##

Based on observations and expertise, it is concluded that the game is heading in the positive direction if the highest valued tile is in the corner and the other tiles are linearly decreases as it moves away from the highest tile. Thus, there are four different best possibilities : Maximum tile is at the (1)  Down -left (2) Top-left (3) Top-Right and (4) Down-Right corner. In order to compute the score, we can multiply the current configuration with a gradient matrix associated with each of the possible cases. The gradient matrix designed for this case is as given. 


 [
 		
				[[ 3,  2,  1,  0],[ 2,  1,  0, -1],[ 1,  0, -1, -2],[ 0, -1, -2, -3]], 
				
				[[ 0,  1,  2,  3],[-1,  0,  1,  2],[-2, -1,  0,  1],[-3, -2, -1, -0]],  
				
				[[ 0, -1, -2, -3],[ 1,  0, -1, -2],[ 2,  1,  0, -1],[ 3,  2,  1,  0]],  
				
				[[-3, -2, -1,  0],[-2, -1,  0,  1],[-1,  0,  1,  2],[ 0,  1,  2,  3]] 
				
]
 
The first element is when the highest score is at the top left, second is for top-right, then bottom-left and bottom-right. If you observe these matrices closely, you can see that the number corresponding to the highest tile is always the largest and others decrease linearly in a monotonic fashion. The sides diagonal to it is always awarded the least score. 

The final score of the configuration is the maximum of the four products (Gradient * Configuration )


## Code Organization ##

GameManager_3 :  Driver program that loads Computer AI and Player AI and begins the game where they compete with each other. Note that the time for making a move is kept as 2 seconds. 

Grid_3 : Defines the Grid object. Incorporates useful operations for the grid like move, getAvailableCells, insertTile and clone

BaseAI_3 : Base class for any AI component. All AI's inherit from this module and implement the getMove function which takes a Grid object as parameter and returns a move


ComputerAI_3 : This inherits from BaseAI. The getMove() function returns a computer action, i.e. a tuple (x, y) indicating the place you want to place a tile

PlayerAI_3 : Gets the next move for the player using Minimax Algorithm 

Minimax_3 : Implements the Minimax algorithm

Minimaxab_3 : Implements the Minimax algorithm with pruning (Depth limit is set as 4)

Helper_3 : All utility functions created for this game are written here. This includes the eval function which evaluates the heuristic score for a given configuration



## How to execute ##

Run python GameManager_3.py


## Environment ##

Python 3


## Results ##

![image](https://user-images.githubusercontent.com/21295042/28233936-9ee61280-68c8-11e7-8bb8-abb9c7980af5.png)


The algorithm with pruning was run 20 times. 
11 observed a score of 2048
2 observed 4096
7 observed 1024

When executed the algorithm with Vanilla Minimax (Minimax without pruning) for 5 runs, the scores were just around 1024. 

It has to be noted that if there were no time and space constraints, the performance of vanilla minimax and that with pruning would have been same. However, real life applications enforce time constraints, hence, pruning is effective 



