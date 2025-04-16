import cffi

### Importing the object:
my_functions = ctypes.CDLL("./my_functions.so")
print(type(my_functions))

print("############################")
print("### Demonstrating int-only functions:")
print( my_functions.square(10) )
print( my_functions.square(8) )
print("")

print("############################")
print("### Demonstrating functions with double:")
my_functions.square_doubles.restype = ctypes.c_double
print( my_functions.square_doubles( ctypes.c_double(10.1) ) )
print( my_functions.square_doubles( ctypes.c_double(8.2)  ) )
print("")
