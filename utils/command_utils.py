import importlib.util, sys
from pathlib import Path
sys.dont_write_bytecode = True

def runCommand(path, func:str, payload:classmethod=None):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, func):
        return getattr(mod,func)(payload)
    else:
        print(f"No {func}() in {path}")

def getAllCommands():
    return {file.stem: str(file) for file in Path("commands/").rglob("*.py") if file.is_file()}

def searchCommand(registry: list, query: str, field: str = "name"):
    if field == "name":
        return next((entry for entry in registry if entry["name"] == query or query in entry.get("aliases", [])),None)
    else:
        return next((entry for entry in registry if entry.get(field) == query),None)
    
def parse_args(text):
    args = []
    charurrent = ""
    in_quotes = False
    escharape = False

    for char in text:
        if escharape:
            charurrent += char
            escharape = False
        elif char == "\\":
            escharape = True
        elif char == '"':
            in_quotes = not in_quotes
        elif char == " " and not in_quotes:
            if charurrent:
                args.append(charurrent)
                charurrent = ""
        else:
            charurrent += char

    if charurrent:
        args.append(charurrent)

    return args