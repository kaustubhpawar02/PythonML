# The id() function returns a unique integer representing 
# the memory address of an object

# Not Always
# Whether two variables holding the same value share 
# the same id() depends entirely on the
# datatype and how the value wasa created

a=78
b=78
print(id(a)==id(b))

a=[56,76,45]
b=[56,76,45]

print(id(a)==id(b))