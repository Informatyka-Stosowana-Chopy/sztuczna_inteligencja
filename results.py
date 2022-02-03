import subprocess
import os
BOARDS = os.listdir("data/")
STRATEGY = ['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD']
HEURISTIC = ['manh', 'hamm']
for i, board in enumerate(BOARDS):
    depth = board.split("_")
    for strategy in STRATEGY:
        # subprocess.run(f"py src/main.py bfs {strategy} {board} solution_{depth[1]}_{i+1}_{strategy}_bfs.txt statistic_{depth[1]}_{i+1}_{strategy}_bfs.txt")
        subprocess.run(f"py src/main.py dfs {strategy} {board} solution_{depth[1]}_{i+1}_{strategy}_dfs.txt statistic_{depth[1]}_{i+1}_{strategy}_dfs.txt")
    # for heuristic in HEURISTIC:
    #     subprocess.run(f"py src/main.py astr {heuristic} {board} solution_{depth[1]}_{i + 1}_{heuristic}.txt statistic_{depth[1]}_{i + 1}_{heuristic}.txt")
