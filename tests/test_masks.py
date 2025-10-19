import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number: int) -> None:
    assert isinstance(card_number, int)
    assert get_mask_card_number(card_number) == "1111 11** **** 1111"


@pytest.mark.parametrize("inv_card, expected", [("123a", "Номер карты должен содержать только цифры")])
def test_not_valid_data(inv_card: str, expected: str) -> None:
    with pytest.raises(ValueError, match=expected):
        get_mask_card_number(inv_card)
        assert get_mask_card_number(inv_card) == expected


@pytest.mark.parametrize("account_number, expected_mask", [
    ("1234567890", "**7890"),
    (1234567890, "**7890"),
])
def test_valid_account_numbers(account_number: str | int, expected_mask: str) -> None:
    """Тестирование валидных номеров счетов различных форматов и длин."""
    result = get_mask_account(account_number)
    assert result == expected_mask
