def bytes_to_string(size):
    unit_number = 0

    while size > 1024:
        size /= 1024
        unit_number += 1
    
    unit_strings = ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes"]
    
    if unit_number < len(unit_strings):
        unit = unit_strings[unit_number]
    else:
        unit = "ERRORR"
    
    size_rounded = round(size, 1)
    size_string = f"{size_rounded} {unit}"

    return size_string