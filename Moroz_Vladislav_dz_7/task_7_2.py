import os

with open("config.yaml", encoding="utf-8") as f:
    while 1:
        dir_path = f.readline().strip()
        if not dir_path:
            break
        try:
            open(dir_path, "w") if "." in dir_path else os.makedirs(dir_path)
        except FileExistsError as e:
            print(f"{e}: already exists, check the names of the created folders, files")
        except FileNotFoundError as e:
            print(f"{e}: check config.yaml, folder names should not contain '.'")
