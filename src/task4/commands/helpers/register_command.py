from collections.abc import Callable
from functools import wraps

commands: list[Callable[[dict[str, str], list[str]], str]] = []

def register_command(aliases: list[str]):
    """
    Registers command for usage by bot's client.

    Copies function's `__doc__` and adds `aliases` field for
    to represent all possible command names.

    :param aliases: names for this command in bot's interface
    :return: wrapped function with command metadata
    """

    def wrapper(fn):
        @wraps(fn)
        def wrapped_f(*args, **kwargs):
            return fn(*args, **kwargs)

        wrapped_f.aliases = set(aliases)
        wrapped_f.__doc__ = wrapped_f.__doc__.strip()

        commands.append(wrapped_f)

        return wrapped_f

    return wrapper
