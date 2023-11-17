"""Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.


Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.


Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.




Allow Duplicates
Since tuples are indexed, they can have items with the same value:
for examples we can have two same numbers or two same stringsetc



Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

But there are some workarounds.


Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
















"""

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])


# x = ("apple", "banana", "cherry")
# y = list(x) ##This line converts the tuple x into a list and assigns it to the variable y. Now, y is a list with the same elements as x: ["apple", "banana", "cherry"].
# y[1] = "kiwi" ##Here, the second element of the list y (index 1) is modified to be "kiwi." After this line, y is now ["apple", "kiwi", "cherry"].
# x = tuple(y) ##This line converts the list y back into a tuple and assigns it to the variable x. Now, x is a tuple with the modified element: ("apple", "kiwi", "cherry").

# print(x) ##Finally, the code prints the content of the tuple x.
# So, the code starts with a tuple, converts it to a list, modifies an element in the list, and 
# then converts it back to a tuple. The result is a tuple with the same elements as the original tuple, 
# but with the second element changed to "kiwi." The conversion between tuple and list allows 
# for the modification of individual elements, which is not directly possible with tuples due to their immutability.

'''Since tuples are immutable, they do not have a built-in append() method, but there are other ways 
to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, 
add your item(s), and convert it back into a tuple.
'''
# x = ("apple", "banana", "orange", "kiwi")
# y = list(x)
# ##y.append("monkey", "donkey") ##list.append() takes exactly one argument (2 given)
# y.append("monkey")
# x = tuple(y)
# print(x)
'''
2 Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, 
(or many), create a new tuple with the item(s), and add it to the existing tuple:

Note: When creating a tuple with only one item, remember to include a comma after the item, 
otherwise it will not be identified as a tuple.
'''
# x = ("apple", "banana", "orange", "kiwi")
# y = ("orange","kawa")
# x += y
#print(x)

'''
remove items
Convert the tuple into a list, remove "apple", and convert it back into a tuple:
'''
# x = ("apple", "banana", "orange", "kiwi")
# y = list(x)
# y.pop(1)#we can use pop delete remove functions to update the list and convert into tuple
# x = tuple(y)
# print(x)

# #another example
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

'''
unpacking tuples
Using Asterisk*
If the number of variables is less than the number of values, you can 
add an * to the variable name and the values will be assigned to the variable as a list:
'''
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)
'''
If the asterisk is added to another variable name than the last, Python will assign 
values to the variable until the number of values left matches the number of variables left.

Example
'''

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# x = ("apple", "banana", "orange", "kiwi")
# i = 0
# while i < len(x):
#     print(x[i])
#     i = i + 1

fruits = ("npple", "banana", "cherry", "apple", "apple")
count_of_index = fruits.index("apple")
print(f"{count_of_index}")

