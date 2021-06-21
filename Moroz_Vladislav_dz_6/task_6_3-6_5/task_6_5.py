import sys
from task_6_4 import read_users, wrote, user_list, hobby_list

try:
    read_users(sys.argv[1], user_list)
    read_users(sys.argv[2], hobby_list)
    wrote(sys.argv[3])
except:
    print("""Пример команды: python task_6_5.py users.csv hobby.csv new.txt
    task_6_5.py -- Имя скрипта
    user.csv -- Имя документа с ФИО пользователей
    hobby.csv -- Имя документа с хобби пользователей
    new.txt -- Имя нового документа, куда все объеденится
    """)

