# simple-command-system

This will be your very own terminal for runnin your silly litle python projects!
You can add commands in the form of .py files and run those in the **terminal** rahh

# how to use?

You will simply clone this repo, then you will be able to create your own commands to use with this framework.

# docs

Each command must have a main function and a help function. Here's some examples

```python
def main(data):
    print("hello")

def help():
    return "short desc","long description"
```

pretty simple right?
the data thats being passed here is just this right here:
```python
class data:
    Command = command #the command text
    Args = args #parsed arguments
```