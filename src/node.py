from copy import deepcopy
from copy import copy


class Node:
    def __init__(self, current_board_tuple: tuple, parent, way: list):
        self.current_board_tuple: tuple = current_board_tuple
        self.current_board: list = list(list(x) for x in self.current_board_tuple)
        self.children = []
        self.parent = parent
        self.last_move = None
        self.way = way.copy()
        self.valid_moves = []
        self.distance = 0
        self.children_distance = {}

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
            left_way = copy(self.way)
            left_way.append('L')
            self.children.append(Node(self.__change_list_to_tuple(left_board), self, left_way))
            self.children[-1].last_move = 'L'
        if 'R' in self.valid_moves:
            right_board = deepcopy(self.current_board)
            right_board[y][x], right_board[y][x + 1] = right_board[y][x + 1], right_board[y][x]
            right_way = copy(self.way)
            right_way.append('R')
            self.children.append(Node(self.__change_list_to_tuple(right_board), self, right_way))
            self.children[-1].last_move = 'R'
        if 'U' in self.valid_moves:
            """
            to go up we have to decrease value because it isn't cartesian system.
            it starts from top left corner and this is (0, 0) point.
            """
            up_board = deepcopy(self.current_board)
            up_board[y][x], up_board[y - 1][x] = up_board[y - 1][x], up_board[y][x]
            up_way = copy(self.way)
            up_way.append('U')
            self.children.append(Node(self.__change_list_to_tuple(up_board), self, up_way))
            self.children[-1].last_move = 'U'
        if 'D' in self.valid_moves:
            """
            according to above, there is + to go down.
            """
            down_board = deepcopy(self.current_board)
            down_board[y][x], down_board[y + 1][x] = down_board[y + 1][x], down_board[y][x]
            down_way = copy(self.way)
            down_way.append('D')
            self.children.append(Node(self.__change_list_to_tuple(down_board), self, down_way))
            self.children[-1].last_move = 'D'

    @staticmethod
    def __change_list_to_tuple(board: list):
        return tuple(tuple(x) for x in board)

    def update_list(self):
        self.current_board = list(list(x) for x in self.current_board_tuple)
