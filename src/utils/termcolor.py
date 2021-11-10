def red(message: str) -> str:
    return colored_message(message, "\033[91m")

def green(message: str) -> str:
    return colored_message(message, "\033[92m")

def blue(message: str) -> str:
    return colored_message(message, "\033[96m")

def colored_message(message: str, color: str, end: str="\033[00m") -> str:
    return f"{color}{message}{end}"