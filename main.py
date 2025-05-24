import json, sys
import utils.command_utils as utils

sys.dont_write_bytecode = True #this way it wont create a compiled module

with open("settings.json", "r") as f:
    settings = json.load(f)
debug = settings["debug"]

command_registry = []

def register_command(name, func, help, aliases=None):
    command_registry.append({"name": name,"func": func,"help": help,"aliases": aliases or []})
    
    if debug: print("registered", name, "command.", "Aliases:", aliases or [])

runCommand = utils.runCommand


def init():
    class payload:
        RegisterFunc = register_command
    
    for _, path in utils.getAllCommands().items():
        runCommand(path,"init",payload)

init()


def rep():
    command = input(">>> ")

    if not command.startswith(settings["prefix"]):
        return

    text = command

    for commandText in text.split("|"):
        args = utils.parse_args(commandText)

        name = args[0][len(settings["prefix"]):]

        class payload:
            Command = commandText
            Args = args[1:]
            Registry = command_registry

        match = utils.searchCommand(command_registry,name)

        if match:
            try:
                match["func"](payload)
            except KeyboardInterrupt:
                print("Force-exiting command.")
                return
        else:
            print("Unknown command.")

while True:
    try:
        rep()
    except KeyboardInterrupt:
        print("\nClosing")
        sys.exit()
    #except Exception as e:
    #    print("Error:",e)


"""
Command errors:
    Error 1 - internal code error,
    something like an exception or a malfunction

    Error 2 - argument error,
    not enough, too many, or wrong types. 
"""