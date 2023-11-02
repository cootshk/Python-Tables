#check for python version
import sys
if sys.version_info < (3, 12):
    print("This script requires Python 3.12+")
    exit(1)
del sys
from typing import Iterable, override, Any, Optional, overload, Callable
class Table(Iterable):
    type KeyValue = str | int
    #typing
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, list: list[Any],/): ...
    @overload
    def __init__(self, dict: dict[str, Any],/): ...
    @overload
    def __init__(self, list: list[Any], dict: dict[str, Any],/): ...
    @overload
    def __init__(self, *list_values: Optional[Any]): ...
    @overload
    def __init__(self, **dict_values: Optional[Any]): ...
    @overload
    def __init__(self, *list_values: Optional[Any], **dict_values: Optional[Any]): ...

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
    def find_keys[default: Any](self, value: Any,/,*, default:default=None) -> list[KeyValue] | default: ...
    ###############################################
    # Types:
    # self.list: list[Any]
    # self.dict: dict[str, Any]
    # KeyValue: str | int
    # TODO: Ensure that all lines have type hinting
    ###############################################

    @override
    def __init__(self, *args: Optional[Any], **kwargs: Optional[Any]):
        if ( #Table([], {})
            len(args) == 2 and
            len(kwargs) == 0 and
            isinstance(args[0], list) and
            isinstance(args[1], dict)
        ):
            self.list = args[0]
            self.dict = args[1]
            return

        elif ( #Table([])
            len(args) == 1 and
            len(kwargs) == 0 and
            isinstance(args[0], list)
        ):
            self.list = list[Any](args[0])
            self.dict = dict[str, Any]({})
            return
        elif ( #Table({})
            len(args) == 1 and
            len(kwargs) == 0 and
            isinstance(args[0], dict)
        ):
            self.list = list[Any]([])
            self.dict = dict[str, Any](args[0])
            return
        #table(1, 2, 3, foo="bar", spam="eggs", ...)
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
            for i, j, k in zip(key, value, range(len(value))):
                self.__setitem__(i, value)
        else:
            raise TypeError(f"Table indices must be integers or strings, not {type(key).__name__}")
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
                raise TypeError(f"Table indices must be integers or strings, not {type(key).__name__}")
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
        return f"Table({self.list}; {self.dict})".replace("[]; ", "").replace("; {}", "")
    def _unpack_kwargs_to_str_(self) -> str:
        ret = ""
        for k, v in zip(self.dict.keys(), self.dict.values()):
            ret += f"{k}:{v if not isinstance(v, str) else f"'{v}'"}, "
        return ret.removesuffix(", ")
    @override
    def __str__(self) -> str:
        #if len(self) == 0:
        #    return "<>"
        return f"<{(''.join([f'{x}, ' for x in self.list])).removesuffix(', ')}, {self._unpack_kwargs_to_str_()}>".replace("<, ", "<").replace(", >",">")
    def __contains__(self, key: str) -> bool:
        return (key in self.dict) or (key in self.list)
    def find_keys(self, value: Any, /, *, default:Any=None) -> list[KeyValue] | Any:
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
    def append(self, value: Any):
        self.list.append(value)
    def extend(self, value: Iterable[Any]):
        self.list.extend(value)
    def insert(self, index: int, value: Any):
        self.list.insert(index, value)
    def pop(self, index: int=-1) -> Any:
        return self.list.pop(index)
    def remove(self, value: Any):
        self.list.remove(value)
    def clear(self):
        self.list.clear()
        self.dict.clear()
    def copy(self) -> "Table":
        return Table(self.list.copy(), self.dict.copy())
    def count(self, value: Any) -> int:
        return self.list.count(value)
    def foreach(self, func: Callable, /, list_eval: bool=True, dict_eval: bool=True):
        ret = []
        if bool(list_eval):
            for i, j in enumerate(self.list):
                ret += func(i, j) #type: ignore
        if bool(dict_eval):
            for k, v in zip(self.dict.keys(), self.dict.values()):
                ret += func(k, v) #type: ignore
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
            raise TypeError(f"unsupported operand type(s) for +: 'Table' and '{type(other).__name__}'")
    @override
    def sort(self, key: Optional[Callable]=None, reverse: bool=False):
        self.list.sort(key=key, reverse=reverse)
        return self
