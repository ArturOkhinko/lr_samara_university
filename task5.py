import os

PATH_TO_NITROGENOUS_BASESS = 'nitrogenous_bases'

def print_all_files_from_folder(path_to_folder):
    try:
        files = os.listdir(path_to_folder)
        print(files)
    except FileNotFoundError:
        print("Указанная папка не найдена.")
        return []
    
print_all_files_from_folder(PATH_TO_NITROGENOUS_BASESS)