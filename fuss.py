if __name__ == "__main__":
    print("\033[32;1;6m[Loading]\033[0m")
    from scan import *
    from global_functions import *
    from cram import *
    print("\033[32m[Imported functions]\033[0m")
    from tkinter.filedialog import askdirectory
    print("\033[32m[Imported File explorer gui]\033[0m")

    frame = Frames(60)

    print("\033[32;1;6m[Loaded!]\033[0m")
    while True:
        frame.clear()
        print("""\033[93;6mver: 1.0\033[0m

        \033[1mHow can Free up some space help you?\033[0m
        
        1. Find the biggest files in a specific folder
        2. Delete permanently deleted files""")
        answer = input(" > ")
        frame.clear()
        if answer == "1":
            folder = askdirectory(title="What folder would you like to scan?")
            frame.clear()
            file_paths, file_sizes, last_used = get_info(folder, "size")
            log([file_paths, file_sizes, last_used])
            sleep(1)
        elif answer == "2":
            drives = []
            print("\033[32m[Getting drives]\033[0m")
            for drive in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                drive = f"{drive}:"
                if exists(drive): drives.append(drive)
            
            frame.clear()
            print(f"\033[1mWhat drive would you like to use?\033[0m\nAvailable: {' '.join(drives)}")
            cram(input("> ").capitalize())
        elif answer == "exit":
            print("\033[96mSee you soon \033[3;1;6m\(^▼^)/\033[0m")
            sleep(0.5)
            exit()
        else:
            print("\033[31mSorry I don't understand that :(\033[0m")
            sleep(1)