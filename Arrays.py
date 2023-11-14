import ctypes

a = ctypes.py_object * 8
array = a()

array[1] = 4
array[2] = 7
array[3] = 6
