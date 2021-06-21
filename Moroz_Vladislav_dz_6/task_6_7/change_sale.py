from sys import argv
from task_6_7 import change_data, tell_read

tell_read()
try:
    change_data(int(argv[1]), argv[2])
except IndexError:
    print("Введите корректный номер записи!")
