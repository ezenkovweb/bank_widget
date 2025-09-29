import pytest

from src.widget import get_date, mask_account_card


def test_get_date() -> None:
    with pytest.raises(TypeError):
        get_date(123)


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("visa 7365410843013587", "visa 7365 41** **** 3587")
    ]
)
def test_mask_account_card(number: str, expected: str) -> None:
    assert mask_account_card(number) == expected
