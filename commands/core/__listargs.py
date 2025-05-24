from main import register_command

def main(data):
    print(data.Args)

def help(data):
    return "testing command","Testing command - prints the args passed to the command"

def init(data):
    register_command("__listargs",main,help)