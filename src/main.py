from algorythms import Algorithm
import time
board = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 0, 11],
         [13, 14, 15, 12]]

board_2 = [[0, 1, 2, 7],
           [8, 9, 12, 10],
           [13, 3, 6, 4],
           [15, 14, 11, 5]]

bfs = Algorithm(board_2)
begin = time.time()
print(bfs.bfs())
print(f"TURNS: {bfs.move_counter}")
end = time.time()
print(f"Time: {end - begin}")
