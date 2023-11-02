"""Testing list and dict methods of tables"""
from ..tables import Table

def test_inheritance() -> None:
    """The actual tests.

    Returns:
        Optional[bool]: True or None if the test passes, False or errors if it fails.
    """
    assert Table(1,3,2).sort() == Table(1,2,3), "Inheritance test 1 failed!"
    assert bool(Table(1,2,3)), "Inheritance test 2 failed!"
    assert not bool(Table()), "Inheritance test 3 failed!"
    assert Table(1,2,3).list == [1,2,3], "Inheritance test 4 failed!"
    assert Table(1,2,3).dict == {}, "Inheritance test 5 failed!"
    x = Table(1,2,3)
    assert x.pop(1) == 2, "Inheritance test 6 failed!"
    assert x == Table(1,3), "Inheritance test 7 failed!"
