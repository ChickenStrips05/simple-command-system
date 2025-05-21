import json, os, importlib.util, sys
from pathlib import Path
sys.dont_write_bytecode = True #this way it wont create a compiled module

with open("settings.json", "r") as f:
    settings = json.load(f)

def getAllCommands():
    return {file.stem: str(file) for file in Path("commands/").rglob("*.py") if file.is_file()}

def run_command(path, data):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, "main"):
        mod.main(data)
    else:
        print(f"No main() in {path}")


try:
    while True:
        cmd_input = input(">>> ")
        
        class Command:
            def __init__(self, content):
                self.content = content
                self.channel = "default-channel"

        command = Command(cmd_input)

        if not command.content.startswith(settings["prefix"]): continue

        text = command.content
        channel = command.channel
        commands = getAllCommands()

        for command_text in text.split("|"):
            args = command_text.strip().split()

            name = args[0][len(settings["prefix"]):]
            path = commands.get(name)
            
            if path:
                class data:
                    Command = command
                    Text = text
                    Channel = channel
                    Commands = commands
                    Args = args
                try:
                    run_command(path, data)
                except Exception as e:
                    print("Error:", e)
            else:
                print("Unknown command.")
except KeyboardInterrupt:
    print("\nClosing.")
except Exception as e:
    print("Error:",e)


"""
Command errors:
    Error 1 - internal code error,
    something like an exeption or malfunction

    Error 2 - argument error,
    not enough, too many, or wrong types. 
"""