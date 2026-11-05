import argparse


# '-> None' main returns nothing. --strict only requires that a label exists
def main() -> None:

    # creates obj in mem, stores rules, holds methods | prog="stock-watcher" help w error msgs
    parser = argparse.ArgumentParser(prog="stock-watcher")

    # group that holds commands
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("hello")  # creates a command called hello

    # it reads the command line and stores the result in args
    args = parser.parse_args()
    if args.command == "hello":
        print("hello")
