from bfs import Bfs
from dfs import Dfs
from reader import Reader
import time

#####################################
# CONDITION
#####################################

board = Reader.read()

#####################################
# DFS
#####################################
dfs = Dfs(board)

begin_dfs = time.time()
dfs.simulation()
end_dfs = time.time()

#####################################
# BFS
#####################################
bfs = Bfs(board)

begin_bfs = time.time()
bfs.simulation()
end_bfs = time.time()

#####################################
# PRINT RESULTS
#####################################
print("\n")
print("#################################")
print(f"DFS time: {end_dfs - begin_dfs}")
print(f"TURNS: {dfs.move_counter}")
print("#################################")
print(f"BFS time: {end_bfs - begin_bfs}")
print(f"TURNS: {bfs.move_counter}")
print("#################################")
print("\n")
