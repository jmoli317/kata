import pytest
from hide_cc_number import hide_card_number


@pytest.mark.parametrize(
    "card_num, hidden_card_num",
    [
        ("00000", "#0000"),
        ("1234", "1234"),
        ("12345", "#2345"),
        ("1111222233334444", "############4444"),
        ]
    )
def test_hide_card_number_with_valid_card_num(card_num, hidden_card_num):
    assert hide_card_number(card_num) == hidden_card_num


@pytest.mark.parametrize(
    "invalid_card_num, error_msg",
    [
        (
                1111_2222_3333_4444,
                "Invalid input: the card number must be a string."
            ),
        (
                1111_2222.33334444,
                "Invalid input: the card number must be a string."
            ),
        (
                True,
                "Invalid input: the card number must be a string."
            ),
        (
                None,
                "Invalid input: the card number must be a string."
            )
        ]
    )
def test_hide_card_number_raises_type_error_with_non_string_arg(
    invalid_card_num, error_msg
    ):
    with pytest.raises(TypeError) as e:
        hide_card_number(invalid_card_num)
    assert str(e.value) == error_msg


@pytest.mark.parametrize(
    "invalid_card_num, error_msg",
    [
        (
                "",
                "Invalid input: the card number must be a series of digits."
            ),
        (
                "aaaabbbbccccdddd",
                "Invalid input: the card number must be a series of digits."
            ),
        (
                "12345678&9",
                "Invalid input: the card number must be a series of digits."
            ),
        (
                "     ",
                "Invalid input: the card number must be a series of digits."
            ),
        (
                "000.4",
                "Invalid input: the card number must be a series of digits."
            ),
        (
                "-1111222233334444",
                "Invalid input: the card number must be a series of digits."
            )
        ]
    )
def test_hide_card_number_raises_value_error_with_non_digits_arg(
    invalid_card_num, error_msg
    ):
    with pytest.raises(ValueError) as e:
        hide_card_number(invalid_card_num)
    assert str(e.value) == error_msg


@pytest.mark.parametrize(
    "invalid_card_num, error_msg",
    [
        (
                "1",
                "Invalid input: the card number must be at least 4 digits "
                "long."
            ),
        (
                "12",
                "Invalid input: the card number must be at least 4 digits "
                "long."
            ),
        (
                "123",
                "Invalid input: the card number must be at least 4 digits "
                "long."
            ),
        ]
    )
def test_hide_card_number_raises_value_error_with_short_card_num(
    invalid_card_num, error_msg
    ):
    with pytest.raises(ValueError) as e:
        hide_card_number(invalid_card_num)
    assert str(e.value) == error_msg
