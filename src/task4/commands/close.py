from .helpers.exit_signal_error import ExitSignalError
from .helpers.register_command import register_command
from .helpers.input_error import input_error

@register_command(aliases=['close', 'exit'])
@input_error
def close_command(_: any):
    """
    close(exit):

    Closes the program.
    """
    raise ExitSignalError()
