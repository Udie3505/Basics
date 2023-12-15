# i = 1 #This line initializes a variable i with the value 1. This variable will be used as a counter in the loop.
# while i < 10: #This line starts a while loop. The condition i < 10 checks whether the value of i is less than 10. If this condition is true, the code inside the loop will be executed.
#     print(i) #This line prints the current value of i to the console. In the first iteration, it will print 1, and in subsequent iterations, it will print the incremented values of i.
#     i += 1 #This line increments the value of i by 1 in each iteration of the loop. It's equivalent to i = i + 1. This is crucial to ensure that the loop will eventually exit when i becomes equal to or greater than 10.

# i = 1
# while i < 10:
#     print(i)
#     i += 2
"""to break a infinte loop we can use ctrl+c on the terminal """
# i = 1
# while i < 6:
#     print(i)
#     if i == 5:
#         break
#     i += 1
"""With the continue statement we can stop the current iteration, and continue with the next:"""
# i = 1
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
# i = 1
# while i < 10:
#     print(f"current value of i: {i}")
#     i += 1
#     if i == 4:
#         continue
#         print(f"current value of i: {i}")
#     if i == 9:
#         break
# else:
#     print(f"current value of i: > 6")
# i = 1

# while i < 10:
#     if i == 4:
#         # Skip printing 4
#         i += 1
#         continue

#     print(i)

#     if i == 9:
#         # Break the loop when i is 9
#         break

#     i += 1
# i = 1
# while i < 10:
#     if i == 4:
#         i += 1
#         continue
#     print(f"current value of i : {i}")
#     if i == 8:
#         i += 1
#         break
# else:
#     print(f"current value of i is greater than 9")
i = 1
while i < 10:
    if i == 4:
        i += 1
        continue
    print(f"current value of i: {i}")
    if i == 8:
        break
    i += 1
else:
    print(f"current value of i is greater than 9")
