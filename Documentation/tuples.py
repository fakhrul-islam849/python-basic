# tuple are unchanged data collection
tuple = ('apple', 'banana', 'cherry')
print(len(tuple))
# have add , for a single variable otherwise it will be string
tuple = ('apple',)

# tuple is unchangeable but possible to convert list and then do operation
tuple = ('apple', 'banana', 'cherry')
change = list(tuple)
change.append('Kiwi')

# it is possible to unpacking - extract value into variable
# Asterisk - if variable is less then value then rest of the other value will be assigned last variable
(x, *y) = tuple
print(x)
print(y)

# looping tuple
for x in tuple:
    print(x)

# index and loop
for i in range(len(tuple)):
    print(tuple[i])

# while loop

while i <len(tuple):
    print(tuple[i])
    i = i + 1

# join tuple
tuple2 = ('house', 'car')
tuple3 = tuple + tuple2
# multiply tuple
tuple4 = tuple2 * 2

# tuple count return the same number repeat how many time

print(tuple.count('apple'))

# find the position of given value return only first

print(tuple.index('apple'))

