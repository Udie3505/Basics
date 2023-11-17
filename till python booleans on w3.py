#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##python was created by guido van rossum


# In[ ]:


'''
PYTHON IS USED FOR 
web development (server-side),
software development,
mathematics,
system scripting.
'''

'''
## WHAT CAN PYTHON DO ?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.

'''


# In[ ]:


'''
Python Indentation
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.
'''


# In[ ]:


#Multiline Comments
#Python does not really have a syntax for multiline comments.
#
#To add a multiline comment you could insert a # for each line:

"""Or, not quite as intended, you can use a multiline string.

Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

"""


# In[ ]:


if 5 > 2:
    p


# In[28]:


if 5 > 2:
    print("five greater than two")


# In[2]:


if 5>2:
    print("five greater than two")


# In[3]:


if 5 > 2:
print("five greater than ")


# In[4]:


if 5 > 2:
        Print("five is greater than two")


# In[5]:


if 5 > 2:
        print("five is greater than two")


# In[6]:


## we have to use same number of spaces in the same block of code 


# In[7]:


if 5 > 2:
    print("five is greater than two")
        print("xyz")


# In[8]:


## correct way is 


# In[11]:


if 5 > 2:
    print("five is greater than two")
    print("xyz")


# In[ ]:


## when you give spacing it should be same for the entire code block


# In[14]:


if 5 > 2:
    print("five is greater than two")
if 5 > 3: 
        print("xyz")


# In[13]:


if 5 > 2:
    print("five is greater than two")
if 5 > 3:
    print("xyz")


# In[15]:


## variables


# In[ ]:


##Variables are containers for storing data values.


# In[17]:


x = 7
y = "uday"
print(x)
print(y)


# In[18]:


x = 4  # here we used x as an intiger
x = "uday"  # here we used x as an string
print(x)


# In[22]:


x = str(3)
y = float(3)
z = int(3)
print(type(x))
print(type(y))
print(type(z))


# In[ ]:


"""CASTING ## WE SHALL LEARN IN FUTURE""" 


# In[ ]:


# we can use either single or double quotes to express a string


# In[23]:


# we can use either single or double quotes to express a string
x = "uday"
print(x)
# same as 
x = 'uday'
print(x)


# In[ ]:



"""CASE- SENSITIVE"""


# In[26]:


a = "uday"
A = 4
print(A)
print(a)


# In[ ]:


"""VARIABLE NAMES
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""


# In[ ]:





# In[ ]:


Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# In[ ]:


Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"


# In[ ]:


"""
CAMEL CASE:Each word, except the first, starts with a capital letter:myVariableName = "John"
PASCAL CASE:Each word  starts with a capital letter: MyVariableName = "John"
SNAKE CASE:Each word is separated by an underscore character:my_variable_name = "John"
"""


# In[ ]:


#assign multiple variables in online and we can give one value to multiple variables


# In[3]:


x, y, z, a, b = "orange", 5, "cherry", 5, "orange"
print(x)
print(y)
print(z)
print(a)
print(b)


# In[ ]:


## unpack a collection 


# In[ ]:


variables are case sensitive 


# In[4]:


Cars = ["amg", "bmw", "toyoto"]
a, b, c = cars
print(a)
print(c)


# In[5]:


Cars = ["amg", "bmw", "toyoto"]
a, b, c = Cars
print(a)
print(c)


# In[ ]:


#IF YOU DEFINE MULTIPLE VARIABLES IN A SINGLE LINE THEY NEED TO BE SEPERATED BY COMMA 


# In[2]:


x y z a b = "orange" 5 "cherry" 5 "orange"
print(x)
print(y)
print(z)
print(a)
print(b)


# In[4]:


#OUTPUT VARIABLES
#The Python print() function is often used to output variables.
X= "UDAY"
print(X)


# In[ ]:


"""In the print ffunction multiple variables are seperated by comma
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome". check the below example 


"""


# In[11]:


x = "Python"
y = "is    "
z = "awesome"
print(x + y +z)


# In[ ]:


#For numbers, the + character works as a mathematical operator:


# In[12]:


###In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x = 5
y = "John"
print(x + y)


# In[13]:


##The best way to output multiple variables in the print() function is to separate them with commas, 
##which even support different data types:
x = 5
y = "John"
print(x, y)


# In[ ]:


##python GLOBAL VARIABLES


# In[ ]:


'''Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.'''


# In[39]:


## CREATING A VARIABLE OUTSIDE OF THE FUNCTION AND USING IT IN INSIDE OF A FUNCTION 

X = "good "
Y = "hundred"
        

def myfunc():
  print("vijay is " + Y +"percent " + X + "boy")

myfunc()
        


# In[26]:


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


# In[36]:


X = "good"
Y = 100
        

def myfunc():
  print("vijay is " + Y +"percent " + X)

myfunc()


# In[40]:


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# In[44]:


x = "good "

def myfunc():
    x = "clever"
    print("uday is "+ x + "boy")
    
myfunc()


# In[7]:


x = "outside 10"


def something():
    global x
    x = "inside 10"
    b = 12
    print(x)

something()   

print(x)


# In[ ]:


## here in the below example "good "is a global variable 
## here in the below example "clever" is a local variable 
"""
the below mentioned function is a local variable function 
def myfunc():
    x = "clever"
    print("uday is "+ x + "boy")
    
myfunc()
"""


# In[45]:


x = "good "

def myfunc():
    x = "clever"
    print("uday is "+ x + "boy")
    
myfunc()
print("uday is "+ x + "boy")


# In[ ]:


## THE GLOBAL KEYWORD
"""Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.\
"""


# In[46]:


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# In[52]:


x = "awesom"
def myfunc():
    global z
    z = "very goood "
    print ("uday was a " + z + "boy")
myfunc()

print("uday is a " + z + "boy" + "and he was " + x )


# In[53]:


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# In[ ]:


###Python Data types:


# In[54]:


x = 5
print(type(x))


# In[55]:


x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x)) 


# In[56]:


x = 20
#display x
print(x)

#display the data type of x
print(type(x))


# In[57]:


x = 20.5
#display x
print(x)

#display the data type of x
print(type(x))


# In[58]:


x = 1j
#display x
print(x)

#display the data type of x
print(type(x))


# In[59]:


x = ["apple", "banana", "cherry"]
#display x
print(x)

#display the data type of x
print(type(x))


# In[60]:


x = ("apple", "banana", "cherry")
#display x
print(x)

#display the data type of x
print(type(x))


# In[61]:


x = range(10)
#display x
print(x)

#display the data type of x
print(type(x))


# In[62]:


x = b"hello"
#display x
print(x)

#display the data type of x
print(type(x))


# In[63]:


x = memoryview(bytes(8))
#display x
print(x)

#display the data type of x
print(type(x))


# In[64]:


x = {"name" : "uday", "age" : 29,"Car" : "BMW"}
print(x)
print(type(x))


# In[65]:


##Python numbers
#Int
x = 123
y = 2650394568780793547083795749123789473854329748308478038
z = -752394809882798209480392040873920

print(type(x))
print(type(y))
print(type(z))


# In[ ]:


## float numbers


# In[66]:


x = 0.1427388532686836328
y = 134627882762.76348721648
z = -73294829.36487290

print(type(x))
print(type(y))
print(type(z))


# In[68]:


x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))



x = 300e4
y = 500E7
Z = -483E9

print(type(x))
print(type(y))
print(type(z))


# In[69]:


x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


# In[70]:


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# In[ ]:


##we cannot convert complex number into intiger or any other type of number 


# In[73]:


X = 8 #INT
Y = 5.5 #FLOAT
Z= 1+2J # COMPLEX

# conversion of int to complex 
c = complex(X)


# CONVERT COMPLEX TO INT 
a = int(z)


print(c)


# In[77]:


X = 8 #INT
Y = 5.5 #FLOAT
Z= 1+2J # COMPLEX

# conversion of int to complex 
c = complex(X)
print(c)


# In[78]:


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# In[ ]:


For generating random numbers 


# In[81]:


import random

print(random.randrange(1, 1000))


# In[ ]:


'''
Specify a Variable Type
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
'''


# In[83]:


x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3


# In[ ]:


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


# In[ ]:


x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


# In[ ]:


###Strings in python are surrounded by either single quotation marks, or double quotation marks.

###'hello' is the same as "hello".

###You can display a string literal with the print() function:


# In[84]:


print("Hello")
print('Hello')


# In[87]:


x = """uday is a
very good boy,
and he is one of the greatesh achiever of all 
time."""

print(x)


# In[ ]:


'''Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.'''


# In[95]:


a = "Hello, World!"
print(a[11])


# In[104]:


for x in "banana":
  print(x)


# In[ ]:


##o get the length of a string, use the len() function.


# In[105]:


x = 'uday is a very good boy'
print(len(x))


# In[ ]:


##Check String
##To check if a certain phrase or character is present in a string, we can use the keyword in.


# In[109]:


x = "Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters."
print("is" in x)


# In[108]:


x = "Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters."
print("many" in x)


# In[ ]:


## using of if statement 


# In[25]:


x = "Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters."
if "many" in x:
    print("yes, 'many' is there in x")


# In[27]:


## using of keyword not in 

x = "Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters."
print("uday" not in x)


# In[32]:


x = "Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters."
if "uday" not in x:
    print("uday" ' ' "not in x.")


# In[10]:


course = " python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.upper())
print(course.strip())b
print(course.lstrip())
print(course.rstrip())
print(course.find("pro"))
print(course.find("Pro"))
print(course.replace("p" , "k"))
print("pro" in course)
print("pro" not in course)
print("swift" in course)


# In[42]:


course = "python programming"
print(course.upper('PYTHON'))


# In[43]:


course = "python programming"
print(course.split())


# In[45]:


course = "python programming"
print(course.split('p'))


# In[46]:


course = "python programming"
print(course.split('o'))


# In[ ]:


'''The part before the first 'o': "pyth"
The part between the first 'o' and the second 'o': "n pr"
The part between the second 'o' and the third 'o': "gramming"
The split() method returns a list of these parts. So, if you print the result:

python
'''


# In[ ]:



"""Certainly! In the given Python code, you have a string assigned to the variable course, which is "python programming." You then use the split() method with the argument 'p' to split the string at every occurrence of the letter 'p'.

Here's what happens step by step:

The split('p') method is called on the course string.
The method looks for the letter 'p' in the string and uses it as the delimiter to split the string into parts.
It splits the string wherever it finds the letter 'p' and removes the 'p' from the resulting parts.
As a result, the string "python programming" is split into the following parts:

The part before the first 'p': "ython "
The part between the first 'p' and the second 'p': "rogramming"
The split() method returns a list of these parts. So, if you print the result:

python
Copy code
print(course.split('p'))
You will get the following output:

python
Copy code
['', 'ython ', 'rogramming']
The output is a list with three elements. The first element is an empty string because the string starts with 'p', and the split method creates an empty string before the first 'p'."""


# In[ ]:


course = "python programming"
course.split(""))


# In[ ]:





# In[17]:


course = 'python\nprogramming'
print(course)


# In[20]:


first = "uday"
middle = "kumar"
last = "surabhi"
full = first + " " + middle + " " + last
print(full)


# In[21]:


first = "uday"
middle = "kumar"
last = "surabhi"
full = f"{first} {middle} {last}"
print(full)


# In[22]:


first = "uday"
middle = "kumar"
last = "surabhi"
full = f"{len(first)} {middle} {last}"
print(full)


# In[24]:


for z in "banana":
  print(z)


# In[34]:


## slicing of index

x = "uday lauda"
print(x[3:8])


# In[35]:


x = "uday lauda"
print(x[:8])


# In[36]:


x = "uday lauda"
print(x[3:])


# In[38]:


"""Negative indexing"""
x = "uday lauda"
print(x[-4:-1])


# In[ ]:


### splitting of the string
###---> strings are immutable sequence 


# In[39]:


a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# In[48]:


a = "hello ; world"
print(a.split())


# In[51]:


###String concatenation
x = "hello"
y = "uday"
z = x + " "+ y
print(z)


x = "hello"
y = "uday"
z = x + y
print(z)


# In[ ]:


### String formatation 
'''As we learned in the Python Variables chapter, we cannot combine strings and numbers'''
'''But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:'''


# In[52]:


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


# In[57]:


age = 29
no_of_years = 8 
driving = 3
txt = " my name is uday, and I am {} years old. and i lived in u.s for {} years "
print(txt.format(age, no_of_years))


# In[54]:


"""You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


# In[56]:


age = 29
no_of_years = 8 
driving = 3
txt = " my name is uday, and I am {1} years old. and i lived in u.s for {0} years and I drive amg for {2} years."
print(txt.format(age, no_of_years, driving))


# In[62]:


###You will get an error if you use double quotes inside a string that is surrounded by double quotes:
###txt = "We are the so-called "Vikings" from the north.""""
### to fix this problem we can use escape character \"
txt = "We are the so-called \"Vikings\" from the north."
print(txt)


# In[63]:


txt = "We are the so-called \'Vikings\' from the north."
print(txt)


# In[68]:


txt = "We are the so-called \\ vikings from the north."
print(txt)


# In[69]:


txt = "We are the so-called \n vikings from the north."
print(txt)


# In[70]:


txt = "We are the so-called \r vikings from the north."
print(txt)


# In[71]:


txt = "We are the so-called \t vikings from the north."
print(txt)


# In[72]:


txt = "We are the so-called \b vikings from the north."
print(txt)


# In[ ]:


"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case

isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found

rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning"""


# In[74]:


### BOOLEAN VALUES
print(10 > 9)
print(10 == 9)
print(10 < 9)


# In[ ]:


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# In[79]:


a = "10"
b = "15"

if b < a:
    print(bool())
else:
    print(bool())


# In[76]:


print(bool("hello"))
print(bool(11))


# In[80]:


x = "Hello"
y = 15

print(bool(x))
print(bool(y))


# In[ ]:


'''Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.'''


# In[87]:


x = 0
y = ""
z = " "
print(bool(x))
print(bool(y))
print(bool(z))
a = ( 1 , 2 , 3)
b = ( )
print(bool(a))
print(bool(b))


# In[ ]:


"""You define a class myclass without any attributes or methods other than the __len__ method.

Inside the __len__ method, you return the integer value 0. This means that when you use the len() function 
on an instance of the myclass class, it will always return 0 because the __len__ method is defined to return 0.

You create an instance of the myclass class and assign it to the variable myobj:"""


# In[90]:


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# In[93]:


def myFunction() :
  return False
  

if myFunction():
  print("YES!")
else:
  print("NO!")


# In[94]:


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


# In[96]:


x = "uday"
print(isinstance(x, int))


# In[97]:


x = 300
print(isinstance(x, int))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




