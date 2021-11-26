from bfs import Bfs
from dfs import Dfs
from reader import Reader
import time
from node import Node
#####################################
# CONDITION
#####################################
FILE_NAME = "board"

board = Reader.read(FILE_NAME)
MAX_DEPTH = 20
start_node = Node(board, "ROOT", None, [])
#####################################
# DFS
#####################################
dfs = Dfs(start_node, MAX_DEPTH)

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
