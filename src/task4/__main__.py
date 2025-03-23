# import list of commands from commands package
from .commands.helpers.exit_signal_error import ExitSignalError
from .commands.helpers.register_command import commands

def get_aliases(command_func: any):
    if hasattr(command_func, 'aliases'):
        return command_func.aliases
    return {command_func.__name__}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    # storing contact information in here
    state = ({})

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command_name, *args = parse_input(user_input)

        # match a command by name
        command = next((
            command
            for command
            in commands
            if command_name in get_aliases(command)
        ), None)

        # if no commands match, we print error message
        if command is None:
            print("Invalid command. Check `help` to list all commands")
            continue

        # get command parameters for checking arity
        command_function = command

        try:
            # execute command with supplied arguments
            result = command_function(state, *args)

            print(result)
        except ExitSignalError:
            print('Goodbye')
            break

if __name__ == "__main__":
    main()
