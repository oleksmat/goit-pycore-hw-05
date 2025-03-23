from .helpers.register_command import register_command, commands
from .helpers.input_error import input_error

@register_command(aliases=['help'])
@input_error
def help_command(_: any):
    """
    help:

    Prints a list of available commands.
    """
    return '\n'.join([f" -- {command.__doc__}" for command in commands])
