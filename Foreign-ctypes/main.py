from ctypes import *

### Importing the object:
my_functions = CDLL("./my_functions.so")
print(type(my_functions))

print("############################")
print("### Demonstrating int-only functions:")
print(my_functions.square(10))
print(my_functions.square(8))
print("")

print("############################")
print("### Demonstrating functions with double:")
print(my_functions.square_doubles(10))
print(my_functions.square_doubles(8))
print("")
