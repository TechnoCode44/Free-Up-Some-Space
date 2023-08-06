# Free Up Some Space

A module to analyse disk usage in Python.

## Scan sub-module

This module contains functions used for scanning directories for information.

### get_files_in_directory function

The `get_files_in_directory` function is used to get all of the files in the directory and sub-directories. It takes one parameter of the  `directory path` and returns a list of `file paths`.

### get_file_data function

The `get_file_data` function is used to get metadata of a file. It takes the file path as a parameter and returns and dictionary of metadata.

Metadata includes:

- File path
- Size
- Modification Time
- Access Time

---

Both functions can be used to get all the metadata from a directory

```python
directory = "foo"
file_paths = get_files_in_directory(directory)

files_data = []
for file in file_paths:
    file_data = get_file_data(file)
    files_data.append(file_data)

print(file_data) # All metadata in the directory
```

## Convert sub-module

This module contains functions that convert numbers to readable strings.

### bytes_to_string function

The `bytes_to_string` function takes an interger in bytes and returns the converted unit in a string. There is an optinoal short string option.

```python
bytes_to_string(2048) # 2 Kilobytes
bytes_to_string(4096, True) # 4 KB
```

---

## Cache sub-module

This sub-module contains functions that help cache data used in the program to improve load times.

### Saving & Loading file paths

You can use the `save_file_paths` function to save file paths. And the `load_file_paths` function to load file paths. They take the `directory path` as a prameter so you can cache multiple directories.

```python
directory = "/"
foo = ["/foo/bar/foo.py", "/foo/bar.sh", "/foo/hi/bye.txt"]

save_file_paths(foo, directory) # Saves to "cache/-foo/files.cache"
load_file_paths(directory) # ["bar/foo.py", "foo/bar.sh", "hi/bye.txt"]
```

### Saving & Loading file data

You can use the `save_file_data` function to save file metadata. And the `load_file_data` function to load file metadata. They take the `directory path` as a prameter so you can cache multiple directories.

```python
directory = "/foo"
file_data = [
    {
        "File Path": "/foo/bar/foo.py",
        "Size": 3246369,
        "Modification Time": 1483129319.727746,
        "Access Time": 1688678899.6798375
    },
    {
        "File Path": "/foo/bar.sh",
        "Size": 47791053,
        "Modification Time": 1689706553.113796,
        "Access Time": 1689706532.781569
    },
    {
        "File Path": "/foo/hi/bye.txt",
        "Size": 23,
        "Modification Time": 1672352802.3541133,
        "Access Time": 1688678899.559835
    },
]

save_file_data(file_data, directory) # Saves to "cache/-foo/file_data.cache"
loaded_file_data = load_file_data(directory) 
file_data == loaded_file_data # True

```