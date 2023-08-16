# Strings
# Basics
    # You are allowed to write string in single quote or double quote
    # 'hello'
    # "hello"
    # "You're a Hero."
# Indexing
    # negative can also be count Indexing start from 0 - n and same workaround for the minus two -2
mystring = 'abcdefg'
print(mystring[1])
# Slicing
mystring = 'abcdefg'
print(mystring[2:]) # if you want to get string from certain point to end
print(mystring[:4]) # if you want strings from start to certain point
print(mystring[2:5]) #if you want to give the range
print(mystring[:]) # for all
print(mystring[::]) # we can also give two colon :: for all
print(mystring[::1]) # if the step size is one then it print everything
print(mystring[::2]) # if the step size is two then it print the alternate character

# x = mystring.upper() # to print all in uppercase
# print(x)
#
# y = x.lower() #  for lowercase
# print(y)
#
# x = y.capitalize() # For first letter to be capital
# print (x)
#
# mystring = 'Hello Kishan Bhatta'
# x = mystring.split()
# print(x)  # which will print [Hello, Kishan, Bhatta]
#
# x = mystring.split('K')
# print(x)  #which will print ['Hello', 'ishan Bhatta']
#
# x = mystring.split('B')
# print(x)

# Basic Methods
# Print Formatting
# For single string
x = "Insert another string here: {}".format("INSERT ME!")
print(x)

# For multiple set of strings
y = "Item One: {} Item Two: {} Item Three: {}".format("dog", "cat", "mouse")
print(y)

# You can also define the variable inside of the Formate
x = "Item One: {x} Item Two: {y}".format(x="dog", y="cat") # you can able to change the variable
print(x)
