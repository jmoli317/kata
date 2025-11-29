def reverse(string: str = None):
    """
    Accept a string and return the same characters reversed.
    EXAMPLE: hello -> olleh
    """

    if string is None:
        string = input("Enter a string: ")
    reverse_str = ""
    for char in string:
        reverse_str = char + reverse_str
    return reverse_str
