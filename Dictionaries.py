# uday = {"name": "uday", "sex": "male", "age": 29, "age": [39, 44, 56]}
# # x = dict(name = "vijay", sex = "female")
# # print(uday)
# # print(uday["age"])
# # print(len(uday))
# # print(type(uday))
# # print(x)
# x = uday.get("name")
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

# Get user input
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation based on the operator
if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "Error: Invalid operator."

# Display the result
print(f"Result: {result}")
## git comments

