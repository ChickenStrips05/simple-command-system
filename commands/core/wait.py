import time
from main import register_command

def main(data):
    if len(data.Args) == 1:
        try:
            time.sleep(float(data.Args[0]))
        except ValueError:
            print("Error 2 - args wrong type. Expected: 1(number, mandatory)")
    else:
        if len(data.Args) < 1:
            print("Error 2 - missing or incomplete args. Expected: 1(number, mandatory)")
        elif len(data.Args) > 1:
            print("Error 2 - too many args. Expected: 1(number, mandatory)")

def help(data):
    return "wait in seconds","Stops the current command execution for the specified number of time in seconds."

def init(data):
    register_command("wait",main,help)