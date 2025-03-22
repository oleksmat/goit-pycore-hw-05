def view_command(state: dict[str, str], username):
    if not (username in state):
        return f"Contact for '{username}' does not exist"

    return f"Contact for '{username}' is {state[username]}"

view = (
    ['view', 'phone'],
    1,
    ' -- phone <username>\n' +
    '    View phone contact of <username>.',
    view_command
)
