from typing import Dict, List
import src.config.settings as settings
import src.utils.debug as debug
import os

def fetch_subdirectories(path: str = settings.PATH_TO_DOCS, indent: int = 0) -> List[str]:
    """
        Fetch subdirectories to generate summary.
    """
    subdirectories = []
    indentation = "\t" * indent
    for dir in os.listdir(path):
        print(f"{indentation}{dir}")
        if os.path.isdir(path + "/" + dir):
            fetch_subdirectories(path + "/" + dir, indent=indent+1)

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