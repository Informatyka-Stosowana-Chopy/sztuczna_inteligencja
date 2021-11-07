from algorythms import Algorithm
from queue import LifoQueue


class Dfs(Algorithm):

    def __init__(self, board: list):
        super().__init__(board)

    def simulation(self):
        open_list = LifoQueue()
        closed_list = set()

        open_list.put(self.current_board_tuple)
        while self.current_board != self.SOLVED_BOARD:
            self.current_board_tuple = open_list.get()
            self.update_list()
            if self.current_board == self.SOLVED_BOARD:
                return f"solved in {self.move_counter - 1} moves"  # TODO

            if self.current_board_tuple not in closed_list:
                self.get_children()
                for child in reversed(self.children):
                    if child not in closed_list:
                        open_list.put(child)
                closed_list.add(self.current_board_tuple)

            # self.print_all_values()
            self.move_counter += 1

        return f"solved in {self.move_counter - 1} moves"  # TODO
