def find_even_index(arr: list[int]):
    """
    Finds an index in an array of integers where the sum of values on
    the left equals the sum of values on the right.

    Returns the index or -1 if there is no valid split.
    """
    for i in range(0, len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1
