def sort(metadata: list, data_type: str, reversed: bool = False):
    
    def sort_key(data):
        return data[data_type]
    metadata.sort(key=sort_key, reverse=reversed)
    return metadata