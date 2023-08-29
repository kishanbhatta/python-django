## Global and local variables revision

# s = "GLOBAL VARIABLE!"
# def func():
#     mylocal = 10
#     print(locals())
#     print(globals()['s'])
#     # s=50
#     # print(s)
#
# func()
# # print(s)

## FUNCTIONA ND FUNCTION ASSIGNMENT
# def hello(name='Kishan'):
#     return "hello "+name
#
# print(hello())
#
# mynewgreet = hello
#
# print(mynewgreet())

## Function within Function
# def hello(name="Kishan"):
#     print("THE HELLO() FUNCTION HAS BEEN RUN!")
#
#     def greet():
#         return "THIS STRING IS INSIDE GREET()"
#     def welcome():
#         return "THIS STRING IS INSIDE WELCOME!"
#     print(greet())
#     print(welcome())
#     print("End of hello()")
# welcome()

## Returning Function

# def hello(name="Kishan"):
#     print("THE HELLO() FUNCTION HAS BEEN RUN!")
#
#     def greet():
#         return "THIS STRING IS INSIDE GREET()"
#     def welcome():
#         return "THIS STRING IS INSIDE WELCOME!"
#     if name == "Kishan":
#         return greet
#     else:
#         return welcome
# x = hello()
#
# print(x())

# Function as an arguments
# def hello():
#     return "Hi Kishan!"
#
# def other(func):
#     print("HELLO")
#     print(func())
#
# other(hello)

# Basic step to create a Decorator
def new_decorator(func):
    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func
def func_needs_decorator():
    print("This FUNCTION IS IN NEED OF A DECORATOR!")

func_needs_decorator = new_decorator(func_needs_decprator)