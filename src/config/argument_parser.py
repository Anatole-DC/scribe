import sys
import src.config.settings as settings
import src.utils.debug as debug



def is_variable_parameter(arg: str, split_symbol: str="=") -> bool:
    return len(arg.split(split_symbol)) > 1



def init_variable_parameter(arg: str, split_symbol: str="=") -> bool:
    argument, value = arg.split(split_symbol)
    if argument == "--detail":
        settings.SUMMARY_DETAILS = value
    elif argument == "--main":
        settings.MAIN_NAME = value
    else:
        debug.error(f"Unknown variable parameter {argument}")
        return False
    
    return True



def is_value(arg: str) -> bool:
    return arg[:2] != "--" or arg[:1] != "-"



def init_value(arg: str, index: int) -> bool:
    if index == 0:
        settings.PATH_TO_DIRECTORY = arg
    elif index == 1:
        settings.PATH_TO_DOCS = arg
    else:
        debug.error(f"To many arguments {index}")
        return False
    return True



def init_parameter(arg: str) -> bool:
    if arg == "--dev" or arg == "-d":
        settings.DEBUG_MESSAGES = True
    else:
        debug.error(f"Unkown parameter {arg}")
        return False

    return True



def init_settings() -> bool:
    """
        Setup the scribe script with the arguments entered when the script was called.
    """

    debug.log(f"Initiating parameters...")

    try:

        arguments = sys.argv

        index: int = 0

        for arg in arguments[1:]:
            if is_variable_parameter(arg):
                init_variable_parameter(arg)

            elif is_value(arg):
                init_value(arg, index)

            else:
                init_parameter(arg)

            index += 1

        debug.log(f"MAIN:{settings.MAIN_NAME}")

        return True
    except:
        return False
