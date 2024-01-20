# a code that demonstrate the use of functions in python
#a function is a collection of codes that performs a specific task
#functions are used to make codes more organized and easier to read

#functions are written with a keyword def, followed by the name of the function, then a parenthesis, then a colon
#the codes in the function are indented
def says_hi(): #this is a function that prints out a string
    print("Hello user!")

says_hi() #this is how you call a function

def says_hi_with_name(name): #this is a function that prints out a string with a variable, this is achieved by adding a parameter to the function
    print("Hello " + name + "!")

says_hi_with_name("sam") #this is how you call a function with a variable
says_hi_with_name("emma") #this is how you call a function with a variable
says_hi_with_name("sunday") #this is how you call a function with a variable

#naming of functions should be done in a way that it is easy to understand what the function does and in lowercase

#a fucntion can also have more than one parameter
def says_hi_with_name_and_age(name, age): #this is a function that prints out a string with two variables, this is achieved by adding two parameters to the function
    print("Hello " + name + "! You are " + age + " years old.")

says_hi_with_name_and_age("sam", "20") #this is how you call a function with two variables

# a function can also return a value, this is done by using the keyword return
def cube_a_number(number): #this is a function that cubes a number
    return number * number * number #this is how you return a value from a function

print(cube_a_number(3)) #this is how you call a function that returns a value
print(cube_a_number(10)) #this is how you call a function that returns a value

#parameters are the variables in the parenthesis of a function, and it is used to give information to a function, while the return is use to return a information from a function
#anything after the return keyword will not be executed, because the return keyword breaks out of the function