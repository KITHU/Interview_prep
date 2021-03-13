# creating a list
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)


# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].
fruits.append("mango")
print(fruits)

#Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
fruits.extend(["ndizi","guava"])
print(fruits)

# insert at specified position
fruits.insert(0,"maembe")
print(fruits)

# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
fruits.remove("ndizi")
print(fruits)

# removes the last element
fruits.pop()
print(fruits)

# list.clear()
# Remove all items from the list. Equivalent to del a[:].

# shallow copy, equivalent to list.copy()
_fruits = fruits[:]
print(_fruits)

#list.copy()
count = fruits.count("apple")
print(count)

# Reverse the elements of the list in place.
_fruits.reverse()
print(_fruits)

#Remove all items from the list. Equivalent to del a[:].
_fruits.clear()
print("empty",_fruits)
