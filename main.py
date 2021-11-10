import src.config.argument_parser as args
import src.utils.cleaner as cleaner
import src.config.settings as settings
import src.utils.debug as debug
import os

def main():
    print("Hello World")

    args.init_settings()

    debug.log(f"\n\tTest PATH: {settings.PATH_TO_DIRECTORY}\n\tTest DOCS PATH : {settings.PATH_TO_DOCS}")

    debug.debug(f"Content of PATH_TO_DIRECTORY : {str(os.listdir(settings.PATH_TO_DIRECTORY))}")


if __name__ == "__main__":
    main()