def convert_input_in_float(text_message: str) -> float:
    """Asks a question to the user
    and converts the answer into numeric data"""

    user_data = input(f'{text_message} >>> ')

    while not is_float_or_int(user_data):

        user_data = input('Please enter number >>> ')

    processed_data = float(user_data)

    return processed_data


def is_float_or_int(some_string: str) -> bool:
    """checks if a string is numeric data"""

    if (some_string.replace('.', '1').isdigit()
            and some_string.count('.') <= 1):

        return True

    else:

        return False

