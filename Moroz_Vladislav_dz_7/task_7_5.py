import os
from os.path import relpath
import django

dir_check, dict_files, bytes_list = django.__path__[0], {}, [100, 1000, 10000, 100000]


def step_dict(x):
    count, ext_list = 0, []
    for root, dirs, files in os.walk(dir_check):
        for file in files:
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            rel_path = relpath(os.path.join(root, file), dir_check)
            file_size = os.stat(f"{dir_check}\\{rel_path}").st_size
            if 0.1 <= file_size / x <= 1:
                count += 1
                if ext not in ext_list:
                    ext_list.append(ext)
            dict_files[x] = (count, ext_list)


for i in range(len(bytes_list)):
    step_dict(bytes_list[i])
print(dict_files)
