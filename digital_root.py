def find_digital_root(num: int):
    """
    Find the digital root of an integer greater than or equal to 10.

    Sum the digits of the provided number. If the sum is greater than or
    equal to 10, then repeat this process until the sum is less than 10.

    :param num: An integer greater than 10.
    :return: An integer less than 10 (the digital root of num).
    """
    
    while num not in range(10):
        num = sum([int(digit) for digit in str(num)])
    return num
