user_list, hobby_list, all_in_one = [], [], {}


def read_users(name_file, list_work):
    with open(name_file, "r", encoding="utf-8") as f:
        while True:
            reader = f.readline()
            if not reader or reader == "\n":
                break
            list_work.append(reader.strip())


read_users("users.csv", user_list)
read_users("hobby.csv", hobby_list)
if len(user_list) >= len(hobby_list):
    for i in user_list:
        if not hobby_list:
            all_in_one[i] = None
        for k in hobby_list:
            all_in_one[i] = k
            hobby_list.remove(k)
            break
else:
    raise Exception("Length users.csv < than hobby.csv")
print(all_in_one)

with open("dir.csv", "w", encoding="utf-8") as f:
    f.write(str(all_in_one))
