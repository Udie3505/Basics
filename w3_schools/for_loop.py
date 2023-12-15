'''A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.'''
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)

# for x in "banana":
#     print(x)
'''The break Statement
With the break statement we can stop the loop before it has looped through all the items:'''
# x = ["uday","apple","bmw","rgv"]
# for i in x:
#     print(i)
#     if i == "bmw":
#         break

'''Exit the loop when x is "banana", but this time the break comes before the print:'''
# x = ["uday","apple","bmw","rgv"]
# for i in x:
#     if i == "bmw":
#         break
#     print(i)
'''here the above two examples are different in breaking the loop one is breaking the loop after itterating till bmw and one is breaking before itterating till bmw '''

x = ["uday","apple","bmw","rgv"]
# for i in x:
#     if i == "bmw":
#         continue
#     print(i)

'''other continue statement'''
# for i in x:
#     print(i)
#     if i == "bmw":
#         continue
#     print(i)

'''The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.'''
# for x in range(2, 9):
#     print(x)

# for x in range(2, 30, 2):
#     print(x)

'''else in for loop'''
# for x in range(2, 30, 2):
#     print(x)
# else:
#     print(f"finished the range till 30 with increment of 2")

'''other example'''
# for x in range(2, 30, 2):
#     if x == 16:
#         break
#     print(x)
# else:
#     print(f"finished the range till 30 with increment of 2")
'''other example with continue'''
# for x in range(2, 30, 2):
#     if x == 16:
#         continue
#     print(x)
# else:
#     print(f"finished the range till 30 with increment of 2")

"""nested loops
Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":"""

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x, y)
        
# # another example of nested loops
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end='\t')
#     print()
    
# # another example with the help of chat gpt
# for i in range(4):
#     for j in range(4):
#         print("u ", end='')
#     print()

# #another example
# for i in range(1, 6):
#     for j in range(i):
#         print("* ", end='')
#     print()

# another example by myself asking chat gpt to give some basic questions on nested loops.
'''1 question multiplication table'''
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end = "\t") # here i used \t because it gives space of a tab so it looks sophisticated
#     print() # here if we do not use the print sttement the entire code will be printed on the same line and it does not #for a multiplication table  hence if we use print() it prints on the next line after every itteration.
'''2 half pyramid pattern'''
# for x in range(1, 5):
#     for j in range(x):
#         print("*", end ="\t")
#     print()

'''3 square of numbers'''
# for x in range(1, 6):
#     square = x ** 2
#     print(f"{x}*{x} = {square}")

'''4 vertical printing of same numbers'''
# for i in range(1, 6):
#     for j in range(i):
#         print(i)
#     print()
'''5 horizontal printing of same numbers'''
# for i in range(1, 6):
#     for j in range(i):
#         print(i, end=" ")
#     print()


'''6 inverted pyramid pattern'''
# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end ="\t")
#     print()
    

'''7 diamond pattern copied the code from chat gpt '''
# n = 3  # You can adjust the value of n to change the size of the diamond

# # Upper part of the diamond
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()

# # Lower part of the diamond
# for i in range(n - 1, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()

# i did not understood the pattern or the formula lets break it down some other time 

