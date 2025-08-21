from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(account_card: str) -> str:
    """
    Обрабатывает информацию как о картах и счетах
    """
    parts = account_card.split()  # делим введённые данные по пробелам, получаем список

    if "Счет" in account_card:
        return f"Счет {get_mask_account(parts[-1])}"  # выводим маскированный номер счёта
    else:
        # Это карта - собираем всё кроме последней части (номера) как название
        card_name = ' '.join(parts[:-1])  # имя карты
        card_number = parts[-1]  # номер карты
        masked_number = get_mask_card_number(card_number)  # маскируем номер карты
        return f"{card_name} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату в формат 'ДД.ММ.ГГГГ'
    используя срезы строк
    """
    # Извлекаем части даты
    year = date_string[0:4]  # Год - первые 4 символа
    month = date_string[5:7]  # Месяц - символы 5-6
    day = date_string[8:10]  # День - символы 8-9

    # Выводим результат
    return f"{day}.{month}.{year}"
