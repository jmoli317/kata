import pytest
from find_equal_sums_in_array import find_even_index


@pytest.mark.parametrize(
    "array, expected_index",
    [
        ([1, 2, 3, 4, 3, 2, 1], 3),
        ([1, 1, 6, 2], 2),
        ([30, 10, -50, 3, 6, -25, -10, 28], 4),
        ([1, 0, 1], 1),
        ([20, 10, -80, 10, 10, 15, 35], 0),
        ([1, 2, 3, 4], -1),
    ]
)
def test_find_even_index(array, expected_index):
    """
    Verify that the function returns the index which divides the array
    so that the sum of values to the left of the index (array[:index])
    equals the sum of values to the right (array[index:]). Returns -1 if
    no such index exists.

    Note: The sum of an empty list is treated as 0, following Python’s
    convention. So, if a list is split at index 0, the left side is []
    and the right side is the entire array.

    For example, with input [20, -20], index 0 is considered a valid
    split because sum([]) == sum([20, -20]) == 0.
    """

    assert find_even_index(array) == expected_index
