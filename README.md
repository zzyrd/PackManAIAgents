# PackManAIAgents
Implement 6 AI agents to playing packman.

## Method

### Breadth First Search
Search next best move by using BFS search algorithm based on current game state.
Since the game state is stochastic, there is no connection between frames. 
BFS searches all possible legal moves for each frame.
Implemented By using Queue

### Depth First Search
Search next best move by using DFS search algorithm based on current game state.
Since the game state is stochastic, there is no connection between frames. 
DFS searches all possible legal moves for each frame.
Implemented By using Stack

### A*  f(n) = g(n) + h(n):  f is total cost, g is depth, h is heuristic
Search game state based on heuristic value for each action, and made decision based on it.
use minheap to implement Priority Queue, sorted by cost, which is depth + heuristic()
keep track of (depth + heuristic(), state, action) in PQ
Implemented By using Priority Queue, (by minHeap)

### Hill Climber 
Reference:
(Updating)

### Genetic Algorithm
Reference:
(Updating)

### Monte Carlo Tree Search
Reference:
(Updating)
