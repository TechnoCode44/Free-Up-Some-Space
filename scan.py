from os import walk
from os.path import join, getsize, getmtime
from time import strftime, gmtime
from global_functions import *
from openpyxl import Workbook

def log(file_info): # Creates a excel spreedsheet
    print("\033[32m[Creating Log File]\033[0m")
    workbook = Workbook()
    sheet = workbook.active
    for data in range(len(file_info[0])):
        sheet[f"A{data + 1}"] = file_info[0][data]
        sheet[f"B{data + 1}"] = file_info[1][data]
        sheet[f"C{data + 1}"] = file_info[2][data]
    workbook.save(filename=f"{DESKTOP_PATH}/log.xlsx")
    print("\033[32m[Created Log File On Desktop]\033[0m")
    

def get_info(path, sort):
    files = []
    files_info = []

    print("\033[32m[Getting File Paths]\033[0m")
    for root, directories, dir_files in walk(path): # Gets all the files
        if not len(dir_files) == 0: # Checks if dir contains files
            for file in dir_files: files.append(join(root, file))
    #with open("log.txt", "w") as f:
    #    for file in files: f.write(f"{file}\n")

    print("\033[32m[Getting File Information]\033[0m")
    for file in files:
        # We sort the size variable in the dict so it will sort the paths aswell
        files_info.append({
            "path": file,
            "size": getsize(file),
            "last_used": getmtime(file)
        })

    """
    The sort function iterates over the array and we can give it a
    'key' aka a function.

    This function will return what we want part of the array we want to sort.
    It is as confusing as it sounds :D 
    """
    def sort_parms(sort): return sort["size"]
    files_info.sort(key=sort_parms, reverse=True) # The array is smallast to biggest but we want the biggest files

    # We create new arrays to extract out the info from the main array
    sorted_files = []
    sorted_sizes = []
    last_used = []
    for dict in files_info:
        sorted_files.append(dict["path"])
        sorted_sizes.append(size_format(round(dict["size"], 3)))
        last_used.append(strftime("%Y/%m/%d %H:%M", gmtime(dict["last_used"])))
    return sorted_files, sorted_sizes, last_used