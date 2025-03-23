from .helpers.register_command import register_command, commands
from .helpers.input_error import input_error

prelude = """
    This is a contact management bot. Available commands (aliases are in parentheses):
""".strip()

@register_command(aliases=['help'])
@input_error
def help_command(_: any):
    """
    help:

    Prints a list of available commands.
    """

    return prelude + '\n' + ('\n'.join([f" -- {command.__doc__}" for command in commands]))
