from os import walk
from os.path import join, getsize, getmtime, getatime, isfile

def get_files_in_directory(directory_path: str):
    file_paths = []

    for current_directory, sub_directories, files_in_directory in walk(directory_path):
        if len(files_in_directory) > 0:
            for file in files_in_directory:
                file_path = join(current_directory, file)
                
                file_exists = isfile(file_path) # Computers like hallucinating???
                if file_exists:
                    file_paths.append(file_path)
    
    return file_paths

def get_file_data(file_path: str):
    file_size = getsize(file_path)
    file_last_modification_time = getmtime(file_path)
    file_last_access_time = getatime(file_path)
    file_data = {
        "File Path": file_path,
        "Size": file_size,
        "Modification Time": file_last_modification_time,
        "Access Time": file_last_access_time
    }
    return file_data

