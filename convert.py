def bytes_to_string(size: int, short_string: bool = False):
    unit_number = 0

    while size > 1024:
        size /= 1024
        unit_number += 1
    
    unit_strings = ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes"]
    unit_strings_short = ["B", "KB", "MB", "GB", "TB", "PB"]
    
    if unit_number < len(unit_strings):
        if short_string:
            unit = unit_strings_short[unit_number]
        else:
            unit = unit_strings[unit_number]
    else:
        unit = "ERROR"
    
    size_rounded = round(size, 1)
    size_string = f"{size_rounded} {unit}"

    return size_string