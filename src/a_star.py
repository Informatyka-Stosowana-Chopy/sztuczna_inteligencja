from algorythms import Algorithm, count_time

from node import Node


class Astar(Algorithm):
    def __init__(self, board: Node, max_depth: int, heuristic: str):
        super().__init__(board)
        self.max_depth = max_depth

        if heuristic == 'hamming':
            self.calculate_heuristic = self._calculate_hamming_distance
        elif heuristic == 'manhattan':
            self.calculate_heuristic = self._calculate_manhattan_distance

    @count_time
    def simulation(self):
        amount_of_visited_nodes = 1
        amount_of_processed_nodes = 1

        while True:
            try:
                if self.is_solved():
                    return self._print_and_return_results()

            except MemoryError:
                pass  # TODO

    def _calculate_hamming_distance(self):
        hamming_distance = 0
        for index_row, row in enumerate(self.node.current_board):
            for index_col, value in enumerate(row):
                target_row, target_col = self.__get_index_from_solved_board(value)
                if abs(index_row - target_row) + abs(index_col - target_col) != 0:
                    hamming_distance += 1
        return hamming_distance

    def _calculate_manhattan_distance(self):
        manhattan_distance = 0
        for index_row, row in enumerate(self.node.current_board):
            for index_col, value in enumerate(row):
                target_row, target_col = self.__get_index_from_solved_board(value)
                manhattan_distance += abs(index_row - target_row) + abs(index_col - target_col)
        return manhattan_distance

    def __get_index_from_solved_board(self, value: int):
        for y in range(4):
            for x in range(4):
                if self.SOLVED_BOARD[y][x] == value:
                    return y, x
