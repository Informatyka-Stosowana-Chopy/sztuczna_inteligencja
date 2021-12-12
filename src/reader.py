import os


class Reader:

    @staticmethod
    def read(file_name: str):
        with open(os.path.join(os.getcwd(), f"data/{file_name}"), 'r') as file:
            size = file.readline()
            size = size.split(" ")
            width = size[0]
            height = size[1]

        with open(os.path.join(os.getcwd(), f"data/{file_name}"), 'r') as file:
            result = tuple(tuple(int(x) for x in line.split()) for i, line in enumerate(file) if i != 0)
        return result, int(width), int(height)

    @staticmethod
    def save_solution(file_name: str, len_solution: int, solution: list):
        with open(os.path.join(os.getcwd(), f"results/{file_name}"), 'w') as file:
            file.write(str(len_solution))
            file.write("\n")
            file.write(str(solution))
            file.write("\n")

    @staticmethod
    def save_statistic(file_name: str, len_solution: int, visited_nodes: int, processed_nodes: int, max_depth: int, time):
        with open(os.path.join(os.getcwd(), f"results/{file_name}"), 'w') as file:
            file.write(str(len_solution))
            file.write("\n")
            file.write(str(visited_nodes))
            file.write("\n")
            file.write(str(processed_nodes))
            file.write("\n")
            file.write(str(max_depth))
            file.write("\n")
            file.write(str(time))
            file.write("\n")
