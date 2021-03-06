import src.config.argument_parser as args
import src.config.settings as settings
import src.utils.debug as debug
import os
import src.code.scribe_architecture as scribe

def main():
    print("Hello World")

    args.init_settings()

    debug.log(f"\n\tTest PATH: {settings.PATH_TO_DIRECTORY}\n\tTest DOCS PATH : {settings.PATH_TO_DOCS}")

    debug.debug(f"Content of PATH_TO_DIRECTORY : {str(os.listdir(settings.PATH_TO_DIRECTORY))}")

    if scribe.validate_scribe_architecture():
        debug.success("Directory architecture is valid. Scribe will begin...")
    else:
        debug.error("The directory architecture is not valid, exiting now...")
        exit(0)

if __name__ == "__main__":
    main()