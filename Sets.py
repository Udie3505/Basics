'''
Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:


Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:




You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, 
or ask if a specified value is present in a set, by using the in keyword.

To add one item to a set use the add() method.

To add items from another set into the current set, use the update() method.

The object in the update() method does not have to be a set, 
it can be any iterable object (tuples, lists, dictionaries etc.).

To remove an item in a set, use the remove(), or the discard() method.

If the item to remove does not exist, remove() will raise an error.
Note: If the item to remove does not exist, discard() will NOT raise an error.

You can also use the pop() method to remove an item, but this method will remove a random item, 
so you cannot be sure what item that gets removed.
he return value of the pop() method is the removed item.
'''
##thisset = {"apple", "banana", "cherry", "apple", 1, 2}

##print(thisset)
# thisset = {"apple", "banana", "cherry", True, False, 1, 2, 0}

# print(thisset)
# note the double round-brackets
# x = set(("uday", "arvind", "harsha"))  # note the double round-brackets
# print(x)

# y = {"apple", "banana", "cherry"}

# for x in y:
#     print(x)

x = {"uday", "banana", "cherry", True, 7, 2}
y = {"kumar", "himaja", "reddy", False, 8, 3}
x.update(y)
x.pop()
print(x)