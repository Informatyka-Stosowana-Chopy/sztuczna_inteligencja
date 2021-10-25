class Algorithm:
    def __init__(self):
        self.current_bord = []
        self.children = []
        self.valid_moves = []

    def bfs(self, board: list):
        """
        wszerz

        story:
        check if the board is solved
        check if the bord isn't in closed list
        check valid moves
        get children
        check if the childres are solved
        append open list with children (if already doesn't exist)
        if it is ont valid board, then remove from open list and add to closed
        :return:
        """

        open_list = set()
        closed_list = set()

    def is_valid_move(self, direction: str):
        """
        check if given direction is valid,
        f.g. if there is direction = 'L' it have to check if 0 is not on the extreme left
        :param direction:
        :return:
        """
        pass
        # self.valid_moves - clear
        # append self.valid_moves with valid move

    def get_children(self):
        """
        inside if statement append self.children with children of current board
        :return:
        """
        if 'L' in self.valid_moves:
            pass
        elif 'R' in self.valid_moves:
            pass
        elif 'U' in self.valid_moves:
            pass
        elif 'D' in self.valid_moves:
            pass




#####################################3
    def dfs(self):
        """
        wgłąb
        :return:
        """
        pass

    def a_star(self):
        """
        heurystyka
        :return:
        """
        pass
