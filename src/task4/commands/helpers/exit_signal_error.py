class ExitSignalError(Exception):
    """
    Error to signal that bot should finish working.

    Used for normal exit (using `close` command for example).
    """

    pass
