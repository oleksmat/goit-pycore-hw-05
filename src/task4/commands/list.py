def list_command(state: dict[str, str]):
    if len(state) == 0:
        return "No contacts yet"

    return '\n'.join([f" -- '{username}' - {state[username]}" for username in state.keys()])

list = (
    ['list', 'all'],
    0,
    ' -- all\n' +
    '    View all phone contacts',
    list_command
)
