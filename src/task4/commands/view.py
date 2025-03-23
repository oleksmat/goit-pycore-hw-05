from .helpers.register_command import register_command
from .helpers.input_error import input_error

@register_command(aliases=['view', 'phone'])
@input_error
def view_command(state: dict[str, str], username):
    """
    phone(view) <username>:

    View phone contact of <username>.

    Parameters:
        - username (str) - identifier for the user
    """

    if not (username in state):
        return f"Contact for '{username}' does not exist"

    return f"Contact for '{username}' is {state[username]}"
