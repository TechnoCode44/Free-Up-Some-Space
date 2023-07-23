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