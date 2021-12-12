from bfs import Bfs
from dfs import Dfs
from a_star import Astar
from reader import Reader
from node import Node

#####################################
# CONDITION
#####################################
# TODO dodać czytanie parametrów podczas wywoływania i w zależności od parametrów odpowiedni algorytm
FILE_NAME = "board_2"

board = Reader.read(FILE_NAME)
MAX_DEPTH = 25
start_node = Node(board, "ROOT", [])
strategy = 'RDUL'
#####################################
# DFS
#####################################
# print("DFS")
# dfs = Dfs(start_node, MAX_DEPTH)
# dfs.simulation()
# print("\n\n")
# #####################################
# # BFS
# #####################################
# print("BFS")
# bfs = Bfs(start_node)
# bfs.simulation()
#####################################
# HEURISTIC
#####################################
mann = Astar(start_node, 'hamming')
mann.simulation()
