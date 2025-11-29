def hide_card_number(card_num: str):
    """
    Replace all but the last four characters in the card number with #.

    Raise TypeError if the card number is not a string.
    Raise ValueError if the card number is not a number or contains
    fewer than four characters.

    Example:
    1111_2222_3333_4444 -> ############4444

    :param card_num: A string representing a credit card number.
    :return: A string representing the hidden credit card number.
    """

    if not isinstance(card_num, str):
        raise TypeError("Invalid input: the card number must be a string.")
    elif not card_num.isdigit():
        raise ValueError(
            "Invalid input: the card number must be a series of digits."
            )
    elif len(card_num) < 4:
        raise ValueError(
            "Invalid input: the card number must be at least 4 digits long."
            )
    return "#" * len(card_num[:-4]) + card_num[-4:]
