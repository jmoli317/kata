import pytest
from digital_root import find_digital_root


@pytest.mark.parametrize(
    "number, digital_root",
    [
        (123, 6),
        (1004, 5),
        (1433, 2),
        (10045987, 7),
        (1, 1),
        (0, 0),
        ]
    )
def test_find_digital_root(number, digital_root):
    assert find_digital_root(number) == digital_root
