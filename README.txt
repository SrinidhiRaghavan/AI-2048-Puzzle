COMS4701-ARTIFICIAL INTELLIGENCE
ASSIGNMENT-2: ADVERSARIAL SEARCH AND GAMES 
UNI: ss5145
NAME: SRINIDHI SRINIVASA RAGHAVAN 

I ran Minimax with pruning for 20 times, amongst which:
 - 11 observed a high-score of 2048 
 - 2 observed 4096
 - 7 observed 1024.
On the other hand, when executed the algorithm with Vanilla Minimax for 5 runs, the scores were just around 1024. 

I printed the maximum depth limit observed for both algorithms. 
Minimax with pruning goes up-to a depth of 5 whereas that with-out pruning observed a maximum limit of 3.
This may be because the number of nodes expanded by Minimax is huge. As a result, it fails to explore higher depth within the allowed time limit. 

It has to be noted that if there were no time and space constraints, the performance of vanilla minimax and that with pruning would have been same. 
However, real life applications enforce time constraints, hence, pruning is effective 
 