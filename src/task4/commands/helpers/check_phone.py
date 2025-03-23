from re import match

def check_phone(phone_str):
    return match('^(\d{10}|\+\d{12})$', string=phone_str) is not None
