import os


class Reader:

    @staticmethod
    def read(file_name: str):
        with open(os.path.join(os.getcwd(), f"data/{file_name}.txt"), 'r') as file:
            result = tuple(tuple(int(x) for x in line.split()) for line in file)
        return result

    @staticmethod
    def save(content_to_save: str):
        with open(os.path.join(os.getcwd(), "results/pattern.txt"), 'w') as file:
            file.write(content_to_save)
