import random

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
            try:  # TODO
                if self.is_solved():
                    return self._print_and_return_results()
                amount_of_processed_nodes += 1

                self.node.get_children()
                for child in self.node.children:
                    child.distance = self.calculate_heuristic(child.current_board)
                    self.node.children_distance[child] = child.distance

                minimum_distance = min(self.node.children_distance.values())
                nodes_with_minimum_distance = [node for node in self.node.children_distance if
                                               self.node.children_distance[node] == minimum_distance]

                random_number = random.randint(0, len(nodes_with_minimum_distance) - 1)
                self.node = nodes_with_minimum_distance[random_number]
                amount_of_visited_nodes += 1

            except MemoryError:
                pass  # TODO

    def _calculate_hamming_distance(self, board):
        hamming_distance = 0
        for index_row, row in enumerate(board):
            for index_col, value in enumerate(row):
                target_row, target_col = self.__get_index_from_solved_board(value)
                if abs(index_row - target_row) + abs(index_col - target_col) != 0:
                    hamming_distance += 1
        return hamming_distance

    def _calculate_manhattan_distance(self, board):
        manhattan_distance = 0
        for index_row, row in enumerate(board):
            for index_col, value in enumerate(row):
                target_row, target_col = self.__get_index_from_solved_board(value)
                manhattan_distance += abs(index_row - target_row) + abs(index_col - target_col)
        return manhattan_distance

    def __get_index_from_solved_board(self, value: int):
        for y in range(4):
            for x in range(4):
                if self.SOLVED_BOARD[y][x] == value:
                    return y, x
