import os
import src.config.settings as settings
import src.utils.debug as debug

def is_markdown(path: str) -> bool:
    """
        Check if a file has the markdown extension.
    """
    return path.lower().endswith((".md", ".markdown"))

def is_valid_path(path: str) -> bool:
    """
        Check if a path is valid.
    """
    return os.path.exists(path)

def validate_scribe_architecture() -> bool:
    """
        Check for existence/validity of every files scribe requires.
    """

    # Import variables
    main, doc = settings.PATH_TO_DIRECTORY + "/" + settings.MAIN_NAME, settings.PATH_TO_DOCS

    debug.debug(f"main path : {main} | doc path : {doc}")

    # Check if variables path exists
    if not is_valid_path(main) or not is_valid_path(doc):
        return False

    # Check if tha main file is a markdown
    if not is_markdown(main):
        debug.error(f"{main} is not a markdown")
        return False

    return True