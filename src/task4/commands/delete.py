def delete_command(state: dict[str, str], username):
    if not (username in state):
        return f"Contact for '{username}' does not exist"

    del state[username]

    return f"Contact for '{username}' was deleted"

delete = (
    ['delete'],
    1,
    ' -- delete <username>\n' +
    '    Delete phone contact of <username>.',
    delete_command
)
