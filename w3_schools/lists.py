'''
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:





Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

List allows duplicate values
list1 = ["apple", "banana", "orange", "apple", "orange"]

The list() Constructor
It is also possible to use the list() constructor when creating a new list.


If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:



To add an item to the end of the list, use the append() method:

Insert Items
To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

If there are more than one item with the specified value, the remove() method removes the first occurance:


If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

The del keyword also removes the specified index: and we can also remove the entire list by using del word
thislist = ["apple", "banana", "cherry"]
del thislist[0] or del thislist
print(thislist)


Clear the List
The clear() method empties the list.

The list still remains, but it has no content.


To sort descending, use the keyword argument reverse = True:

You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):




By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:



Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:

Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)



Or you can use the extend() method, where the purpose is to add elements from one list to another list:
'''
# list1 = ["apple", "banana", "orange"]
# print(len(list1))

# list1 = ["abc", 34, True, 40, "male"]
# list2 = list(("apple","bannan", True , 45, "gamlaboy","cherry","kiwi","dragonfruit"))
# # print(list2)
# # ## you can acess the list by refering tot he index number
# # print(list2[2:5]) ### here always the starting index will be included and ending index will not be included
# # print(list2[3:-3])### here the index started at 3 i.e true from there to negative index -3 is cherry which will be excluded and till gamla boy is printed 
# # print(list2[-7:-3])
# # print(list2[:3])
# # print(list2[3:])
# # if "apple" in list2:
# #     print("yes, 'apple' is in the list2")
# # list2[3:6] = ["vijay", "paradox"]## here i did not updated the 5th index number so in the result new list updated withouth cherry and if we add more items to the list it will expand 
# # print(list2)
# # thislist = ["apple", "banana", "cherry"]
# # thislist[1:2] = ["blackcurrant", "watermelon"]
# # print(thislist)
# # list2.insert(5, "gamalaboy")
# # print(list2)
# list2.append("hector")
# print(list2)
# list1 = ["omega","sid","akshath"]
# list2.extend(list1)
# print(list2)
##If there are more than one item with the specified value, the remove() method removes the first occurance:
# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)
thislist = ["apple", "canana", "Bherry","Watermelon","kawi"]
# i = 0
# while i<len(thislist):
#   print(thislist[i])
#   i = i+2
# newlist = [x if x != "banana" else "orange" for x in thislist]

# print(newlist)


# for x in thislist:
#     if "e" in x:
#         newlist.append(x)
    
# # print(newlist)    
# thislist.sort()
# print(thislist)
# x = [100, 98, 94, 92, 101, 125]
# x.sort()
# # print(x)
# # def myfunc(i):
# #     return (i-70)

# # x = [100, 98, 74, 52, 101, 125]
# # x.sort(key = myfunc)
# # print(x)
# # thislist.sort(key = str.lower)
# # print(thislist)

# # x = thislist.copy()
# # print(x)

# # x = list(thislist)
# # print(x)
# x = [1, 2, 3, 4]
# for y in x:
#     thislist.append(y)
    
# print(thislist)
# fruits = ["apple", "banana", "cherry"]
# print(fruits[-1])
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)
##ttry using aestrix in lists
x = 5%10
print(x)
