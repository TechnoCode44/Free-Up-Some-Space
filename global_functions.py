from os import system, popen
from time import time, sleep

class Frames:
    def __init__(self, fps):
        self.fps = fps
        self.frame_time = 1 / self.fps
        self.last_frame_time = 0
    
    def refresh(self): # For timed refresh of frames
        self.refreshed = False
        while not self.refreshed:
            if self.last_frame_time > self.frame_time:
                system("cls")
                self.last_frame_time = time()
                self.refreshed = True
    
    def clear(self): system("cls") # For untimed refresh of frames


# We get sizes in bytes
# so we need to convert it into a string for the user
def size_format(value):
    units = 1
    while value > 1000:
        value /= 1000
        units += 1
    value = str(int(value))
    if units == 1: return f"{value} bytes"
    elif units == 2: return f"{value} kilobytes"
    elif units == 3: return f"{value} megabytes"
    elif units == 4: return f"{value} gigabytes"
    elif units == 5: return f"{value} tetrabytes"