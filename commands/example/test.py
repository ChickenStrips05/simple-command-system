from main import register_command

def main(data):
    print("hello!")

def help(data):
    return "testing command","Testing command - returns 'Hello!'"

def init(data):
    register_command("test",main,help)