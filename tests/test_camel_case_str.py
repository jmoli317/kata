import pytest
from camel_case_str import to_camel_case

@pytest.mark.parametrize(
    "string, camel_case_string",
    [
        ("camel-case-string", "camelCaseString"),
        ("camel_case_string", "camelCaseString"),
        ("Camel_Case_String", "CamelCaseString"),
        ]
    )
def test_to_camel_case(string, camel_case_string):
    assert to_camel_case(string) == camel_case_string
