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
            print("\033[22;39mComplete: \033[1;92m{}%   \033[22;39m Free space: \033[1;92m{}   \033[22;39m Total: \033[1;92m{}   \033[22;39m Used: \033[1;92m{}".format(free_space, size_format(disk_space[2]), size_format(disk_space[0]), size_format(disk_space[1])))

        if disk_space[2] <= 1024:
            print("\033[32m[Completed!]\033[0m")
            break
        last_free_space = free_space


def cram(DRIVE): # Deletes permenantly deleted files

    DRIVE = f"{DRIVE}:"
    BIG_FILE = "{}\\tmp\\Big file{}.txt"
    FREE_SPACE = disk_usage(DRIVE)[2] # Gets free space in bytes
    BINARY = "1" * 1048576 # 1gb of data
    threads = []
    frame = Frames(60)

    print(f"\033[32m[Info]\033[0m Found {size_format(round(FREE_SPACE))} on the drive {DRIVE[0]}")

    if not exists(f"{DRIVE}\\tmp"):makedirs(f"{DRIVE}\\tmp")

    for thread_num in range(50): threads.append(Thread(target=write, args=(BINARY, BIG_FILE.format(DRIVE, thread_num), FREE_SPACE,)))
    threads.append(Thread(target=cram_progress, args=(DRIVE,)))
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    print("\033[32m[Finishing up]\033[0m")
    popen(f"cipher /w:{DRIVE}")
    frame.clear()

    files_removed = 0
    for file_num in range(50):
        files_removed += 1
        remove(BIG_FILE.format(DRIVE, file_num))
        frame.clear()
        print("\033[32m[Cleaning up]\033[0m")
        print("\033[32m[Progress]\033[0m Removed: {}/50 files".format(files_removed))
    
    print("\033[32m[Done]\033[0m")