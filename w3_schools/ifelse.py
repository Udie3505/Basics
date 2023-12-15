# a = 450
# b = 570
# if b > a:
#     print("b is greater than a")##Python relies on indentation (whitespace at the beginning of a line) 
#     # to define scope in the code.
#     # Other programming languages often use curly-brackets for this purpose.
    
# if a > b:
# print("a is greater than b") #here we will get an error because of indentation 

""" Elif
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition"."""
# a = 33
# b = 33
# if b > a:
#     print("b is greater than a")
# elif a > b:
#     print("a greater than b")
# else:
#     print("a  and b are equal")


#one more example
# a = 100
# b = 200
# if b < a:
#     print("b is less than a")
# elif b == a:
#     print("a and b are equal")
# else:
#     print("b is greater than a")

"""short hand if function"""
# a = 100
# b = 200
# if a > b: print("a greater than b")
# else: print("a is less than b")

# one more example of printing both if and else on one line
# a = 100
# b = 200
# print("a greater than b") if a > b else print("b is greater than a")

"""one more example by using 3 conditions in one line"""
# a = 100
# b = 100
# print("a greater than b") if a > b else print("b is greater than a") if b > a else print ("a and b are equal")

#combining conditional statements with if and ifelse

a = 100
b = 200
c = 300
# if a < b and b < c:
#     print("c is the biggest of all 3")

# if a > b or c >b:
#     print("true")

# if not b < a:
#     print("false")

"""nested if
You can have if statements inside if statements, this is called nested if statements.
"""
# x = 39
# if x > 10:
#     print("x is greater than 10")
#     if x > 20:
#         print("x is greater than 20")
#         if x > 30:
#             print("x greater than 30")
#             if x > 40:
#                 print("x greater than 40")
#             else:
#                 print("but not above 40")

# using nested loops with f string in print statements
x = 39
# result = grade = hero = zero = final = None
# #Now, all the variables (result, hero, zero, and final) are initialized outside the nested if-else 
# # blocks to ensure they exist regardless of the conditions. This way, you won't encounter a NameError 
# # when trying to print the formatted string.
# if x > 10:
#     result = "it is above 10"
#     if x > 20:
#         grade = "it is above 20"
#         if x > 30:
#             hero = "it is above 30"
#             if x > 40:
#                 zero = "it is above 40"
#             else:
#                 final = "it is not above 40"

# print(f"{result} and {grade} and {hero} and {zero} and {final}")
# if x > 10:
#     result = "10"
# elif x > 20:
#     result = "20"
# elif x > 30:
#     result = "30"
# elif x > 40:
#     result = "40"
# else:
#     result = "40"

# print(f"x is greater than{result} and x is greater than{result} and x is greater than{result} and x is less than {result} ")
# x = 39

# if x > 40:
#     result = "40"
# elif x > 30:
#     result = "30"
# elif x > 20:
#     result = "20"
# elif x > 10:
#     result = "10"
# else:
#     result = "less than 10"

# print(f"x is greater than {result} and x is greater than {result} and x is greater than {result} and x is less than {result}")
a = 33
b = 200
"""if statements cannot be empty, but if you for some reason have an if statement with no content, 
put in the pass statement to avoid getting an error."""
if b > a:
    pass


