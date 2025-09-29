

from src.processing import filter_by_state, sort_by_date


def test_empty_input_list() -> None:
    result = filter_by_state([])
    assert result == []


def test_filter_empty_result() -> None:
    transactions = [
        {'id': 1, 'state': 'PENDING'},
        {'id': 2, 'state': 'CANCELED'},
    ]
    result = filter_by_state(transactions, 'EXECUTED')
    assert result == []


def test_filter_executed_from_mixed(mixed_transactions: list[dict]) -> None:
    result = filter_by_state(mixed_transactions, 'EXECUTED')
    assert len(result) == 2
    assert all(t['state'] == 'EXECUTED' for t in result)
    assert [t['id'] for t in result] == [1, 3]


def test_sort_by_date(mixed_date: list[dict]) -> None:
    result = sort_by_date(mixed_date)
    assert result[-1].get("date") == '16.01.2025'
