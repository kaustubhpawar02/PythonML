a=10
b=10

print(id(a)==id(b))

#In Python, the id() function returns
#the unique memory address of an object.

#Python uses an optimization technique
#called integer caching (or integer interning).
#When Python starts up, it automatically creates 
#and caches integer objects in memory 
#for the range -5 to 256