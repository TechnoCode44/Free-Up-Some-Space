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