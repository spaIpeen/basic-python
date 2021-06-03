from shutil import copy2, copytree

dir_path1, dir_path2 = "my_project\\authapp\\templates", "my_project\\mainapp\\templates\\mainapp"

copytree(dir_path1, "my_project\\templates")
copytree(dir_path2, "my_project\\templates\\mainapp")

"""
Предполагается, что task_7_3.py выполняется после task_7_2.py
"""
