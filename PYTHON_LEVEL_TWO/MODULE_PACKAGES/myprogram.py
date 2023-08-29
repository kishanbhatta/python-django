# One Way to import from another file
import mymodule # currently we are in  the same folder otherwise we have to give the file location
mymodule.fun_in_module()

# Another way to import
import mymodule as mm  # here we are defining mymodule to mm so that we don't have to write mymodule again and again
mm.fun_in_module()

# If you don't want to import full module or file you can direct call the function as well
from mymodule import fun_in_module
fun_in_module()

# we can import with the below syntax as well but not suggested to work this way
# from mymodule import * # Astrik use the lot of memory to import all the things so not suggested to use this syntax
# func_in_module()