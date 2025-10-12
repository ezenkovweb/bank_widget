import pytest

from src.widget import get_date, mask_account_card


def test_get_date() -> None:
    with pytest.raises(TypeError):
        get_date(123)


def test_get_date_success():
    """Тест успешного преобразования"""
    assert get_date("2023-12-25") == "25.12.2023"
    assert get_date("1999-01-05") == "05.01.1999"


def test_get_date_invalid_format():
    """Тест неверного формата"""
    with pytest.raises(ValueError):
        get_date("2023/12/25")  # Неправильные разделители

    with pytest.raises(ValueError):
        get_date("2023-12-25-extra")  # Лишние символы


def test_get_date_short_string():
    """Тест слишком короткой строки"""
    with pytest.raises(ValueError):
        get_date("2023-12")  # Не хватает дня


def test_get_date_invalid_chars():
    """Тест нечисловых символов"""
    with pytest.raises(ValueError):
        get_date("abcd-ef-gh")  # Буквы вместо цифр


def test_get_date_invalid_date():
    """Тест некорректных значений даты"""
    with pytest.raises(ValueError):
        get_date("2023-13-01")  # Несуществующий месяц

    with pytest.raises(ValueError):
        get_date("2023-12-32")  # Несуществующий день


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("visa 7365410843013587", "visa 7365 41** **** 3587")
    ]
)
def test_mask_account_card(number: str, expected: str) -> None:
    assert mask_account_card(number) == expected
