user_list, hobby_list = [], []


def read_users(name_file, list_work):
    with open(name_file, "r", encoding="utf-8") as f:
        while True:
            reader = f.readline()
            if not reader or reader == "\n":
                break
            list_work.append(reader.strip())


def enter_str(f_str=""):
    if len(user_list) >= len(hobby_list):
        for name in user_list:
            if not hobby_list:
                f_str += f"{name}: {None}\n"
            for hobby in hobby_list:
                f_str += f"{name}: {hobby}\n"
                hobby_list.remove(hobby)
                break
        return f_str
    else:
        raise Exception("Length users.csv < than hobby.csv")


def wrote(name):
    with open(name, "w", encoding="utf-8") as f:
        f.write(enter_str())


if __name__ == "__main__":
    read_users("users.csv", user_list)
    read_users("hobby.csv", hobby_list)
    wrote("users_hobby.txt")
