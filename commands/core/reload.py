import utils.command_utils as utils
from main import register_command,command_registry
def main(data):
    global command_registry


    runCommand = utils.runCommand

    command_registry.clear()

    class payload:
        RegisterFunc = register_command

    for _, path in utils.getAllCommands().items():
        runCommand(path, "init", payload)

    print("Registry reloaded.")

def help(data):
    return "reload the registry", "Reload the whole command registry. This will update the code."

def init(data):
    register_command("reload", main, help)