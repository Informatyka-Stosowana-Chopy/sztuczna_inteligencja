import random

from algorythms import Algorithm, count_time

from node import Node

from queue import Queue


class Astar(Algorithm):
    def __init__(self, board: Node, heuristic: str):
        super().__init__(board)
        self.max_depth = 20

        if heuristic == 'hamm':
            self.calculate_heuristic = self._calculate_hamming_distance
        elif heuristic == 'manh':
            self.calculate_heuristic = self._calculate_manhattan_distance

    @count_time
    def simulation(self):
        open_list = Queue()
        closed_list = set()

        open_list.put(self.node)
        while not open_list.empty():
            if self.move_counter < 1000:
                if self.is_solved():
                    return self._print_and_return_results()

                self.move_counter += 1
                self.node = open_list.get()
                self.amount_of_visited_nodes += 1

                if len(self.node.way) > self.reached_max_depth:
                    self.reached_max_depth = len(self.node.way)

                if self.node.current_board_tuple not in closed_list:
                    self.node.get_children()

                    for child in self.node.children:
                        child.distance = self.calculate_heuristic(child.current_board)
                        self.node.children_distance[child] = child.distance

                    minimum_distance = min(self.node.children_distance.values())
                    nodes_with_minimum_distance = [node for node in self.node.children_distance if
                                                   self.node.children_distance[node] == minimum_distance]

                    for child in nodes_with_minimum_distance:
                        open_list.put(child)
                    self.amount_of_processed_nodes += 1
            else:
                self.len_of_solution = -1
                return -1
            
        self.len_of_solution = -1
        return -1

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
