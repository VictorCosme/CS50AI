> GOAL TEST: way to determine weather a given state is a goal state

> PATH COST: numerical cost associated with a given path

> SOLUTION: a sequence of states that leads from initial state to a goal state

> OPTIMAL SOLUTION: the solution with the lowest path cost

> UNINFORMED SEARCH: search strategy that uses no problem-specific knowledge

> INFORMED SEARCH: search strategy that uses problem-specific knowledge to find solutions more efficiently





## Data structure
 > NODE: 
	state
	parent: the previous node (allows to backtrack sequence of states)
	action: the action applied to parent
	path cost since initial state: 


## Algorithms
- Depth-first search: 
	- uses a stack as frontier; 
	- finds a solution, but not always the optimal one 

- Breadth-first search: 
	- like DFS but uses a queue as frontier; 
	- finds the optimal solution, but requires more resources

- Greedy best-first search:
	- expands the node that is closest to the goal as estimated by a heuristic function `h(n)`; 
	- finding a good heuristic gives an advantage but it's quite challenging
	- Sometimes finds non-optimal solutions

- A*: 
	- expands node with lowest value of `g(n) + h(n)`, where `g(n)` is the cost to reach node and `h(n)` is the estimated cost to goal
	- it's optimal if h(n) is admissible and consistent
	- has a tendency to use a lot of memory
## Adversarial search
- A agent trying to make intelligent decisions while another agent wants the former one to fail

### Minimax
- (...)