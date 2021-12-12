from bfs import Bfs
from dfs import Dfs
from a_star import Astar
from reader import Reader
from node import Node
import argparse

#####################################
# CONDITION
#####################################
# TODO dodać czytanie parametrów podczas wywoływania i w zależności od parametrów odpowiedni algorytm

# Parsing
parser = argparse.ArgumentParser(description="Algorithm, strategy, source file, solution file, statistics file.")
parser.add_argument('algorithm')
parser.add_argument('strategy')
parser.add_argument('source_file')
parser.add_argument('solution_file')
parser.add_argument('statistic_file')
args = parser.parse_args()


board = Reader.read(args.source_file)
MAX_DEPTH = 22
start_node = Node(board, "ROOT", [], args.strategy)  # TODO puzzle size somewhere


# TODO przekopiować to co niżej do tego if statementu
if args.algorithm == 'dfs':
    pass
elif args.algorithm == 'bfs':
    pass
elif args.algorithm == 'astr':
    if args.strategy == 'hamm':
        pass
    elif args.strategy == 'manh':
        pass
    else:
        raise "wrong heuristic"
else:
    raise "wrong algorithm"

# TODO save()
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
