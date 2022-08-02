from threading import Thread
from os import makedirs, remove
from os.path import exists
from shutil import disk_usage
from global_functions import *

def write(data, file, free_space):
    full = False
    with open(file, "w") as file:
        while not full:
            try:
                for _ in range(int(free_space / 1024)): file.write(data) # File size increased 1gb
            except:
                full = True

def cram_progress(DRIVE):
    last_free_space = 0
    frame = Frames(60)

    while True:
        disk_space = disk_usage(DRIVE)
        free_space = round(disk_space[1] / disk_space[0] * 100, 3)

        if not last_free_space == free_space:
            frame.clear()
            print(f"Complete: {free_space}%    Free space: {size_format(disk_space[2])}    Total: {size_format(disk_space[0])}    Used: {size_format(disk_space[1])}")

        if disk_space[2] <= 1024:
            print("Completed!")
            break
        last_free_space = free_space


def cram(DRIVE): # Deletes permenantly deleted files

    DRIVE = f"{DRIVE}:"
    BIG_FILE = "{}\\tmp\\Big file{}.txt"
    FREE_SPACE = disk_usage(DRIVE)[2] # Gets free space in bytes
    BINARY = "1" * 1048576 # 1gb of data
    threads = []
    frame = Frames(60)

    print(f"Found {size_format(round(FREE_SPACE))} on the drive {DRIVE[0]}")

    if not exists(f"{DRIVE}\\tmp"):makedirs(f"{DRIVE}\\tmp")

    for thread_num in range(50): threads.append(Thread(target=write, args=(BINARY, BIG_FILE.format(DRIVE, thread_num), FREE_SPACE,)))
    threads.append(Thread(target=cram_progress, args=(DRIVE,)))
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    print("Finishing up..")
    popen(f"cipher /w:{DRIVE}")
    frame.clear()

    print("Cleaning up...")
    files_removed = 0
    for file_num in range(50):
        files_removed += 1
        remove(BIG_FILE.format(DRIVE, file_num))
        frame.clear()
        print(f"Removed: {files_removed}/50 files")
    
    print("Done!!")