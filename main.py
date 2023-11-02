"""The Table module.

    See the Table class for more info.

    """

# check for python version
from typing import Iterable, override, Any, Optional, overload, Callable
import sys
if sys.version_info < (3, 12):
    print("This script requires Python 3.12+")
    exit(1)
del sys


class Table(Iterable):
    """The Table class. It's a list and a dict combined.

    Examples:
        Table() # Table([])
        Table(1, 2, 3) # Table([1, 2, 3])
        Table(foo="bar", spam="eggs") # Table({'foo': 'bar', 'spam': 'eggs'})
        # Table([1, 2, 3]; {'foo': 'bar', 'spam': 'eggs'})
        Table(1, 2, 3, foo="bar", spam="eggs")
        Table([], {}) # Table([])
        Table([1, 2, 3], {}) # Table([1, 2, 3])
        Table(1,2,3) == Table([1,2,3]) # True
        len(Table("a", "b", "c", four="d", five="e")) # 5
    """
    type KeyValue = str | int
    # typing
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, list_val: list[Any], /): ...
    @overload
    def __init__(self, dict_val: dict[str, Any], /): ...
    @overload
    def __init__(self, list_val: list[Any], dict_val: dict[str, Any], /): ...
    @overload
    def __init__(self, *list_values: Optional[Any]): ...
    @overload
    def __init__(self, **dict_values: Optional[Any]): ...

    @overload
    def __init__(self, *list_values: Optional[Any], **
                 dict_values: Optional[Any]): ...

    @overload
    def __delitem__(self, key: KeyValue): ...
    @overload
    def __delitem__(self, key: Iterable[KeyValue]): ...

    @overload
    def __setitem__(self, key: KeyValue, value: Any): ...
    @overload
    def __setitem__(self, key: Iterable[KeyValue], value: Iterable[Any]): ...

    @overload
    def find_keys(self, value: Any, /) -> KeyValue: ...

    @overload
    def find_keys[default: Any](
        self, value: Any, /, *, default: Any = None) -> list[KeyValue] | default: ...

    @overload
    def sort(self) -> "Table": ...
    @overload
    def sort(self, *, key: Callable) -> "Table": ...
    @overload
    def sort(self, *, reverse: bool) -> "Table": ...
    @overload
    def sort(self, *, key: Callable, reverse: bool) -> "Table": ...

    ###############################################
    # Types:
    # self.list: list[Any]
    # self.dict: dict[str, Any]
    # KeyValue: str | int

    # Functions:
    # __init__
    # __getitem__
    # __setitem__
    # __delitem__
    # __iter__
    # __len__
    # _list_len_
    # _dict_len_
    # __repr__
    # _unpack_kwargs_to_str_
    # __str__
    # __contains__
    # find_keys
    # append
    # extend
    # insert
    # pop
    # remove
    # clear
    # copy
    # count
    # foreach
    # __eq__
    # __add__
    # sort
    ###############################################

    @override
    def __init__(self, *args: Optional[Any], **kwargs: Optional[Any]):
        """The init function. 
        Args:
            *list_values (list[Any] | Any): The list values. If there is only one argument, then that is set to the list.
            **dict_values (dict[str, Any] | Any): The dict values. If there is only one argument, then that is set to the dict.
        
        Examples:
            see the Table() documentation

        """
        if (  # Table([], {})
            len(args) == 2 and
            len(kwargs) == 0 and
            isinstance(args[0], list) and
            isinstance(args[1], dict)
        ):
            self.list = args[0]
            self.dict = args[1]
            return

        elif (  # Table([])
            len(args) == 1 and
            len(kwargs) == 0 and
            isinstance(args[0], list)
        ):
            self.list = list[Any](args[0])
            self.dict = dict[str, Any]({})
            return
        elif (  # Table({})
            len(args) == 1 and
            len(kwargs) == 0 and
            isinstance(args[0], dict)
        ):
            self.list = list[Any]([])
            self.dict = dict[str, Any](args[0])
            return
        # table(1, 2, 3, foo="bar", spam="eggs", ...)
        self.list = list(args)
        self.dict = dict[str, Any](kwargs)

    def __getitem__(self, key: KeyValue) -> Any:
        return self.dict[key] if isinstance(key, str) else self.list[key]

    def __setitem__(self, key: KeyValue | Iterable[KeyValue], value: Any):
        if isinstance(key, str):
            self.dict[key] = value
        elif isinstance(key, int):
            self.list[key] = value
        elif isinstance(key, Iterable):
            for i, j, _ in zip(key, value):
                self[i] = j
        else:
            raise TypeError(f"Table indices must be integers or strings, not {
                            type(key).__name__}")

    def __delitem__(self, key: KeyValue | Iterable[KeyValue]):
        if isinstance(key, Iterable):
            for i in key:
                self.__delitem__(i)
        x = str(type(key))
        match x:
            case "str":
                assert isinstance(key, str)
                if key in self.dict:
                    del self.dict[key]
                else:
                    raise KeyError(f"Key {key} not found")
            case "int":
                assert isinstance(key, int)
                if key < self._list_len_():
                    del self.list[key]
                else:
                    raise KeyError(f"Index {key} not found")
            case _:
                raise TypeError(f"Table indices must be integers or strings, not {
                                type(key).__name__}")

    @override
    def __iter__(self) -> Any:
        return iter(self.list)

    def __len__(self) -> int:
        return len(self.list) + len(list(self.dict.keys()))

    def _list_len_(self) -> int:
        return len(self.list)

    def _dict_len_(self) -> int:
        return len(self.dict)

    @override
    def __repr__(self) -> str:
        if len(self) == 0:
            return "Table()"
        return f"Table({self.list}; {self.dict})".replace(
            "[]; ", "").replace(
                "; {}", "")

    def _unpack_kwargs_to_str_(self) -> str:
        ret = ""
        for k, v in zip(self.dict.keys(), self.dict.values()):
            ret += f"{k}: {v if not isinstance(v, str) else f"'{v}'"}, "
        return ret.removesuffix(", ")

    @override
    def __str__(self) -> str:
        # if len(self) == 0:
        #    return "<>"
        return f"<{(''.join([
            f'{x}, ' for x in self.list
        ])).removesuffix(', ')}, {
                self._unpack_kwargs_to_str_()}>".replace(
                    "<, ", "<").replace(
                        ", >", ">")

    def __contains__(self, key: str) -> bool:
        return (key in self.dict) or (key in self.list)
    def find_keys(self, value: Any, /, *, default: Any=None) -> list[KeyValue] | Any:
        """Finds all keys and indices that have a value equal to value.

        Args:
            value (Any): The value to search for.
            default (Any, optional): What to return if no matches are found. Defaults to None.

        Returns:
            list[KeyValue] | Any: A list of all keys an indicies, otherwise default.
        """
        ret = []
        for i in self.list:
            if i == value:
                ret.append(i)
        for k, v in zip(self.dict.keys(), self.dict.values()):
            if v == value:
                ret.append(k)
        if len(ret) == 0:
            return default
        elif len(ret) == 1:
            return ret[0]
        return ret

    @override
    def append(self, value: Any) -> "Table":
        """Append a value to the end of the list.

        Args:
            value (Any): The value to insert.

        Returns:
            Table: self. Useful for chaining and repls.
        """
        self.list.append(value)
        return self

    @override
    def extend(self, value: Iterable[Any]) -> "Table":
        """Extend the list with another iterable.

        Args:
            value (Iterable[Any]): The other iterable.

        Returns:
            Table: self. Useful for chaining and repls.
        """
        self.list.extend(value)
        return self

    @override
    def insert(self, index: int, value: Any) -> "Table":
        """Insert a value at a specific index.

        Args:
            index (int): the index to insert at.
            value (Any): the value to insert.

        Returns:
            Table: self. Useful for chaining and repls.
        """
        self.list.insert(index, value)
        return self

    @override
    def pop(self, index: int = -1) -> Any:
        """Returns a specific value in a list and removes it.

        Args:
            index (int, optional): The value to return. Defaults to -1.

        Returns:
            E: The item that was removed.
        """
        return self.list.pop(index)

    def remove(self, value: Any) -> "Table":
        """Removes an item from the list, if it exists.

        Args:
            value (Any): The value to remove.

        Returns:
            Table: self. Useful for chaining and repls.
        """
        self.list.remove(value)
        return self

    def clear(self) -> "Table":
        """Makes the table empty.

        Returns:
            Table: An empty table. Equivalent to Table().
        """
        self.list.clear()
        self.dict.clear()
        return self

    def copy(self) -> "Table":
        """Makes a second copy of the table. Useful to deal with references.

        Returns:
            Table: A new object that is equivalent to the original.
        """
        return Table(self.list.copy(), self.dict.copy())

    def count(self, value: Any,  count_list: bool = True, count_dict_keys: bool = False, count_dict_values: bool = True) -> int:
        """Counts the number of items in a list equal to value. Also counts the number of keys and values in the dict equal to value.

        Args:
            value (Any): The value to match for.
            count_list (bool, optional): If list items should be checked. Defaults to True.
            count_dict_keys (bool, optional): If dict keys should be checked. Defaults to False.
            count_dict_values (bool, optional): If dict values should be checked. Defaults to True.

        Returns:
            int: _description_
        """
        ret = 0
        ret += self.list.count(value) if count_list else 0
        ret += list(self.dict.values()
                    ).count(value) if count_dict_values else 0
        ret += list(self.dict.keys()).count(value) if count_dict_keys else 0
        return ret

    def foreach(self, func: Callable, /, list_eval: bool =True, dict_eval: bool=True):
        """Call a function on each item in the table.

        Args:
            func (Function): The function to call. Must take two arguments: key (or index), and value.
            list_eval (bool, optional): Call the function on list items. Defaults to True.
            dict_eval (bool, optional): Call the function on dict items. Defaults to True.

        Returns:
            List: A list of all of the function returns.
            Any: The function return if there is only one.

        Raises:
            ValueError: If neither list_eval nor dict_eval are True.
        """
        if not (list_eval or dict_eval):
            raise ValueError("There is nothing to evaluate!")
        ret = []
        if bool(list_eval):
            for i, j in enumerate(self.list):
                ret += func(i, j)  # type: ignore
        if bool(dict_eval):
            for k, v in zip(self.dict.keys(), self.dict.values()):
                ret += func(k, v)  # type: ignore
        return ret if len(ret) > 1 else ret[0] if len(ret) == 1 else None

    @override
    def __eq__(self, other):
        if isinstance(other, Table):
            return self.list == other.list and self.dict == other.dict
        return False

    def __add__(self, other: Any) -> "Table":
        if isinstance(other, Table):
            return Table(self.list + other.list, self.dict | other.dict)
        elif isinstance(other, list):
            return Table(self.list + other, self.dict)
        elif isinstance(other, dict):
            return Table(self.list, self.dict | other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for +: 'Table' and '{type(other).__name__}'")

    @override
    def sort(self, *, key: Optional[Callable] = None, reverse: bool=False) -> "Table":
        """Sorts the list in place.

        Args:
            key (Optional[Callable], optional): The key to sort for. Defaults to None.
            reverse (bool, optional): If you should sort in reverse. Defaults to False.

        Returns:
            Table: self. Useful for chaining and repls.
        """
        self.list.sort(key=key, reverse=reverse)
        return self

    @override
    def __hash__(self) -> int:
        return hash((self.list, self.dict))

    @override
    def __bool__(self) -> bool:
        return bool(self.list) or bool(self.dict)

    def isempty(self) -> bool:
        """Returns True if the table is empty.

        Returns:
            bool: if the table is empty.
        """
        return not bool(self)
