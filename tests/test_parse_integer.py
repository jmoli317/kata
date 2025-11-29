import pytest
from parse_integer import parse_int


@pytest.mark.parametrize(
    "string_integer, parsed_integer",
    [
        ("zero", 0),
        ("one hundred and twenty-five", 125),
        ("three thousand one hundred sixteen", 3116),
        (
                "four million seven hundred thirty-nine thousand two hundred "
                "thirteen",
                4_739_213
            ),
        ("eight million and six hundred and three", 8_000_603),
        ]
    )
def test_parse_int(string_integer, parsed_integer):
    assert parse_int(string_integer) == parsed_integer
