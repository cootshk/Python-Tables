"""Unit tests for main.py
"""

from ..tables import Table

def test_tables():
    """Unit tests for Table() class
    """
    assert True, "Test 0 failed!"
    assert repr(Table()) == "Table()", "Test 1 failed!"
    assert repr(Table(1, 2, 3)) == "Table([1, 2, 3])", "Test 2 failed!"
    assert repr(
        Table(foo="bar", spam="eggs")
    ) == "Table({'foo': 'bar', 'spam': 'eggs'})", "Test 3 failed!"
    x = Table(1,2,3, foo="bar", spam="eggs")
    assert repr(x) == "Table([1, 2, 3]; {'foo': 'bar', 'spam': 'eggs'})", "Test 4 failed!"
    assert x.list == [1,2,3], "Test 5 failed!"
    assert x.dict == {"foo":"bar", "spam":"eggs"}, "Test 6 failed!"
    assert x[0] == 1, "Test 7 failed!"
    assert x[1] == 2, "Test 8 failed!"
    assert x[2] == 3, "Test 9 failed!"
    assert x["foo"] == "bar", "Test 10 failed!"
    assert x["spam"] == "eggs", "Test 11 failed!"
