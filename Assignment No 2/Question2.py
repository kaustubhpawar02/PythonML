a= 10
b = 10

print(id(a)==id(b))  #True

a = [10]
b = [10]

print(id(a)==id(b))  #False

# Whether two variables holding the same value share 
# the same id() depends entirely on the
# datatype and how the value wasa created

