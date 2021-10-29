from queue import Queue
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
        while self.current_bord == self.SOLVED_BOARD:
            if self.current_bord not in closed_list:
                self.get_children()
                open_list.append(self.children)
                closed_list.append(self.current_bord)

            self.current_bord = open_list[self.move_counter]
            self.move_counter += 1



        return "solved"  # TODO

    def _is_valid_move(self):
        """
        used in get_children

        check if given direction is valid,
        f.g. if there is direction = 'L' it have to check if 0 is not on the extreme left
        :return:
        """
        flag = True
        self.valid_moves = []

        for move in self.MOVES:
            if move == 'L':
                for i in range(4):
                    if 0 in self.current_bord[i][0]:
                        flag = False
                        break
                if flag:
                    self.valid_moves.append('L')
            elif move == 'R':
                for i in range(4):
                    if 0 in self.current_bord[i][3]:
                        flag = False
                        break
                if flag:
                    self.valid_moves.append('R')
            elif move == 'U':
                for i in range(4):
                    if 0 in self.current_bord[0][i]:
                        flag = False
                        break
                if flag:
                    self.valid_moves.append('U')
            elif move == 'D':
                for i in range(4):
                    if 0 in self.current_bord[3][i]:
                        flag = False
                        break
                if flag:
                    self.valid_moves.append('D')
            else:
                raise "Not valid move"
            flag = True

    def __search_zero(self):
        for i in range(4):
            for j in range(4):
                if self.SOLVED_BOARD[i][j] == 0:
                    return i, j
        return ValueError

    def get_children(self):
        """
        inside if statement append self.children with children of current board
        :return:
        """
        self._is_valid_move()
        self.children = []
        zero_coordinates = self.__search_zero()

        if 'L' in self.valid_moves:
            left_board = deepcopy(self.current_bord)
            left_board[zero_coordinates[0]][zero_coordinates[1]], left_board[zero_coordinates[0]][zero_coordinates[1] -1] \
                = left_board[zero_coordinates[0]][zero_coordinates[1] -1], left_board[zero_coordinates[0]][zero_coordinates[1]]
            self.children.append(left_board)
        if 'R' in self.valid_moves:
            right_board = deepcopy(self.current_bord)
            right_board[zero_coordinates[0]][zero_coordinates[1]], right_board[zero_coordinates[0]][zero_coordinates[1] + 1] \
                = right_board[zero_coordinates[0]][zero_coordinates[1] + 1], right_board[zero_coordinates[0]][zero_coordinates[1]]
            self.children.append(right_board)
        if 'U' in self.valid_moves:
            up_board = deepcopy(self.current_bord)
            up_board[zero_coordinates[0]][zero_coordinates[1]], up_board[zero_coordinates[0] - 1][zero_coordinates[1]] \
                = up_board[zero_coordinates[0] - 1][zero_coordinates[1]], up_board[zero_coordinates[0]][zero_coordinates[1]]
            self.children.append(up_board)
        if 'D' in self.valid_moves:
            down_board = deepcopy(self.current_bord)
            down_board[zero_coordinates[0]][zero_coordinates[1]], down_board[zero_coordinates[0] + 1][zero_coordinates[1]] \
                = down_board[zero_coordinates[0] + 1][zero_coordinates[1]], down_board[zero_coordinates[0]][zero_coordinates[1]]
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
