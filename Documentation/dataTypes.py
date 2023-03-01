"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
str = 'Hello world'
print(type(str))

int = 5
print(type(int))

float = 20.0
print(type(float))

# complex number is written with j
complex = 1j
print(type(complex))

list = ["First", "Second", "Third"]
print(type(list))

tuple = ("First", "Second", "Third")
print(type(tuple))

range = range(6)
print(type(range))

dict = {'name' : 'jewel', 'age': 27}
print(type(dict))

set = {"apple", "banana", "cherry"}
print(type(set))

frozenSet = frozenset({"apple", "banana", "cherry"})
print(type(frozenSet))

bool = True
print(bool)

byteV = b"Jewel"
print(type(byteV))

byteArray = bytearray(5)
print(type(byteArray))

memoryView = memoryview(bytes(5))
print(memoryView)

none = None
print(type(none))

# display random number
import random

print(random.randrange(1, 10))

# determine the data types
# built-in function isinstance() it will return true or false

x = 200
print(isinstance(x, int))
