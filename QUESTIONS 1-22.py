# print("uday",end=" ")
# print("was a good boy", end=" ")
# print("and awesome buddy")
# # questions and answers from code and debug 
# #question- 1
# path = "c:\\users\\john\\Desktop\\file.txt"
# print(path)
# #question-2
# x = "he said,\"Hello!\"."
# print(x)

# #question -3 
# x = "She said,\'it\'s cold\'."
# print(x)
# print("my name is uday\ni am 29 years old\nmy girlfriend name is Himaja")
# output = 'My girlfriend name is\t\t "himaja"\\"manvitha".'
# print(output)

## alt shift down arrow will help us to copy the above line 
# name = "uday"
# age = 36
# gender = "male"

# print(f"my name is {name} and my age is {age} and my gender is {gender} and a good boy")


# ##input function

# name = input("type your name = ")
# age = input("type your age = ")
# gender = input("type your gender = ")
# print("you entered")
# print(f"my name is {name} and my age is {age} and my gender is {gender}")

##so inputs always stores string by default 
# num1 = int(input("enter your first number = "))
# num2 = int(input("enter your second number = "))
# num3 = int(input("enter your third number = "))
# num4 = int(input("enter your fourth number = "))
# num5 = int(input("enter your fifth number = "))

# total = num1+num2+num3+num4+num5
# print(f"Your total is = {total}")

# ##q4
# x = int(input("enter number 1 = "))
# y = int(input("enter number 2 = "))
# total = x+y
# print(f"Total of {x} and {y} is {total}")

##Q5

# x = "356"
# print(x, type(x))

# #converting string to intiger

# y = int(x)
# print(y, type(y))
# #viceversa
# x = 320
# print(x, type(x))

# #converting integer to string

# y = str(x)
# print(y, type(y))

# #q6
# w = float(input("enter width = "))
# h = float(input("enter height = "))
# area = w*h
# print(f"the area of rectangle is {area}")

##q7

# num1 = int(input("enter your first number = "))
# num2 = int(input("enter your second number = "))
# num3 = int(input("enter your third number = "))

# average = (num1+num2+num3)/3
# print(f"average of 3 numbers is {average}")

##q8
# x = 44.5
# print(x, type(x))

# y = int(x)
# print(y, type(y))

# x = 23
# print(x, type(x))

# y = float(x)
# print(y, type(y))

# ##q9
# fahrenheit_temperature = float(input("enter your temperature in fahrenheit = "))
# celsius_temperature = (fahrenheit_temperature - 32) * 5/9
# print(f"{fahrenheit_temperature} fahrenheight converted into celsius temperature will be {celsius_temperature}")

#q10
# num1 = float(input("enter your first number = "))
# num2 = float(input("enter your second number = "))
# num3 = float(input("enter your third number = "))
# num4 = float(input("enter your fourth number = "))
# num5 = float(input("enter your fifth number = "))

# sum = num1+num2+num3+num4+num5
# max_score_per_Subject = 100
# total_sum = max_score_per_Subject*5
# percentage = (sum/total_sum)*100
# print(f"percentage of 5 subjects is {percentage} and sum of 5 subjects is {sum} ")

#q11
# games_played = int(input("Total no of games played = "))
# games_Won = int(input("Total no of games won = "))
# games_lost = int(input("Total no of losses = "))
# games_tied = (games_played-games_Won-games_lost)
# total_points = (games_Won*4)+(games_tied*2)
# print(f"total points {total_points} and total matches tied {games_tied}")

##q12)
# x = float(input("enter your first number = "))
# y = float(input("enter your second number = "))
# print(x+y)
# print(x-y)
# print(x/y)
# print(x*y)
# print(x%y)
# print(x//y)
# print(x**y)
##13q) not solved
# x = 10
# x+= 5
# print(x)
#q14)
# principal = float(input("enter the principal amount = "))
# rate_of_interest = float(input("enter the rate of interest = "))
# number_of_times_interest_compounded_annually = float(input("enter the number of times interest is compounded annually = "))
# tenure = float(input("enter the tenure in years = "))
# amount = principal*(1 + rate_of_interest/number_of_times_interest_compounded_annually)**(number_of_times_interest_compounded_annually*tenure)
# interest_earned = amount-principal
# print(f"interest earned : {interest_earned}")
#q15
# radius = float(input("enter the radius of a circle = "))
# area = 3.14*(radius)**2
# print(f"Area of the circle is {area}")

# #q18
# p = True
# q = False
# print(not p or q)

# #q19
# x = 15
# y = 10
# # print(x == y or x > y) 
# x = 25
# print(x % 2 == 0)