"""
test_another_module.py

Pytest tests expecting the "sum of quantities" behavior from another_module.py.
These tests PASSED before the bad change was introduced.
Now they FAIL, revealing the incorrect logic.
"""

import pytest
from src.another_module import aggregate_orders

def test_aggregate_orders_basic():
    # Sample data
    orders = [
        {"item": "apple", "quantity": 2},
        {"item": "banana", "quantity": 3},
        {"item": "apple", "quantity": 5}
    ]

    # We expect "apple" => 2 + 5 = 7, "banana" => 3
    result = aggregate_orders(orders)

    assert "apple" in result, "Expected 'apple' key in the result dictionary."
    assert "banana" in result, "Expected 'banana' key in the result dictionary."

    assert result["apple"] == 7, f"Expected aggregated apple quantity to be 7, got {result['apple']}"
    assert result["banana"] == 3, f"Expected aggregated banana quantity to be 3, got {result['banana']}"


def test_aggregate_orders_empty():
    # Empty list case
    orders = []
    result = aggregate_orders(orders)
    assert result == {}, f"Expected empty dict for empty input, got {result}"