import pytest

from src.widget import get_date, mask_account_card


def test_get_date() -> None:
    with pytest.raises(TypeError):
        get_date(123)


def test_get_date_success():
    """Тест успешного преобразования"""
    assert get_date("2023-12-25") == "25.12.2023"
    assert get_date("1999-01-05") == "05.01.1999"


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("visa 7365410843013587", "visa 7365 41** **** 3587")
    ]
)
def test_mask_account_card(number: str, expected: str) -> None:
    assert mask_account_card(number) == expected


def test_get_date_valid_formats():
    """Тестирование функции с валидными форматами дат"""

    # Стандартные случаи
    assert get_date("2023-12-25") == "25.12.2023"
    assert get_date("1999-01-05") == "05.01.1999"
    assert get_date("2024-02-29") == "29.02.2024"  # високосный год

    # Граничные значения месяцев и дней
    assert get_date("2023-01-01") == "01.01.2023"  # первый день года
    assert get_date("2023-12-31") == "31.12.2023"  # последний день года

    # Даты с однозначными числами (с ведущими нулями)
    assert get_date("2023-01-01") == "01.01.2023"
    assert get_date("2023-09-07") == "07.09.2023"

    # Разные годы
    assert get_date("2000-06-15") == "15.06.2000"
    assert get_date("2015-08-20") == "20.08.2015"
    assert get_date("1995-03-10") == "10.03.1995"

    # Все месяцы
    assert get_date("2023-01-15") == "15.01.2023"
    assert get_date("2023-06-15") == "15.06.2023"
    assert get_date("2023-12-15") == "15.12.2023"


def test_get_date_edge_cases():
    """Тестирование граничных случаев с валидными датами"""

    # Минимальная дата (в реальном проекте нужно учитывать ограничения)
    assert get_date("0001-01-01") == "01.01.0001"

    # Максимальная дата (условно)
    assert get_date("9999-12-31") == "31.12.9999"

    # 30 дней в апреле
    assert get_date("2023-04-30") == "30.04.2023"

    # 28 дней в феврале невисокосного года
    assert get_date("2023-02-28") == "28.02.2023"