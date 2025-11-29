import pytest
from tower_builder import build

@pytest.mark.parametrize(
    "number_of_floors, tower",
    [
        (1, ["*"]),
        (2, [" * ", "***"]),
        (3, ["  *  ", " *** ", "*****"])
        ]
    )
def test_to_camel(number_of_floors, tower):
    assert build(number_of_floors) == tower
