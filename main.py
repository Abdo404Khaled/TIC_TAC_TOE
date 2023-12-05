import os
import fontstyle
from collections import deque
import heapq

class tic_tac_toe(object):
    def __init__(self):
        self.__playing = True
        self.__complete = False
        self.__default_spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        self.__spots = self.__default_spots.copy()
        self.__turn = 0
        self.__prev_turn = -1
        self.__algo = -1
        self.__vs_computer = False
        self.winning_combinations = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),
            (1, 4, 7), (2, 5, 8), (3, 6, 9),
            (1, 5, 9), (3, 5, 7)
        ]
        self.__huPlayer = fontstyle.apply('X', 'red')
        self.__computer = fontstyle.apply('O', 'green')

    def play(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Welcome to Tic-Tac-Toe Game')
            try:
                choice = int(input('Choose 1 option:\n1- Player vs Player\n2- Player vs Computer\n'))
                if choice == 1:
                    self.__vs_computer = False
                elif choice == 2:
                    self.__vs_computer = True
                else:
                    raise ValueError()
                break
            except ValueError:
                pass

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Welcome to Tic-Tac-Toe Game')
            try:
                choice = int(input('Choose 1 option:\n1- vs DFS \n2- vs BFS\n3- vs Iterative Deepening\n4- vs UCS\n5- Greedy\n6- A*\n7- MiniMax\n'))
                if choice == 1:
                    self.__algo = 0
                elif choice == 2:
                    self.__algo = 1
                elif choice == 3:
                    self.__algo = 2
                elif choice == 4:
                    self.__algo = 3
                elif choice == 5:
                    self.__algo = 4
                elif choice == 6:
                    self.__algo = 5
                elif choice == 7:
                    self.__algo = 6
                else:
                    raise ValueError()
                break
            except ValueError:
                pass

        while self.__playing:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.__draw_board()
            if self.__prev_turn == self.__turn:
                print('Invalid spot selected, please pick another')
            self.__prev_turn = self.__turn
            if self.__check_current_turn() == 'O' and self.__vs_computer:
                if self.__algo == 0:
                    self.__switch(self.__DFS_computer_move(self.__spots.copy(), self.__computer))
                elif self.__algo == 1:
                    self.__switch(self.__BFS_computer_move(self.__spots.copy(), self.__computer))
                elif self.__algo == 2:
                    self.__switch(self.__DFS_limited_computer_move(self.__spots.copy(), self.__computer))
                elif self.__algo == 3:
                    self.__switch(self.__UCS_computer_move(self.__spots.copy(), self.__computer))
                elif self.__algo == 4:
                    self.__switch(self.__GREEDY_computer_move(self.__spots.copy(), self.__computer))
                elif self.__algo == 5:
                    self.__switch(self.__AStar_computer_move(self.__spots.copy(), self.__computer))
                elif self.__algo == 6:
                    self.__switch(self.__Minimax_computer_move(self.__spots.copy(), self.__computer)[1])
            else:
                choice = input(f'Player {self.__check_current_turn()} to play or press q to quit: ')
                self.__switch(choice)
            if self.__check_for_win():
                self.__playing, self.__complete = False, True
            if self.__turn > 8:
                self.__playing = False

        os.system('cls' if os.name == 'nt' else 'clear')
        self.__draw_board()

        if self.__complete:
            print(f'Player {self.__check_turn()} wins!!\n')
        else:
            print('No Winner!!')

        print('Thanks for Playing!')

        if str.lower(input('Press P to play again: ')) == 'p':
            self.__spots = self.__default_spots.copy()
            self.__playing, self.__complete = True, False
            self.__turn = 0
            self.__prev_turn = -1
            self.play()

    def __draw_board(self):
        print(
                f"+---+---+---+\n"
                f"| {self.__spots[1]} | {self.__spots[2]} | {self.__spots[3]} |\n"
                f"+---+---+---+\n"
                f"| {self.__spots[4]} | {self.__spots[5]} | {self.__spots[6]} |\n"
                f"+---+---+---+\n"
                f"| {self.__spots[7]} | {self.__spots[8]} | {self.__spots[9]} |\n"
                f"+---+---+---+"
            )

    def __check_turn(self):
        if self.__turn % 2 == 0:
            return 'O'
        else:
            return 'X'

    def __check_current_turn(self):
        if self.__turn % 2 == 0:
            return 'X'
        else:
            return 'O'

    def __switch(self, choice):
        if choice == 'q':
            self.__playing = False
            return
        elif str.isdigit(choice) and int(choice) in self.__spots:
            if not self.__spots[int(choice)] in [self.__huPlayer, self.__computer]:
                self.__turn += 1
                self.__spots[int(choice)] = fontstyle.apply(self.__check_turn(), 'red' if self.__check_turn() == 'X' else 'green')
    # ----------------------------------------------------------

    def __DFS_computer_move(self, board, player):
        stack = [(board, player, None)]
        while stack:
            current_board, current_player, move = stack.pop()
            available_spots = self.__available_spots(current_board.copy())

            if self.__only_check_for_win(current_board.copy(), self.__computer):
                return move
            elif not available_spots:
                return move

            for spot in available_spots:
                if spot is not None and isinstance(spot, str):
                    temp = current_board.copy()
                    temp[int(spot)] = current_player
                    next_player = self.__huPlayer if current_player == self.__computer else self.__computer
                    stack.append((temp, next_player, spot))

        return None
    # ----------------------------------------------------------

    def __BFS_computer_move(self, board, player):
        queue = deque([(board, player, None)])

        while queue:
            current_board, current_player, move = queue.popleft()
            available_spots = self.__available_spots(current_board.copy())

            if self.__only_check_for_win(current_board.copy(), self.__computer):
                return move
            elif not available_spots:
                return move

            for spot in available_spots:
                temp = current_board.copy()
                temp[int(spot)] = current_player
                next_player = self.__huPlayer if current_player == self.__computer else self.__computer
                queue.append((temp, next_player, spot))

        return None
    # ----------------------------------------------------------

    def __DFS_limited_computer_move(self, board, player, max_depth=100):
        for depth_limit in range(1, max_depth + 1):
            move = self.__dfs_limited(board.copy(), player, depth_limit)
            if move is not None:
                return move

        return None

    def __dfs_limited(self, board, player, depth_limit):
        stack = [(board, player, None, 0)]

        while stack:
            current_board, current_player, move, depth = stack.pop()
            available_spots = self.__available_spots(current_board.copy())

            if depth >= depth_limit:
                continue

            if self.__only_check_for_win(current_board.copy(), self.__computer):
                return move
            elif not available_spots:
                return move

            for spot in available_spots:
                temp = current_board.copy()
                temp[int(spot)] = current_player
                next_player = self.__huPlayer if current_player == self.__computer else self.__computer
                stack.append((temp, next_player, spot, depth + 1))

        return None

    # ----------------------------------------------------------
    class __UCS_GameNode:
        def __init__(self, board, player, move, cost):
            self.board = board
            self.player = player
            self.move = move
            self.cost = cost

        def __lt__(self, other):
            return self.cost < other.cost

    def __UCS_computer_move(self, board, player):
        start_node = self.__UCS_GameNode(board, player, None, 0)
        priority_queue = [start_node]

        while priority_queue:
            current_node = heapq.heappop(priority_queue)
            current_board = current_node.board
            current_player = current_node.player
            move = current_node.move
            path_cost = current_node.cost

            available_spots = self.__available_spots(current_board.copy())

            if self.__only_check_for_win(current_board.copy(), self.__computer):
                return move

            for spot in available_spots:
                temp = current_board.copy()
                temp[int(spot)] = current_player
                next_player = self.__huPlayer if current_player == self.__computer else self.__computer
                next_cost = path_cost + 1
                next_node = self.__UCS_GameNode(temp, next_player, spot, next_cost)
                heapq.heappush(priority_queue, next_node)

        return None
    # ----------------------------------------------------------

    class __GREEDY_GameNode:
        def __init__(self, board, player, move, heuristic):
            self.board = board.copy()
            self.player = player
            self.move = move
            self.heuristic = heuristic

        def __lt__(self, other):
            return self.heuristic < other.heuristic

    def __GREEDY_computer_move(self, board, player):
        start_node = self.__GREEDY_GameNode(board, player, None, self.__heuristic(board.copy(), self.__computer))
        priority_queue = [start_node]

        while priority_queue:
            current_node = heapq.heappop(priority_queue)
            current_board = current_node.board
            current_player = current_node.player
            move = current_node.move
            available_spots = self.__available_spots(current_board.copy())

            if self.__only_check_for_win(current_board.copy(), self.__computer):
                return move

            for spot in available_spots:
                temp = current_board.copy()
                temp[int(spot)] = current_player
                next_player = self.__huPlayer if current_player == self.__computer else self.__computer
                heuristic_value = self.__heuristic(temp.copy(), self.__computer)
                next_node = self.__GREEDY_GameNode(temp, next_player, spot, heuristic_value)
                heapq.heappush(priority_queue, next_node)

        return None
    # ----------------------------------------------------------

    class __AStarGameNode:
        def __init__(self, board, player, move, cost, heuristic):
            self.board = board.copy()
            self.player = player
            self.move = move
            self.cost = cost
            self.heuristic = heuristic

        def __lt__(self, other):
            return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __AStar_computer_move(self, board, player):
        start_node = self.__AStarGameNode(board, player, None, 0, self.__heuristic(board.copy(), self.__computer))
        priority_queue = [start_node]
        visited = set()

        while priority_queue:
            current_node = heapq.heappop(priority_queue)
            current_board = current_node.board
            current_player = current_node.player
            move = current_node.move
            cost = current_node.cost

            if tuple(current_board.values()) in visited:
                continue

            visited.add(tuple(current_board.values()))

            if self.__only_check_for_win(current_board.copy(), self.__computer):
                return move

            available_spots = self.__available_spots(current_board.copy())

            for spot in available_spots:
                temp = current_board.copy()
                temp[int(spot)] = current_player
                next_player = self.__huPlayer if current_player == self.__computer else self.__computer
                next_heuristic = self.__heuristic(temp.copy(), self.__computer)
                next_cost = cost + 1
                next_node = self.__AStarGameNode(temp, next_player, spot, next_cost, next_heuristic)
                heapq.heappush(priority_queue, next_node)

        return None
    # ----------------------------------------------------------

    def __Minimax_computer_move(self, new_board, player):
        available_spots = [key for key, value in new_board.items() if value not in [self.__huPlayer, self.__computer]]

        if self.__only_check_for_win(new_board, self.__huPlayer):
            return -10, None
        elif self.__only_check_for_win(new_board, self.__computer):
            return 10, None
        elif not available_spots:
            return 0, None

        moves = []

        for spot in available_spots:
            move = {'index': new_board[spot]}
            new_board[spot] = player

            if player == self.__computer:
                score, _ = self.__Minimax_computer_move(new_board, self.__huPlayer)
                move['score'] = score
            else:
                score, _ = self.__Minimax_computer_move(new_board, self.__computer)
                move['score'] = score

            new_board[spot] = move['index']
            moves.append(move)

        bestMove = None

        if player == self.__computer:
            bestScore = -10000
            for i in range(len(moves)):
                if moves[i]['score'] > bestScore:
                    bestScore = moves[i]['score']
                    bestMove = i
        else:
            bestScore = 10000
            for i in range(len(moves)):
                if moves[i]['score'] < bestScore:
                    bestScore = moves[i]['score']
                    bestMove = i

        return moves[bestMove]['score'], moves[bestMove]['index']
    # ----------------------------------------------------------

    def __heuristic(self, board, computer_player):
        heuristic_value = 0

        for combo in self.winning_combinations:
            marks = [board[i] for i in combo]
            if marks.count(computer_player) == 2 and marks.count(self.__huPlayer) == 0:
                heuristic_value += 1

        return heuristic_value

    def __available_spots(self, current_board):
        return [str(k) for k, v in current_board.items() if v not in [self.__huPlayer, self.__computer]]

    def __only_check_for_win(self, board, player):
        for combo in self.winning_combinations:
            if all(board[i] == player for i in combo):
                return True
        return False

    def __check_for_win(self):
        for combo in self.winning_combinations:
            if all(self.__spots[i] == self.__spots[combo[0]] for i in combo):
                for i in combo:
                    self.__spots[i] = fontstyle.apply(self.__spots[i],
                                                      'bold/green/UNDERLINE' if self.__check_current_turn() == 'X' else 'bold/red/UNDERLINE')
                return True
        return False


game = tic_tac_toe()
game.play()
