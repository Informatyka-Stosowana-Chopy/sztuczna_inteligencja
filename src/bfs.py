from algorythms import Algorithm, count_time
from queue import Queue
from node import Node


class Bfs(Algorithm):

    def __init__(self, board: Node):
        super().__init__(board)

    @count_time
    def simulation(self):
        """
        wszerz

        story:
        check if the board is solved
        check if the bord isn't in closed list
        check valid moves
        get children
        check if the children are solved
        append open list with children (if already doesn't exist)
        if it is ont valid board, then remove from open list and add to closed
        :return:
        """

        open_list = Queue()
        closed_list = set()

        open_list.put(self.node)
        while not open_list.empty():
            if self.is_solved():
                return self._print_and_return_results()

            self.move_counter += 1
            self.node = open_list.get()

            self.amount_of_visited_nodes += 1
            if len(self.node.way) > self.reached_max_depth:
                self.reached_max_depth = len(self.node.way)

            if self.node.current_board_tuple not in closed_list:
                closed_list.add(self.node.current_board_tuple)
                self.node.get_children()

                for child in self.node.children:
                    if child.current_board_tuple not in closed_list:
                        open_list.put(child)

            self.amount_of_processed_nodes += 1

        print("No solution founded!")
        self.len_of_solution = -1
        return "No solution founded!"
