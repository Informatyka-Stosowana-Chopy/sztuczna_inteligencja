from abc import ABC, abstractmethod

from node import Node

import time


def count_time(func):
    def wrapper(*args):
        begin_time = time.time()
        func(*args)
        end_time = time.time()
        print("SOLUTION TIME: " + str(end_time - begin_time) + "\n")
    return wrapper


class Algorithm(ABC):

    def __init__(self, board: Node):
        self.node = board
        self.SOLVED_BOARD = [[1, 2, 3, 4],
                             [5, 6, 7, 8],
                             [9, 10, 11, 12],
                             [13, 14, 15, 0]]
        self.move_counter = 0
        self.results = ""
        self.amount_of_visited_nodes = 0
        self.amount_of_processed_nodes = 0
        self.reached_max_depth = 0
        self.len_of_solution = 0

    @abstractmethod
    def simulation(self):
        pass

    def is_solved(self):
        if self.node.current_board == self.SOLVED_BOARD:
            return True
        return False

    def _print_and_return_results(self):
        self.results = "WAY: " + str(self.node.way) + "\n"
        self.results += "DEPTH: " + str(len(self.node.way)) + "\n"
        self.results += "MAX SEARCHED DEPTH: " + str(len(self.node.way)) + "\n"
        self.results += "ITERATIONS: " + str(self.move_counter) + "\n"
        self.results += "VISITED NODES: " + str(self.amount_of_visited_nodes) + "\n"
        self.results += "PROCESSED NODES: " + str(self.amount_of_processed_nodes)
        # Time is printed in decorators
        print(self.results)
        return self.results
