import cffi, pathlib

### Building the binding:
ffi = cffi.FFI()
this_dir = pathlib.Path().absolute()
h_file_name = this_dir / "my_functions.h"
with open(h_file_name) as h_file:
    ffi.cdef(h_file.read())
ffi.set_source(
    "cffi_example",
    None,
    )
ffi.compile()

exit()
print("############################")
print("### Demonstrating functions with double:")
my_functions.square_doubles.restype = ctypes.c_double
print( my_functions.square_doubles( ctypes.c_double(10.1) ) )
print( my_functions.square_doubles( ctypes.c_double(8.2)  ) )
print("")
