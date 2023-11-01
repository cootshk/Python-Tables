# LuaTable
Implementing tables from Lua into Python 3.12

## Usage

```py
from luatable import Table

tbl = Table()
print(tbl) # <>
tbl.append(1)
tbl["foo"] = "bar"
print(tbl) # <1, 'foo': 'bar'>
print(tbl == Table(1,foo="bar")) # True

print(tbl.foreach(lambda x, y: print(f"{x = }\n{y = }")))
# x = 0
# y = 1
# x = foo
# y = bar