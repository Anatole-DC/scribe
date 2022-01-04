from typing import Dict, List
import src.config.settings as settings
import src.utils.debug as debug
import os

def fetch_subdirectories(path: str = settings.PATH_TO_DOCS, indent: int = 0) -> Dict:
    """Loop through directories to translate the folder architecture into a dictionnay.

    Args:
        path (str, optional): The path to the the doc folder. Defaults to settings.PATH_TO_DOCS.
        indent (int, optional): Indentation for architecture display. Defaults to 0.

    Returns:
        Dict: The architecture into dictionnary.
    """

    subdirectories = {}

    indentation = "\t" * indent

    for dir in os.listdir(path):
        print(f"{indentation}{dir}")
        if os.path.isdir(path + "/" + dir):
            subdirectories[dir] = fetch_subdirectories(path + "/" + dir, indent=indent+1)
        else:
            if "files" not in subdirectories.keys():
                subdirectories["files"] = [dir]
            else: subdirectories["files"].append(dir)

    return subdirectories

def fetch_markdowns() -> List[str]:
    """
        Fetch markdowns in subdirectories.
    """
    pass

def fetch_doc_elements() -> Dict:
    """
        Fetch all the elements in the doc directory.
    """
    pass