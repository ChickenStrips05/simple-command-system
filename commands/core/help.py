import utils.command_utils as utils
from main import register_command

def main(data):
    class payload:  # help payload
        pass

    commands = data.Registry  # the current registry

    if len(data.Args) == 0:
        print("Available commands:\n")
        for command in commands:
            aliases = command.get("aliases", [])
            alias_str = f" (aliases: {', '.join(aliases)})" if aliases else ""
            print(f"{command['name']}{alias_str} — {command['help'](payload)[0]}")

    elif len(data.Args) == 1:
        match = utils.searchCommand(commands, data.Args[0])
        if match:
            aliases = match.get("aliases", [])
            alias_str = f"\nAliases: {', '.join(aliases)}" if aliases else ""
            print(f"{match['name']} — {match['help'](payload)[1]}{alias_str}")
        else:
            print("Command not found.")
    else:
        print("Error 2 - too many args. Expected: 1 (string, optional)")

def help(data):
    return "core help command", "This command provides useful information about other commands!"

def init(data):
    register_command("help", main, help)