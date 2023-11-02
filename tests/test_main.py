"""Unit tests for main.py
"""

try:
    from ..tables import Table
except:
    try:
        from tables import Table
    except:
        from .tables import Table

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
    assert x == Table(1,2,3, foo="bar", spam="eggs"), "Test 7 failed!"
    assert x + Table(4,5,6) == Table(1,2,3,4,5,6, foo="bar", spam="eggs"), "Test 8 failed!"
    assert x.foreach(
        lambda k, v: [k, v]) == [0, 1, 1, 2, 2, 3, "foo", "bar", "spam", "eggs"
        ], "Test 9 failed!"
    assert Table(1,3,2).sort() == Table(1,2,3), "Test 10 failed!"
    assert bool(Table(1,2,3)), "Test 11 failed!"
    assert not bool(Table()), "Test 12 failed!"
    #congrats, the code works!
    print("All tests passed!")
