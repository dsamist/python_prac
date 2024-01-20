print(5) #integer
print(5.098) #float
print(-5.098) #negative float
print(3 + 4.5) #addition
print(3 * 4 + 5) #order of operations
print(3 * (4 + 5)) #order of operations
print(10 % 3) #modulus operator, gives the remainder

#numbers can be stored in variables

my_num = 5
print(my_num) #this will print 5 because it is assiged to the variable my_num
print(str(my_num)) #this will print 5 as a string because it is converted to a string
print(str(my_num) + " is my favorite number") #this will print 5 is my favorite number because it is converted to a string and concatenated with the string
print(f"{my_num}" + " is my favorite number") #this uses formated string literals to print 5 is my favorite number
my_num_neg = -5
print(abs(my_num_neg)) #this will print the absolute value of the number, that means it will print the number without the negative sign
print(pow(3, 2)) #this will print 3 to the power of 2, the pow function takes two arguments, the first is the base and the second is the power
print(3 ** 2) #this will print 3 to the power of 2, the ** operator takes two arguments, the first is the base and the second is the power
print(max(4, 6)) #this will print the maximum number between the two numbers
print(min(4, 6)) #this will print the minimum number between the two numbers
print(round(3.2)) #this will round the number to the nearest integer
print(round(3.7)) #this will round the number to the nearest integer, where it rounds up if the decimal is greater than or equal to 5

#the import statement allows you to use functions from other python files, to use this functions you have to import the file first
#you can also import functions from python libraries
from math import * #this will import all the functions from the math library
import math #this will import the math library
print(floor(3.7)) #this will round the number down to the nearest integer
print(ceil(3.2)) #this will round the number up to the nearest integer
print(sqrt(36)) #this will print the square root of the number
print(dir(math)) #this will print all the functions in the math library