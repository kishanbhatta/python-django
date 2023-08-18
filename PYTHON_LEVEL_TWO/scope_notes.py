#SCOPE
#Python scope follows the LEGB Rule:
    # Local (L)
    # Enclosing Function Locals (E)
    # Global (G)
    # Built-in (B)

# L: Local -- Names assigned in any way within a function (def pr lambda), and
                # not declared global in that function.
# E: (EFLs) -- Name in the local scopeof any and all enclosing functions
                # (def or lambda), from inner to outer.
# G: Global (module) -- names assigned at the top-level of a module file,
                # or declared global in a def within the file.
# B: Built-in (Python) -- Names preassigned in the built-in names module:
                # open, range, SyntaxError,...


# Examples
x = 25

def my_func():
    x = 50
    return(x)

# print(x)  #We will get 25 as out output for this print
# print(my_func()) # we will get the output 50

my_func()
print(x)  # In this scenario we will get the output 25
