from sys import argv
from task_6_7 import read_data


if len(argv) == 1:
    read_data()
elif len(argv) == 2:
    read_data(int(argv[1]))
elif len(argv) == 3:
    read_data(int(argv[1]), int(argv[2]))
