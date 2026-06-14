# Why input() function always returns a string?
#The input() function always returns a string 
# because it reads raw keyboard characters.

#Python has no way of knowing if the 
# characters "25" mean the number twenty-five
# or just a text label (like a street address). 
# Treating everything as a string is the safest 
# default because all user inputs can be represented 
# as text, but not all text can be represented 
# as numbers.

#For example, if a user types 123abc, 
# Python cannot automatically convert that into 
# a valid mathematical number,
# but it functions perfectly fine as a string

# How to Convert it (Typecasting)

#To convert the input string into a 
# different data type, you wrap the input() function 
# inside a conversion function. 
# This process is called typecasting

a=int(input("enter a number :"))
print(a)
print(type(a))

b=float(input("enter a decimal number :"))
print(b)
print(type(b))

bool=True
if bool==True:
    print(bool)
else:
    print(False)

print(type(bool))

