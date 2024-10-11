import os

PATH_TO_NITROGENOUS_BASESS = 'nitrogenous_bases'

def print_all_files_from_folder(path_to_folder):
    files = os.listdir(path_to_folder)
    print(files)

print_all_files_from_folder(PATH_TO_NITROGENOUS_BASESS)