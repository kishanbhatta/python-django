# LOCAL
# lambda x: x**2  # this is a local level

# Enclosing function Locals
name = 'This is a global name!'

def greet():
    #name = "Sammy" # When we comment this then name search for the global level

    def hello():
        print("Hello "+name)

    hello()
greet()

# Built-in level
x = 50

def func(x):
    print('x is: ', x) # This will print the output 50
    x = 1000
    print('local x changed to: ',x)

func(x) # This will give us the output: local x changed to: 1000
print(x) # here again output is from the global x = 50


# Lets talk about the scenario that we have to change the globally define x
x = 50
def func():
    global x  # This is not the better way to write the code so we are only using here to understand how we are going to change the global variable

    x = 1000

# print("before function call, x is: ",x) # before the function call it gives us the output 50
func()
print("after function call, x is: ", x) # Now the function has been called so the global value of x changed to 1000
