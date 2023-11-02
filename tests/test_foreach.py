"""Testing table.foreach() method. 
    This is a **very dangerous** method, so it is tested separately.
"""
from ..tables import Table


def test_tables() -> None:
    """The actual tests."""
    tbl = Table(1, 2, 3)
    assert isinstance(tbl.foreach(lambda x, y: y),
                      list), "Foreach test 1 failed!"
    assert tbl.foreach(lambda x, y: [x, y, True]) == [
        [0, 1, True],
        [1, 2, True],
        [2, 3, True]
    ], "Foreach test 2 failed!"
