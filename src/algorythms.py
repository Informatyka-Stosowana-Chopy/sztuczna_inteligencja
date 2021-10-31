from copy import deepcopy


class Algorithm:
    def __init__(self, board: list):
        self.current_bord = board
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

        open_list = []
        closed_list = []
        # TODO do sth to change list to set
        while self.current_bord != self.SOLVED_BOARD:
            if self.current_bord not in closed_list:
                self.get_children()
                open_list.append(self.children)
                closed_list.append(self.current_bord)

            self.current_bord = deepcopy(open_list[self.move_counter])
            open_list[self.move_counter] = None
            self.move_counter += 1



        return "solved"  # TODO

    def _is_valid_move(self):
        """
        used in get_children

        if 0 occurred on one of side, then the corresponding direction is removed from list valid_moves
        :return:
        """
        self.valid_moves = ['L', 'R', 'U', 'D']

        for i in range(4):
            if self.current_bord[i][0] == 0:
                self.valid_moves.remove('L')
            if self.current_bord[i][3] == 0:
                self.valid_moves.remove('R')
            if self.current_bord[0][i] == 0:
                self.valid_moves.remove('U')
            if self.current_bord[3][i] == 0:
                self.valid_moves.remove('D')

    def __search_zero(self):
        for i in range(4):
            for j in range(4):
                if self.current_bord[i][j] == 0:
                    return i, j
        return ValueError

    def get_children(self):
        """
        inside if statement append self.children with children of current board
        :return:
        """
        self._is_valid_move()
        self.children = []
        y, x = self.__search_zero()

        if 'L' in self.valid_moves:
            left_board = deepcopy(self.current_bord)
            left_board[y][x], left_board[y][x - 1] = left_board[y][x - 1], left_board[y][x]
            self.children.append(left_board)
        if 'R' in self.valid_moves:
            right_board = deepcopy(self.current_bord)
            right_board[y][x], right_board[y][x + 1] = right_board[y][x + 1], right_board[y][x]
            self.children.append(right_board)
        if 'U' in self.valid_moves:
            """
            to go up we have to decrease value because it isn't cartesian system.
            it starts from top left corner and this is (0, 0) point.
            """
            up_board = deepcopy(self.current_bord)
            up_board[y][x], up_board[y - 1][x] = up_board[y - 1][x], up_board[y][x]
            self.children.append(up_board)
        if 'D' in self.valid_moves:
            """
            according to above, there is + to go down.
            """
            down_board = deepcopy(self.current_bord)
            down_board[y][x], down_board[y + 1][x] = down_board[y + 1][x], down_board[y][x]
            self.children.append(down_board)




#####################################3
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
