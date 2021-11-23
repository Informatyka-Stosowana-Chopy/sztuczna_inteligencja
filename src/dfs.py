from algorythms import Algorithm
from queue import LifoQueue


class Dfs(Algorithm):

    def __init__(self, board: list, max_depth: int):
        super().__init__(board)
        self.max_depth = max_depth

    def simulation(self):
        open_list = LifoQueue()
        closed_list = set()

        open_list.put(self.current_board_tuple)
        while self.current_board != self.SOLVED_BOARD:

            self.move_counter += 1

            if self.move_counter < self.max_depth:
                self.current_board_tuple = open_list.get()
                self.update_list()
                if self.current_board == self.SOLVED_BOARD:
                    return f"solved in {self.move_counter - 1} moves"  # TODO

                if self.current_board_tuple not in closed_list:
                    self.parents.append(self.current_board_tuple)  # TODO
                    self.get_children()
                    for child in reversed(self.children):
                        if child not in closed_list:
                            open_list.put(child)
                            self.solution_moves += ""  # TODO
                    closed_list.add(self.current_board_tuple)

                # self.print_all_values()

            else:
                closed_list.add(self.parents[-1])
                self.parents.pop(-1)
                self.move_counter = 0

        return f"solved in {self.move_counter - 1} moves"  # TODO
