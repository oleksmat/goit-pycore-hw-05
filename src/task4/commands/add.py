from .helpers.check_phone import check_phone
from .helpers.register_command import register_command
from .helpers.input_error import input_error

@register_command(aliases=['add'])
@input_error
def add_command(state: dict[str, str], username, phone) -> str:
    """
    add <name> <number>:

    Adds a contact to the contacts book.

    Parameters:
        - username (str) - identifier for the user
        - phone (str) - user's phone number
    """

    if username in state:
        return f"Contact for '{username}' already exists"

    if not check_phone(phone):
        return f"Invalid phone number"

    state[username] = phone

    return f"Contact for '{username}' is now {phone}"
