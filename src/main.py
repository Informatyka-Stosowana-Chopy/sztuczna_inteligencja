from bfs import Bfs
from reader import Reader
import time

board = Reader.read()
bfs = Bfs(board)
begin = time.time()
print(bfs.simulation())
print(f"TURNS: {bfs.move_counter}")
end = time.time()
print(f"Time: {end - begin}")
