import pytest


@pytest.fixture
def card_number() -> int:
    return 1111111111111111


@pytest.fixture
def mixed_transactions() -> list[dict]:
    transactions = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
        {'id': 3, 'state': 'EXECUTED'},
        {'id': 4, 'state': 'CANCELED'},
    ]
    return transactions


@pytest.fixture
def mixed_date() -> list[dict]:
    transactions = [
        {'id': 1, 'date': '16.01.2025'},
        {'id': 2, 'date': '16.02.2025'},
        {'id': 3, 'date': '16.11.2025'},
        {'id': 4, 'date': '16.07.2025'},
    ]
    return transactions
