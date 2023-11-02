from ..main import Table
if __name__ == "__main__" and not __debug__: # definitions
    print("Table definitions:")
    #print(f"{Table() = }")
    print(f"{repr(Table()) = }")
    print(f"{str(Table()) = }")
    #print(f"{Table(1, 2, 3) = }")
    print(f"{repr(Table(1, 2, 3)) = }")
    print(f"{str(Table(1, 2, 3)) = }")
    #print(f"{Table(foo='bar', spam='eggs') = }")
    print(f"{repr(Table(foo='bar', spam='eggs')) = }")
    print(f"{str(Table(foo='bar', spam='eggs')) = }")
    #print(f"{Table(1, 2, 3, foo='bar', spam='eggs') = }")
    print(f"{repr(Table(1, 2, 3, foo='bar', spam='eggs')) = }")
    print(f"{str(Table(1, 2, 3, foo='bar', spam='eggs')) = }")
    print(f"{len(Table()) = }") # 0
    print(f"{len(Table(1, 2, 3)) = }") # 3
    print(f"{len(Table(foo='bar', spam='eggs')) = }") # 2
    print(f"{len(Table(1, 2, 3, foo='bar', spam='eggs')) = }") # 5
    print(f"{Table(1,2,3).list = }") # [1,2,3]
    print(f"{Table(1,2,3).dict = }") # {}
    print(f"{Table(foo='bar', spam='eggs').list = }") # []
    print(f"{Table(foo='bar', spam='eggs').dict = }") # {'foo': 'bar', 'spam': 'eggs'}
    print(f"{Table(1,2,3, foo='bar', spam='eggs').foreach((lambda _, y: y ), True, False) = }") # [1,2,3]
    exit(0)

def test_tables():
    assert True, "Test 0 failed!"
    assert repr(Table()) == "Table()", "Test 1 failed!"
    assert repr(Table(1, 2, 3)) == "Table([1, 2, 3])", "Test 2 failed!"
    assert repr(Table(foo="bar", spam="eggs")) == "Table({'foo': 'bar', 'spam': 'eggs'})", "Test 3 failed!"
    x = Table(1,2,3, foo="bar", spam="eggs")
    assert repr(x) == "Table([1, 2, 3]; {'foo': 'bar', 'spam': 'eggs'})", "Test 4 failed!"
    assert x.list == [1,2,3], "Test 5 failed!"
    assert x.dict == {"foo":"bar", "spam":"eggs"}, "Test 6 failed!"
    assert x == Table(1,2,3, foo="bar", spam="eggs"), "Test 7 failed!"
    assert x + Table(4,5,6) == Table(1,2,3,4,5,6, foo="bar", spam="eggs"), "Test 8 failed!"
    assert x.foreach(lambda k, v: [k, v]) == [0, 1, 1, 2, 2, 3, "foo", "bar", "spam", "eggs"], "Test 9 failed!"
    assert Table(1,3,2).sort() == Table(1,2,3), "Test 10 failed!"
    #congrats, the code works!
    print("All tests passed!")