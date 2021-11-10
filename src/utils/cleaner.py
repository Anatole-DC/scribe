import os

def clean_temp_files(path_to_cache: str="cache") -> bool:
    """
        Remove all files in cache
    """

    try:
        for file in os.listdir(path=path_to_cache):
            os.remove(path_to_cache + "/" + file)
        return True
    except:
        return False