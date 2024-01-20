#tuple is a type of data structure in Python. It is similar to a list, but it is immutable that means you cannot modify the items in the tuple (what you see is what you get). 
#a tuple is also ordered, which means the items in the tuple have a defined order, and it is indexed, which means you can access any item in the tuple using its index. Tuples are written with round brackets.

coordinates = (4, 5) #tuple of integers
print(coordinates) #print the tuple
print(coordinates[0]) #print the first item in the tuple    
print(coordinates[1]) #print the second item in the tuple

#a tuple and a list looks similar, but the difference is that a tuple is immutable and a list is mutable (you can modify the items in the list, with all the list functions)
#people use tuple when they know that the data will not change, like the coordinates of a location, the date of birth of a person, etc
#you can also have a list of tuples
coordinates = [(4, 5), (6, 7), (80, 34)] #list of tuples