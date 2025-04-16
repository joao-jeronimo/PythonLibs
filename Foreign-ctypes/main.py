from ctypes import *

### Importing the object:
my_functions = CDLL("./my_functions.so")

############################
### Demonstrating int-only functions:
print(type(my_functions))
print(my_functions.square(10))
print(my_functions.square(8))

