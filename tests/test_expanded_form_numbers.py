import pytest
from expanded_form_numbers import expanded_form


@pytest.mark.parametrize(
    "num, expanded_form_num",
    [
        (3, "3"),
        (25, "20 + 5"),
        (168, "100 + 60 + 8"),
        (530_287, "500000 + 30000 + 200 + 80 + 7"),
        (
                944_552_309,
                "900000000 + 40000000 + 4000000 + 500000 + 50000 + 2000 "
                "+ 300 + 9"
            )
        ]
    )
def test_expanded_form_with_valid_integers(num, expanded_form_num):
    assert expanded_form(num) == expanded_form_num
