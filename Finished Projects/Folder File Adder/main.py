import os


FILE_PATH = os.path.dirname(os.path.realpath(__file__))
FILE_PATH = FILE_PATH.split("CodeStorm-sProjects")[0]

search_folder = f"{FILE_PATH}CodeStorm-sProjects/Future Projects"
sub_folders = [file.path for file in os.scandir(search_folder) if file.is_dir()]

changed_folders = []
for sub_folder in sub_folders:
    if not os.path.exists(os.path.join(sub_folder, "main.py")):
        with open(os.path.join(sub_folder, "main.py"), "w") as file:
            changed_folders.append(sub_folder)

print(f"Folders Changed: {changed_folders}")
