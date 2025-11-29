def expanded_form(num: int):
    """
    Create a string representing the expanded form of an integer.

    :param num:
    :return:
    """
    digits = [digit for digit in str(num)]
    place_values = []
    for i, digit in enumerate(digits):
        if int(digits[i]) != 0:
            place_values.append(f"{digits[i]}{'0' * len(digits[i + 1:])}")
    return " + ".join(place_values)
