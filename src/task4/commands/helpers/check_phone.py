from re import match

def check_phone(phone_str: str) -> bool:
    """
    Validate that `phone_str` is a phone string.

    Either 10 digits or 12 digits prefixed by `+`.

    :param phone_str: phone string to validate
    :return: true, if `phone_str` is a phone string
    """

    return match('^(\d{10}|\+\d{12})$', string=phone_str) is not None
