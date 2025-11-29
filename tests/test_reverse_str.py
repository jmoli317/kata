import pytest
import reverse_str


@pytest.mark.parametrize(
    "string, reversed_string",
    [
        ("hello", "olleh"),
        ("a", "a"),
        ("raise the roof", "foor eht esiar"),
        ("period.", ".doirep"),
        (".!", "!."),
        ("123", "321"),
        ("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba")
    ]
)
def test_reverse(string, reversed_string):
    """Verify the reverse function reverses the entered string."""

    result = reverse_str.reverse(string)

    assert result == reversed_string
