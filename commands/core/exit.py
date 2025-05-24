import sys
from main import register_command

def main(data):
    if len(data.Args)==0:
        sys.exit(0)
    elif len(data.Args)==1:
        sys.exit(int(data.Args[0]))
    else:
        print("Error 2 - too many args. Expected: 1(number, optional)")

def help(data):
    return "stop program","Exits program. You may specify status code."

def init(data):
    register_command("exit",main,help)