import time
def main(data):
    if len(data.Args) == 2:
        try:
            time.sleep(float(data.Args[1]))
        except ValueError:
            print("Error 2 - args wrong type. Expected: 1(number, mandatory)")
    else:
        if len(data.Args) < 2:
            print("Error 2 - missing or incomplete args. Expected: 1(number, mandatory)")
        elif len(data.Args) > 2:
            print("Error 2 - too many args. Expected: 1(number, mandatory)")

def help():
    return "wait in seconds","Stops the current command execution for the specified number of time in seconds."