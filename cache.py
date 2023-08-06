from json import dump, load
from os.path import isdir
from os import mkdir

def save_file_paths(files: list, directory: str):
    directory = directory.replace("/", "-")

    CACHE_DIRECTORY = f"cache/{directory}"
    cache_directory_exists = isdir(CACHE_DIRECTORY)
    if not cache_directory_exists:
        mkdir(CACHE_DIRECTORY)

    with open(f"{CACHE_DIRECTORY}/files.cache", "w") as cache_file:
        for file in files:
            cache_file.write(f"{file}\n")

def load_file_paths(directory: str):
    directory = directory.replace("/", "-")
    CACHE_FILE_PATH = f"cache/{directory}/files.cache"
    cache_file = open(CACHE_FILE_PATH, "r").read()
    file_paths = cache_file.split("\n")
    file_paths = file_paths[:-1] # Last line is empty
    return file_paths

def save_file_data(file_data: list, directory: str): # Function name needs to be plural
    directory = directory.replace("/", "-")

    CACHE_DIRECTORY = f"cache/{directory}"
    cache_directory_exists = isdir(CACHE_DIRECTORY)
    if not cache_directory_exists:
        mkdir(CACHE_DIRECTORY)

    with open(f"{CACHE_DIRECTORY}/file_data.cache", "w", encoding="utf-8") as cache_file:
        dump(file_data, cache_file, ensure_ascii=False, indent=4)

def load_file_data(directory: str):
    directory = directory.replace("/", "-")
    cache_file = open(f"cache/{directory}/file_data.cache")
    file_data = load(cache_file)
    return file_data