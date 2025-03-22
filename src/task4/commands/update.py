from re import match

def update_command(state: dict[str, str], username, phone):
    if not (username in state):
        return f"Contact for '{username}' does not exists"

    if match('^\d{10}$', string=phone) is None:
        return f"Invalid phone number"

    state[username] = phone

    return f"Changed contact for '{username}' to {phone}"

update = (
    ['change', 'update'],
    2,
    ' -- change <name> <number>\n' +
    '    Change a contact in the contacts book.',
    update_command
)
