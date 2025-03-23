from .helpers.register_command import register_command
from .helpers.input_error import input_error

@register_command(aliases=['greet', 'hello'])
@input_error
def greet_command(_: any):
    """
    hello(greet):

    Prints hello statement.
    """
    return 'How can I help you?'
