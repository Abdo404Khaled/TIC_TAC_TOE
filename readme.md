# Tic-Tac-Toe Game

## Introduction
This Python implementation of the classic Tic-Tac-Toe game offers a variety of gameplay options, including Player vs Player and Player vs Computer modes. The computer player utilizes different search algorithms for an intelligent gaming experience.

## Features
- **Player vs Player mode:** Play against a friend locally.
- **Player vs Computer mode:** Challenge the computer with various search algorithms.
- **Search Algorithms for Computer Player:**
  - **Depth-First Search (DFS):** Explores as far as possible along each branch before backtracking.
  - **Breadth-First Search (BFS):** Explores all the neighbor nodes at the current depth prior to moving on to nodes at the next depth level.
  - **Iterative Deepening:** Repeatedly applies DFS with increasing depth limits until a solution is found.
  - **Uniform-Cost Search (UCS):** Chooses the path that has the lowest total cost.
  - **Greedy Best-First Search:** Selects the path that appears to be the best based on a heuristic (evaluative function).
  - **A* Search:** Combines the advantages of UCS and Greedy Best-First by considering both the cost to reach a node and the heuristic estimate.
  - **MiniMax (for Player vs Computer mode):** Minimax is a decision-making algorithm used in two-player games where the goal is to minimize the possible loss for a worst-case scenario.

## How to Play
1. **Clone the repository:** `git clone https://github.com/Abdo404Khaled/TIC_TAC_TOE.git`
2. **Run the game:** `python tic_tac_toe.py`
3. **Choose the game mode:** Follow the on-screen instructions to select Player vs Player or Player vs Computer.
4. **Select the search algorithm:** If playing against the computer, choose from the available search algorithms.
5. **Enjoy the game:** Have fun playing Tic-Tac-Toe with your chosen settings!

## Game Rules
- The game is played on a 3x3 grid.
- Players take turns placing their symbol ('X' or 'O') in an empty spot on the grid.
- The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins.
- If all spots on the grid are filled and no player has won, the game is a draw.

## Algorithms Details

### Depth-First Search (DFS)
DFS explores as far as possible along each branch before backtracking, making it suitable for exploring different move possibilities.

### Breadth-First Search (BFS)
BFS explores all the neighbor nodes at the current depth before moving on to nodes at the next depth level. It ensures the shortest path is found.

### Iterative Deepening
Iterative Deepening repeatedly applies DFS with increasing depth limits until a solution is found. It combines the benefits of DFS and BFS.

### Uniform-Cost Search (UCS)
UCS chooses the path that has the lowest total cost. In Tic-Tac-Toe, it aims to find the optimal move based on the cost of reaching each state.

### Greedy Best-First Search
Greedy Best-First Search selects the path that appears to be the best based on a heuristic function. It prioritizes moves that seem more likely to lead to a win.

### A* Search
A* Search combines the advantages of UCS and Greedy Best-First by considering both the cost to reach a node and the heuristic estimate. It aims to find the optimal path efficiently.

### MiniMax
MiniMax is a decision-making algorithm used in two-player games. It evaluates possible moves by minimizing the possible loss for a worst-case scenario.

## Contributors
- Abdelrahman Khaled

Feel free to contribute, report issues, or suggest improvements!
