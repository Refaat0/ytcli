#!/usr/bin/python3 
from src.utilities.args import args
from src.argument_handlers.process_arguments import process_arguments

# the main method
def main(args):
    # loop through all the arguments and only process the one with positional arguments
    for argument, positional_arguments in vars(args).items():
        if positional_arguments is not None:
            process_arguments(argument, positional_arguments)

if __name__ == "__main__":
    main(args())
