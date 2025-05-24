from main import register_command

def main(data):
    if len(data.Args) == 0:
        pass
    elif len(data.Args) == 1:
        print(data.Args[0])
    else:
        print("Error 2 - too many args. Expected: 1(string, optional)")

def help(data):
    return "prints to terminal","Prints text to terminal. Use quotes to send multiple words."

def init(data):
    register_command("echo",main,help,["say"])