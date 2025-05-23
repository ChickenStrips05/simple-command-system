import sys
def main(data):
    if len(data.Args)==1:
        sys.exit(0)
    elif len(data.Args)==2:
        sys.exit(int(data.Args[1]))
    else:
        print("Error 2 - too many args. Expected: 1(number, optional)")

def help():
    return "stop program","Exits program. You may specify status code."