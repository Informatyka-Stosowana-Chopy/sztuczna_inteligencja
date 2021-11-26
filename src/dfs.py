from algorythms import Algorithm
from queue import LifoQueue

from node import Node


class Dfs(Algorithm):

    def __init__(self, board: Node, max_depth: int):
        super().__init__(board)
        self.max_depth = max_depth
        self.depth = 0

    def simulation(self):
        open_list = LifoQueue()
        closed_list = set()

        open_list.put(self.node.current_board_tuple)
        while self.node.current_board != self.SOLVED_BOARD:

            self.move_counter += 1
            self.length_of_solution += 1
            self.depth = len(self.node.way) - 1

            if self.move_counter < self.max_depth or 0 == 0:
                next_node = Node(open_list.get(), self.node, self.node.way)
                self.node = next_node
                if self.node.current_board == self.SOLVED_BOARD:
                    return f"solved in {self.move_counter - 1} moves"  # TODO

                if self.node.current_board_tuple not in closed_list:
                    closed_list.add(self.node.current_board_tuple)
                    self.node.get_children()
                    for child in reversed(self.node.children):
                        if child.current_board_tuple not in closed_list:
                            open_list.put(child.current_board_tuple)


                # self.print_all_values()

            else:
                # TODO
                pass

        return f"solved in {self.move_counter - 1} moves"  # TODO
