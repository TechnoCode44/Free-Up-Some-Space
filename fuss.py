if __name__ == "__main__":
    print("[Loading]")
    from scan import *
    from global_functions import *
    from cram import *
    print("[Imported functions]")
    from tkinter.filedialog import askdirectory
    print("[Imported File explorer gui]")

    frame = Frames(60)

    print("Loaded!")
    while True:
        frame.clear()
        print("""ver: 1.0

        How can Free up some space help you?
        
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
            print(f"What drive would you like to use?\nAvailable: {' '.join(drives)}")
            cram(input("> ").capitalize())
        elif answer == "exit":
            print("See you soon")
            sleep(0.5)
            exit()
        else:
            print("\033[31mSorry I don't understand that :(\033[0m")
            sleep(1)