"""Testing table operands, like +, ==, etc."""
from ..tables import Table


def test_operands() -> None:
    """The actual tests."""
    assert Table() + Table() == Table(), "Operands test 1 failed!"
    assert Table(1, 2, 3) + Table(4, 5, 6) == Table(1, 2,
                                                    3, 4, 5, 6), "Operands test 2 failed!"
    assert Table(1, 2, 3) != Table(
        1, 2, 3, foo="bar"), "Operands test 3 failed!"
    assert Table(1, 2, 3) == Table(1, 2, 3), "Operands test 4 failed!"
    assert Table(1, 2, 3) != Table(1, 2, 4), "Operands test 5 failed!"
    assert Table(foo="bar") == Table(foo="bar"), "Operands test 6 failed!"
    assert Table(foo="bar") != Table(foo="baz"), "Operands test 7 failed!"
    assert Table(1, 2, 3) + Table(foo="bar") == Table(1, 2,
                                                      3, foo="bar"), "Operands test 8 failed!"
    x = Table()
    x.append(2)
    x["foo"] = "bar"
    assert x == Table(2, foo="bar"), "Operands test 9 failed!"
    assert id(x) != id(Table(2, foo="bar")), "Operands test 10 failed!"
