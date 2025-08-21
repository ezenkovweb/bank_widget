def get_mask_card_number(card_number: str | int) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    Видны первые 6 и последние 4 цифры, остальные заменены на *.
    """
    # Преобразуем номер карты в строку (на случай, если передан int)
    str_number = str(card_number).strip()

    # Проверяем, что номер карты состоит только из цифр и имеет допустимую длину
    if not str_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    if len(str_number) < 12 or len(str_number) > 19:
        raise ValueError("Номер карты должен содержать от 12 до 19 цифр")

    # Форматируем номер карты
    masked = f"{str_number[:4]} {str_number[4:6]}** **** {str_number[-4:]}"

    return masked


def get_mask_account(account_number: str | int) -> str:
    """
    Маскирует номер счёта (число) в формате **XXXX.
    Показывает только последние 4 цифры, перед ними — две звёздочки.
    """
    # Преобразуем число в строку
    num_str = str(account_number)

    # Проверяем, что в номере минимум 4 цифры
    if len(num_str) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    # Возвращаем последние 4 цифры с **
    return f"**{num_str[-4:]}"
