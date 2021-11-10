from src.config.settings import DEBUG_MESSAGES
import src.utils.termcolor as termcolor

def debug_message(message: str, print_message: bool=DEBUG_MESSAGES) -> None:
    if print_message : print(">>> " + message)

def log(message: str):
    debug_message("[ LOG ] " + message)

def error(message: str):
    debug_message(termcolor.red("[ERROR] ") + message)

def success(message: str):
    debug_message(termcolor.green("[SUCCESS] ") + message)

def debug(message: str):
    debug_message(termcolor.blue("[DEBUG] ") + message)