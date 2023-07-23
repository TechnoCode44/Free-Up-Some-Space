from json import dump

def save_file_paths(files: list):
    with open("cache/files.cache", "w") as cache_file:
        for file in files:
            cache_file.write(f"{file}\n")

def load_file_paths():
    CACHE_FILE_PATH = "cache/files.cache"
    cache_file = open(CACHE_FILE_PATH, "r").read()
    file_paths = cache_file.split("\n")
    file_paths = file_paths[:-1] # Last line is empty
    return file_paths

def save_file_data(file_data: list): # Function name needs to be plural

    with open(f"cache/file_data.cache", "w", encoding="utf-8") as cache_file:
        dump(file_data, cache_file, ensure_ascii=False, indent=4)