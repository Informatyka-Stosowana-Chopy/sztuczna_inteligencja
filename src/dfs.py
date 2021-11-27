from algorythms import Algorithm, count_time
from queue import LifoQueue

from node import Node


class Dfs(Algorithm):

    def __init__(self, board: Node, max_depth: int):
        super().__init__(board)
        self.max_depth = max_depth

    @count_time
    def simulation(self):
        open_list = LifoQueue()
        closed_list = set()

        open_list.put(self.node)
        while not open_list.empty():
            if self.is_solved():
                return self._print_and_return_results()

            self.move_counter += 1
            self.node = open_list.get()

            if len(self.node.way) > self.max_depth:
                closed_list.add(self.node.current_board_tuple)
                self.node = self.node.parent

            if self.node.current_board_tuple not in closed_list:
                closed_list.add(self.node.current_board_tuple)
                self.node.get_children()
                for child in reversed(self.node.children):
                    if child.current_board_tuple not in closed_list:
                        open_list.put(child)

        print("No solution founded!")
        return "No solution founded!"
