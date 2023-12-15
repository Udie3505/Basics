# # types of functions 
# # user degined function and built in functions
# # functions vs methods
# def greet():
#     print("hello this is greet")
#     print("we are learning functions")
#     print("ok done")
# # always we need to call the functions to print the function.
# greet()
# #scope of the variable
# def addition():
#     #scoping
#     num1 = int(input("enter your number1: "))
#     num2 = int(input("enter your number2: "))
#     print(f"sum of {num1} and {num2} is {num1+num2}")
    

# def subtraction():
#     num1 = int(input("enter your number1: "))
#     num2 = int(input("enter your number2: "))
#     print(f"subtraction of {num1} and {num2} is {num1-num2}")

# addition()
# subtraction()

# '''scoping1'''
# def greet():
#     name = input("enter your name: ") # here this is a different variable
#     print(f"your name is {name}")


# name = "xyz" # this name is a different variable both are not similar
# greet()
# print(name)

# '''make a function which takes 5 parameters into that function'''
# def addition(n1, n2, n3, n4, n5): # here n1,n2,n3,n4,n5 are called as parameters
#     total = n1 + n2 + n3 + n4 + n5
#     print(total)
    

# addition(5, 10, 14, 11, 9)  # here whatever we are passing are called as arguments
# # in the above lines we can send intiger or bool or string or float any kind of arguments can be sent 

# def addition_list(x):
#     print(sum(x))

# my_list = [5, 6, 4, 3, 2]
# addition_list(my_list) # if we write the code in this format its big blunder there is no logic in it 
# def addition_list(x):
#     total = 0
#     for i in x:
#         total = total +i
#     print(total)



# my_list = [5, 6, 4, 3, 2]
# addition_list(my_list)

'''global key word'''














'''return'''
def addition(num1, num2):
    total = num1 + num2
    return total # so if we are using a return then we need to store the function in some kind of a variable to return the function 

addition(10 , 5) # the output of this will be nothing as there is no variable to store the value
def addition(num1, num2):
    total = num1 + num2
    return total 

x = addition(10 , 5) # so here we have given the variable as x to store the return value hence it would print the ans
print(x) # we need not store in a variable we can directly print the function see below for the example.

def addition(num1, num2):
    total = num1 + num2
    return total 

print(addition(10 , 5))  # even we can print the return function by printing the function this can be done whene there is return function.


def addition(num1, num2):
    total = num1 + num2
    print(total) # here the values 10 and 5 go into 83 rd line and print the total on 84 th line 

x = addition(10 , 5) #but we have given x as a variable for the function but total has been already printed then something goes into x and the x value is None
print (x)


''''basic example on return when to be used and when not to be used '''

""" ask 2 numbers from user and caluclate total of 2 numbers.
print if the sum is odd or even 
we need to use two functions add() and check()"""

def add(n1, n2):
    total = n1 + n2
    return total # here we are using return function because we need to store the value of total in someplace(s) for sending the total into check
    

def check(num): # how can we send the total into check so its not possible so we need to use the return function
    if num % 2 ==0:
        print("even") # here we can use the return function too then we need to store the check value in some variable in line112 like c = print(check(s))
    else:
        print("odd") # here we can use the return function too then we need to store the check value in some variable in line112 like c = print(check(s))


x = int(input("enter n1 = "))
y = int(input("enter n2 = "))

s = add(x, y)
print(s)
check(s)











