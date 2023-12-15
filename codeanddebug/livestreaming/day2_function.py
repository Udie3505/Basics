'''positional arguments'''
# def total_marks(m, s, e, h, history):
#     total = m + s + e + h +history
#     print(total)

# total_marks(89, 70, 54, 45, 61)
# total_marks(s=90, m=45, e=54, h=115, history=55)
'''default arguments'''
# def add(num1, num2=100):# here we can give a default valu for few parameters
#     print(num1 + num2)


# add(15)## this default parameteres will be used in the future when we learn django where we might be needing to send 15 parameters and few of them might be default parameters

'''arguments and kwargs'''
'''args''' '''and args is a tuple'''
# def add(x, y, z):
#     total = x + y +z
#     print(total) #this will result in tuple

# add(1, 2, 3)
# add(1, 2, 3, 55, 66) # here we will get an error as 5 arguments were given 
# add(1, 2, 3, 4) # here we will get an error as 4 arguments were given instead of 3
# to fix this we can use args keyword for n number of arguments and they form a tuple 

# def add(*args): #this will be helpfull when we dont know know no of parameters
#     print(args) #this will result in tuple

# add(1, 2, 3)
# add(1, 2, 3, 55, 66)
# add(1, 2, 3, 4)

# def add(*args):
#     print(sum(args)) #this will result in addition of tuples

# add(1, 2, 3)
# add(1, 2, 3, 55, 66)
# add(1, 2, 3, 4)

# def add(*args):
#     print(args)

# add(1, 2, 3)
# add([1, 2], [3, 55], 66, 89) # we can send a list in args and we cannot sum this we will receive an error
# add(1, 2, 3, 4)

'''key word arguments **kwargs'''
'''kwargs will form adictionary'''

# def add(**kwargs):
#     print(kwargs)

# add(name = "uday", age = 29, gender = "male" )

# def add(n1, n2, n3, *args, **kwargs):
#     print(f"{n1 = }")
#     print(f"{n2 = }")
#     print(f"{n3 = }")
#     print(f"{args = }")
#     print(f"{kwargs = }")

# add(5 , 10, 15)


# def add(n1, n2, n3, *args, **kwargs):
#     print(f"{n1 = }")
#     print(f"{n2 = }")
#     print(f"{n3 = }")
#     print(f"{args = }")
#     print(f"{kwargs = }")

# add(5 , 10, 15, 100, 101, 155, 187)

# def add(n1, n2, n3, *args, **kwargs):
#     print(f"{n1 = }")
#     print(f"{n2 = }")
#     print(f"{n3 = }")
#     print(f"{args = }")
#     print(f"{kwargs = }") # we can also say keyword arguments goes into kwargs

# add(5 , 10, 15, 100, 101, 155, 187, name = "uday", age = 29, gender = "male")

'''lambda function - annonymous function'''
# def add_numbers(n1, n2, n3):
#     return n1 + n2 + n3
    
# even lambda also returns the functions

# add_numbers = lambda n1, n2, n3: n1 + n2 + n3

# print(add_numbers(10, 20, 30))

'''take a argument whih will be number make a list from 0 to n '''

# make_list = lambda n:[i for i in range(0, n +1)] #here we need to give parametere only and cannot give input for lambda

# length = int(input("enter the length of the list: "))
# length1 = int(input("enter the length1 of the list: "))

# list1 = make_list(length)
# list2 = make_list(length1)
# list3 = make_list(12)

# print(f"{list1}")
# print(f"{list2}")
# print(f"{list3}")

'''simple example to check the given number is even or odd'''

# check_even = lambda n: n % 2 == 0

# if check_even(31):
#     print("even")
# else:
#     print("odd")
'''terniary operator by using lambda'''
# check_even = lambda num: print("even") if num % 2 == 0 else print("odd")
# check_even(44)
# check_even(43)

'''important thing annotations'''
# def add(x, y):
#     total = x + y
#     print(total)

# add("10", 20) # as we know we cannot add string with intiger

# def add(x: int, y: int):
#     total = x + y
#     print(total)

# add("10", "20")

# a = [11, 15, 83, 34, 65]

# a.sort()
# print(a)

# c = a.count(7) # here if we place cursor on count u will see the return value as int

from typing import *

def sum_of_lists(x: list[int]):
    print(sum(x))

sum_of_lists([1, 2 , 3, 4])
sum_of_lists([100, 200])



















