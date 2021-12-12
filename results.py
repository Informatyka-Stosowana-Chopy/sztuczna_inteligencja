import subprocess
import os
BOARDS = os.listdir("data/")
STRATEGY = ['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD']
HEURISTIC = ['manh', 'hamm']

for i, board in enumerate(BOARDS):
    for strategy in STRATEGY:
        subprocess.run(f"py src/main.py bfs {strategy} {board} solution_{i+1}_bfs.txt statistic{i+1}_bfs.txt")
        subprocess.run(f"py src/main.py dfs {strategy} {board} solution_{i+1}_dfs.txt statistic{i+1}_dfs.txt")

    for heuristic in HEURISTIC:
        subprocess.run(f"py src/main.py astr {heuristic} {board} solution_{i + 1}_manh.txt statistic{i+1}_manh.txt")
        subprocess.run(f"py src/main.py astr {heuristic} {board} solution_{i + 1}_hamm.txt statistic{i+1}_hamm.txt")


