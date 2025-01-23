"""
another_module.py

A function that is SUPPOSED to aggregate orders by summing quantities
for each item. However, someone made a bad change that breaks the
original (correct) logic.
"""

def aggregate_orders(orders):
    """
    Given a list of orders, each containing an 'item' and 'quantity', 
    this function should return a dictionary mapping each item to its 
    total aggregated quantity.

    For example:
    orders = [
        {"item": "apple", "quantity": 2},
        {"item": "banana", "quantity": 3},
        {"item": "apple", "quantity": 5}
    ]
    We EXPECT:
    {
        "apple": 7,
        "banana": 3
    }

    BUT there's a bad change below that breaks the logic!
    """

    result = {}


    for order in orders:
        item = order["item"]
        quantity = order["quantity"]
        
        # Bad line:
        result[item] += quantity

    return result