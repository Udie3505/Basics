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

The clear() method empties the set
The del keyword will delete the set completely:

Join Two Sets
There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both sets, 
or the update() method that inserts all the items from one set into another:


The intersection_update() method will keep only the items that are present in both sets.

The intersection() method will return a new set, that only contains the items that are present in both sets.


Keep All, But NOT the Duplicates
The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.




The symmetric_difference() method will return a new set, that contains only the elements 
that are NOT present in both sets.




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