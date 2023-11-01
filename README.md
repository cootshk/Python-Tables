# LuaTable
Implementing tables from Lua into Python 3.12

## Usage

```py
from luatable import Table

tbl = Table()
print(tbl) # <>
tbl.append(1)
tbl["foo"] = "bar"
print(tbl) # <1, foo: 'bar'>
print(tbl == Table(1,foo="bar")) # True

print(repr(tbl)) # Table([1]; {"foo": "bar"})