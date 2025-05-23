import importlib.util;from pathlib import Path

def getAllCommands():
    return {file.stem: str(file) for file in Path("commands/").rglob("*.py") if file.is_file()}

def get_info(path):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, "help"):
        return mod.help()
    else:
        print(f"No help() in {path}")


def main(data):
    commands = getAllCommands()
    if len(data.Args)==1:
        print("Available commands:\n")
        for command in commands:
            print(command," — ",get_info(commands[command])[0])

    elif len(data.Args)==2:
        if data.Args[1] in commands:
            print(f"{data.Args[1]} command:\n{get_info(commands[data.Args[1]])[1]}")
    else:
        print("Error 2 - too many args. Expected: 1(string, optional)")
def help():
    return "core help command", "This command provides useful information about other commands!"