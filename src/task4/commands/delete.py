from .helpers.register_command import register_command
from .helpers.input_error import input_error

@register_command(aliases=['delete'])
@input_error
def delete_command(state: dict[str, str], username):
    """
    delete <username>:

    Delete phone contact of <username>.

    Parameters:
        - username (str) - identifier for the user
    """
    if not (username in state):
        return f"Contact for '{username}' does not exist"

    del state[username]

    return f"Contact for '{username}' was deleted"
