def save_file_paths(files: list):
    with open("cache/files.txt", "w") as cache_file:
        for file in files:
            cache_file.write(f"{file}\n")