import pytest
from likes import likes_msg


@pytest.mark.parametrize(
    "names, msg",
    [
        ([], "no one likes this"),
        (["Jeff"], "Jeff likes this"),
        (["Alex", "Brian"], "Alex and Brian like this"),
        (
                ["Daphne", "Hannah", "Macey"],
                "Daphne, Hannah and Macey like this"
        ),
        (
                ["Jeff", "Brian", "Hannah", "George"],
                "Jeff, Brian and 2 others like this"
        ),
        (
                ["Jeff", "Alex", "Brian", "Daphne", "Hannah", "Macey"],
                "Jeff, Alex and 4 others like this"
        )
    ]
)
def test_likes_msg(names, msg):
    assert likes_msg(names) == msg
