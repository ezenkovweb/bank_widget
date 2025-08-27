def filter_by_state(transactions: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    filtered_transactions = []
    for transaction in transactions:
        if transaction.get('state') == state:
            filtered_transactions.append(transaction)


    return filtered_transactions


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате (ключ 'date').
    """
    # Создаем копию списка чтобы не изменять оригинал
    sorted_transactions = transactions.copy()

    # Сортируем список по ключу 'date'
    # lambda функция извлекает значение даты для сортировки
    sorted_transactions.sort(key=lambda x: x['date'], reverse=reverse)

    # Возвращаем отсортированный список
    return sorted_transactions
