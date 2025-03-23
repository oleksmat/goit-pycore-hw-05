from .helpers.check_phone import check_phone
from .helpers.register_command import register_command
from .helpers.input_error import input_error

@register_command(aliases=['change', 'update'])
@input_error
def update_command(state: dict[str, str], username, phone):
    """
    change(update) <username>:

    Change a <username>'s contact.

    Parameters:
        - username (str) - identifier for the user
    """

    if not (username in state):
        return f"Contact for '{username}' does not exists"

    if not check_phone(phone):
        return f"Invalid phone number"

    state[username] = phone

    return f"Changed contact for '{username}' to {phone}"
