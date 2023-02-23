# list comprehension
oldList = ['Germany', 'Bangladesh', 'UK', 'Koblenz']
newList = []

for x in oldList:
    if 'a' in x:
        newList.append(x)

print(newList)

# list comprehension short code

oldList = ['Germany', 'Bangladesh', 'UK', 'Koblenz', 'america']
newList = [x for x in oldList if 'a' in x]
print(newList)

# short list

oldList.sort() # by default sort is ascending for string and number
oldList.sort(reverse=True) # reverse the keyword
oldList.sort(key= str.lower) # case intensive ascending sort
oldList.reverse() # reverse the list
print(oldList)

# a = b is only reference use copy or define list for copy a list item
newList = oldList.copy()
newList = list(oldList)
print(newList)