def close_command(_: any):
    return 'Goodbye', True

close = (
    ['close', 'exit'],
    0,
    ' -- close\n' +
    '    Closes the program',
    close_command
)
