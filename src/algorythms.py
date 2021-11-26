from copy import deepcopy
from abc import ABC, abstractmethod

from node import Node


class Algorithm(ABC):

    def __init__(self, board: Node):
        self.node = board
        self.SOLVED_BOARD = [[1, 2, 3, 4],
                             [5, 6, 7, 8],
                             [9, 10, 11, 12],
                             [13, 14, 15, 0]]
        self.move_counter = 0
        self.solution_moves = ''
        self.length_of_solution = 0

    @abstractmethod
    def simulation(self):
        pass

    def print_all_values(self):
        print(f"TURN: {self.move_counter}")
        print(self.node.current_board)
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
