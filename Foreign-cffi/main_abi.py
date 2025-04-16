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

print("############################")
print("### Demonstrating functions with double:")
import cffi_example
print( cffi_example.ffi.square_doubles( 10.1 ) )    # Does not work.
print( cffi_example.ffi.square_doubles( 8.2  ) )    # Does not work.
print("")
