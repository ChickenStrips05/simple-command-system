import json, importlib.util, sys
from pathlib import Path
from utils import parser
sys.dont_write_bytecode = True #this way it wont create a compiled module

with open("settings.json", "r") as f:
    settings = json.load(f)

def getAllCommands():
    return {file.stem: str(file) for file in Path("commands/").rglob("*.py") if file.is_file()}

def runCommand(path, data):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, "main"):
        mod.main(data)
    else:
        print(f"No main() in {path}")

def rep():
    command = input(">>> ")

    if not command.startswith(settings["prefix"]): return

    text = command
    commands = getAllCommands()

    for commandText in text.split("|"):
        args = parser.parse_args(commandText)

        name = args[0][len(settings["prefix"]):]
        path = commands.get(name)
        
        if path:
            class data:
                Command = command
                Args = args
            
            try:
                runCommand(path, data)
                
            except KeyboardInterrupt:
                print("force-exiting command")
                return
                    
        else:
            print("Unknown command.")

while True:
    try:
        rep()
    except KeyboardInterrupt:
        print("\nClosing")
        sys.exit()
    except Exception as e:
        print("Error:",e)


"""
Command errors:
    Error 1 - internal code error,
    something like an exception or a malfunction

    Error 2 - argument error,
    not enough, too many, or wrong types. 
"""