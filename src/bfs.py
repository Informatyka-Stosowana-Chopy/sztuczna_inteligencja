from algorythms import Algorithm


class Bfs(Algorithm):

    def __init__(self, board: list):
        super().__init__(board)

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

        open_list = set()
        closed_list = set()
        # TODO do sth to change list to set

        open_list.add(self.current_board_tuple)
        while self.current_board != self.SOLVED_BOARD:
            self.current_board_tuple = open_list.pop()
            self.update_list()
            if self.current_board == self.SOLVED_BOARD:
                return f"solved in {self.move_counter - 1} moves"  # TODO

            if self.current_board_tuple not in closed_list:
                self.get_children()
                for child in self.children:
                    open_list.add(child)
                closed_list.add(self.current_board_tuple)

            # self.print_all_values()
            self.move_counter += 1

        return f"solved in {self.move_counter - 1} moves"  # TODO