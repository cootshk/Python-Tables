from ..main import Table

if __name__ == "__main__": # definitions
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
    print(f"{Table(1,2,3, foo='bar', spam='eggs').foreach((lambda _, y: y ), True, False) = }")
