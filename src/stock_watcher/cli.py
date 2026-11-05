import argparse

def main()->None: # '-> None' because mypy '--strict'
    parser = argparse.ArgumentParser() # creates obj in mem, stores rules, holds methods
    subparsers = parser.add_subparsers(dest="command", required=True) # group that holds commands
    subparsers.add_parser("hello") # creates a command called hello
#    subparsers.add_parser("nope") # to test, now also excepts nope as a command
    parser.parse_args() # reads cmd exp. "stock-watcher hello" holds "hello"
    print("hello")
    