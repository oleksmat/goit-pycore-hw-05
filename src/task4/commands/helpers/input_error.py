from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError as e:
            message: str = e.args[0]

            args = message.split(': ')[1].split(' and ')

            return f"Missing parameter(s): {', '.join(args)}"

    return inner
