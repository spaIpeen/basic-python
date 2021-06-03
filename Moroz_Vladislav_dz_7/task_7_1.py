import os

root_dir, sub_dir = "my_project", ["settings", "mainapp", "adminapp", "authapp"]
for sub in sub_dir:
    dir_path = os.path.join(root_dir, sub)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
