from bfs import Bfs
from dfs import Dfs
from a_star import Astar
from reader import Reader
from node import Node
import argparse
import time

#####################################
# CONDITION
#####################################

# Parsing
parser = argparse.ArgumentParser(description="Algorithm, strategy, source file, solution file, statistics file.")
parser.add_argument('algorithm')
parser.add_argument('strategy')
parser.add_argument('source_file')
parser.add_argument('solution_file')
parser.add_argument('statistic_file')
args = parser.parse_args()

board, width, height = Reader.read(args.source_file)
MAX_DEPTH = 20
start_node = Node(board, "ROOT", [], args.strategy, height, width)

begin_time = time.time()
if args.algorithm == 'dfs':
    # print("DFS")
    program = Dfs(start_node, MAX_DEPTH)
    program.simulation()
    print("\n\n")
elif args.algorithm == 'bfs':
    # print("BFS")
    program = Bfs(start_node)
    program.simulation()

elif args.algorithm == 'astr':
    if args.strategy == 'hamm':
        program = Astar(start_node, 'hamm')
        program.simulation()

    elif args.strategy == 'manh':
        program = Astar(start_node, 'manh')
        program.simulation()
    else:
        raise "wrong heuristic"
else:
    raise "wrong algorithm"
end_time = time.time()

program.len_of_solution = len(program.node.way)
time = round(end_time - begin_time, 3)

# save solutution
# Reader.save_solution(args.solution_file, program.len_of_solution, program.node.way) TODO

# save statistic
Reader.save_statistic(args.statistic_file, program.len_of_solution, program.amount_of_visited_nodes,
                      program.amount_of_processed_nodes, program.reached_max_depth, time)
