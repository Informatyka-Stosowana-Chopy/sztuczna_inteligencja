from copy import deepcopy

# TODO
#   make board as 2D numpy array
#   they may be hashable
#   TODO check if they are
#       then if yes change open_list and closed_list to set type


class Algorithm:
    def __init__(self, board: list):
        self.current_board = board
        self.current_board_tuple = tuple(tuple(x) for x in self.current_board)
        self.children = []
        self.valid_moves = []
        self.MOVES = 'LRUD'
        self.SOLVED_BOARD = [[1, 2, 3, 4],
                             [5, 6, 7, 8],
                             [9, 10, 11, 12],
                             [13, 14, 15, 0]]
        self.move_counter = 0
        self.solution_moves = ''

    def bfs(self):
        """
        wszerz

        story:
        check if the board is solved
        check if the bord isn't in closed list
        check valid moves
        get children
        check if the children are solved
        append open list with children (if already doesn't exist)
        if it is ont valid board, then remove from open list and add to closed
        :return:
        """

        open_list = set()
        closed_list = set()
        # TODO do sth to change list to set

        open_list.add(self.current_board_tuple)
        while self.current_board != self.SOLVED_BOARD:
            self.current_board_tuple = open_list.pop()
            self.update_list()
            if self.current_board == self.SOLVED_BOARD:
                return f"solved in {self.move_counter - 1} moves"  # TODO

            if self.current_board_tuple not in closed_list:
                self.get_children()
                for child in self.children:
                    open_list.add(child)
                closed_list.add(self.current_board_tuple)

            # self.print_all_values()
            self.move_counter += 1
            if self.move_counter >= 10000:
                return "10k poszło"

        return f"solved in {self.move_counter - 1} moves"  # TODO

    def _is_valid_move(self):
        """
        used in get_children

        if 0 occurred on one of side, then the corresponding direction is removed from list valid_moves
        :return:
        """
        self.valid_moves = ['L', 'R', 'U', 'D']

        for i in range(4):
            if self.current_board[i][0] == 0:
                self.valid_moves.remove('L')
            if self.current_board[i][3] == 0:
                self.valid_moves.remove('R')
            if self.current_board[0][i] == 0:
                self.valid_moves.remove('U')
            if self.current_board[3][i] == 0:
                self.valid_moves.remove('D')

    def __search_zero(self):
        for y in range(4):
            for x in range(4):
                if self.current_board_tuple[y][x] == 0:
                    return y, x

    def get_children(self):
        """
        inside if statement append self.children with children of current board
        :return:
        """
        self._is_valid_move()
        self.children = []
        y, x = self.__search_zero()

        if 'L' in self.valid_moves:
            left_board = deepcopy(self.current_board)
            left_board[y][x], left_board[y][x - 1] = left_board[y][x - 1], left_board[y][x]
            self.children.append(self.change_list_to_tuple(left_board))
        if 'R' in self.valid_moves:
            right_board = deepcopy(self.current_board)
            right_board[y][x], right_board[y][x + 1] = right_board[y][x + 1], right_board[y][x]
            self.children.append(self.change_list_to_tuple(right_board))
        if 'U' in self.valid_moves:
            """
            to go up we have to decrease value because it isn't cartesian system.
            it starts from top left corner and this is (0, 0) point.
            """
            up_board = deepcopy(self.current_board)
            up_board[y][x], up_board[y - 1][x] = up_board[y - 1][x], up_board[y][x]
            self.children.append(self.change_list_to_tuple(up_board))
        if 'D' in self.valid_moves:
            """
            according to above, there is + to go down.
            """
            down_board = deepcopy(self.current_board)
            down_board[y][x], down_board[y + 1][x] = down_board[y + 1][x], down_board[y][x]
            self.children.append(self.change_list_to_tuple(down_board))

    def print_all_values(self):
        print(f"TURN: {self.move_counter}")
        print(self.current_board)
        print(self.SOLVED_BOARD)
        print("\n")
        print("CURRENT BOARD:")
        for line in self.current_board:
            print(line)
        print("\n")
        print("CHILDREN:")
        for child in self.children:
            print(child)
        print("\n")
        print(f"Valid moves =  {self.valid_moves}")

    @staticmethod
    def change_list_to_tuple(board: list):
        return tuple(tuple(x) for x in board)

    def update_list(self):
        self.current_board = list(list(x) for x in self.current_board_tuple)

#####################################
    def dfs(self):
        """
        wgłąb
        :return:
        """
        pass

    def a_star(self):
        """
        heurystyka
        :return:
        """
        pass
