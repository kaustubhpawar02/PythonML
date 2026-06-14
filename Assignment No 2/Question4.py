import sys
a=10
print(sys.getsizeof(a))

#getsizeof() function returns the exact memoey size of an
#an object in bytes

b=[10]
print(sys.getsizeof(b))

#Memory sizes differ across data types
#  because each type requires a different 
# amount of structural overhead 
# (metadata) to be managed by the Python interpreter.