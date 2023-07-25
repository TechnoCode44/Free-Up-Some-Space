# Free Up Some Space

A module to analyse disk usage in Python.

## Scan sub-module

This module contains functions used for scanning directories for information.

### get_files_in_directory function

The `get_files_in_directory` function is used to get all of the files in the directory and sub-directories. It takes one parameter of the  `directory path` and returns a list of `file paths`.

### get_file_data function

the `get_file_data` function is used to get metadata of a file. It takes the file path as a parameter and returns and dictionary of metadata.

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