from algorythms import Algorithm

board = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 0, 12],
         [13, 14, 15, 11]]

bfs = Algorithm(board)
print(bfs.bfs())
print(bfs.current_bord)
