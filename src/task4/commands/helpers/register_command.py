import re
from collections.abc import Callable
from functools import wraps

commands: list[Callable[[dict[str, str], list[str]], str]] = []

def register_command(aliases: list[str]):
    print('called register')

    def wrapper(fn):
        print('called wrapper')

        @wraps(fn)
        def wrapped_f(*args, **kwargs):
            return fn(*args, **kwargs)

        wrapped_f.aliases = set(aliases)
        wrapped_f.__doc__ = re.sub(
            "(?m)^\n[ \t]+:param (state|context):[^\n\r]$", '',
            wrapped_f.__doc__.strip()
        )

        commands.append(wrapped_f)

        return wrapped_f

    return wrapper
