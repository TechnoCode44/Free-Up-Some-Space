from os import walk
from os.path import join

def get_files_in_directory(directory_path):
    file_paths = []

    for current_directory, sub_directories, files_in_directory in walk(directory_path):
        if len(files_in_directory) > 0:
            for file in files_in_directory:
                file_path = join(current_directory, file)
                file_paths.append(file_path)
    
    return file_paths