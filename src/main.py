from bfs import Bfs
from dfs import Dfs
from reader import Reader
from node import Node

#####################################
# CONDITION
#####################################
FILE_NAME = "board"

board = Reader.read(FILE_NAME)
MAX_DEPTH = 25
start_node = Node(board, "ROOT", [])
#####################################
# DFS
#####################################
print("DFS")
dfs = Dfs(start_node, MAX_DEPTH)
dfs.simulation()
print("\n\n")
#####################################
# BFS
#####################################
print("BFS")
bfs = Bfs(start_node)
bfs.simulation()
