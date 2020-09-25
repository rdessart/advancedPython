from os import path


def launch_analysis(data_file):
    directory = path.dirname(__file__)
    path_to_file = path.join(directory, "data", data_file)
    with open(path_to_file, "r") as f:
        print(f.readline())


if __name__ == "__main__":
    launch_analysis('current_mps.csv')