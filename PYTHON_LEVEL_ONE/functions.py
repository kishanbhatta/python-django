# def python_def_keyword(param1='default'):
#     print("Hello {}".format(param1))
# python_def_keyword()
#
# # If our function has a doc string
# def my_func(param1='default'):
#     """
#     This is the DocString
#     """
#     print("my first python function! {}".format(param1))
#
# def hello():
#     print("hello")
#
# hello()
#
#
# def hello():
#     return "hello"
#
# result = hello()
# print(result)
#
# def addNum(num1, num2):
#     return num1 + num2
#
# result = addNum(2,3) # Python add numbers. results would be 5
# # result = addNum("2", "3") # Python even add strings as well result would be 23
# print(type(result)) # Python tell us the type of the string. OUTPUT: <class 'str'> for string and <class 'int'>
# # print(result)
#
# def addNum (num1, num2):
#     if type(num1)==type(num2)==type(10):
#         return num1+num2
#     else:
#         return "Sorry, I need integers!"
# # result = addNum(2,3)
# result = addNum("2","3")
# print(result)
#
# # Input method practice
# print('Enter your name:')
# x = input()
# print('Hello '+x)
#
# # Lamda Expression
#
# # Filter function
# mylist = [1,2,3,4,5,6,7,8,9,10]
#
# # def even_bool(num):
# #     return num%2 == 0
#
# evens = filter(lambda num:num%2==0,mylist)
# print(list(evens))
#
# tweet = "Go Sports! #Sports"
# result = tweet.split('#')[1] # if you don't put the [1] then all the text will be print but seggregated by comma
# print(result)
#
# print('x' in [1,2,3,'x'])

#Write a function that returns tells you whether a number is even or not
# def evencheck(num):
#     print("I'm checking to see if {} is even!".format(num))
#     print(num%2==0)
# evencheck(42)

# Write a function that will greet you!
def helloYou(name = input("Enter Your name:")):
    return("Hello, "+name)
result = helloYou()
print(result)


# Write a function taht will add two numbers together, only if they are even!
def addEvenOnly(num1, num2):
    """
    INPUT: Two numbers
    OUTPUT: False if both numbers are not even,
    the sum if both number are even
    """
    if(num1 % 2 != 0) or (num2 % 2 != 0):
        return False
    else:
        return num1 + num2
x = addEvenOnly(1,2)
y = addEvenOnly(2,2)
print(x)
print(y)

# Lambda Expression
def timesTwo(num):
    return num*2

# Same in lamda Expression
lambda num: num*2

# To really understand the use case for this, we need to introduce a function
# that accepts other functions as input parameters, in this case, we will use filter:
my_list = [1,2,3,4,5,6,7,8,9,10]

def evenBool(num):
    return num%2 == 0

evens = filter (evenBool, my_list)
print(list(evens))

# Now with Lambda!
evens = filter(lambda num: num%2==0, my_list)
print(list(evens))

# Methods are almost like functions that are built into the object. Some Methods
# return something, other just affect the object in place.
st = 'hello my name is Sam'
st.lower()
st.upper()
st.split()

tweet = 'Go Sports! #Sports'
tweet.split('#')
tweet.split('#')[1]

d = {'k1':1, 'k2':2}
d.keys()
d.items()

lst = [1,2,3]
x = lst.pop()

# in Operator (not a method, just something useful)
'x' in [1,2,3]
'x' in ['x', 'y','z']
