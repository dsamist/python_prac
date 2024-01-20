#if statement is used to check if a condition is true, and to make decision in our code. if the condition is true, the code under the if statement will be executed, if not, the code will not be executed
#the code under the if statement is indented
#the code under the if statement will only be executed if the condition is true
#the code under the if statement will not be executed if the condition is false

is_male = True #this is a boolean variable, it can either be true or false
is_tall = True #this is a boolean variable, it can either be true or false

if is_male and is_tall: #this is an if statement, it is used to check if a condition is true, and to make decision in our code. if the condition is true, the code under the if statement will be executed, if not, the code will not be executed
    print("The user is a tall male") #this is a code under the if statement, it will only be executed if the condition in the if statement is true
elif is_male and not(is_tall): #this is an elif statement, it is used to check if a condition is true, and to make decision in our code. if the condition is true, the code under the elif statement will be executed, if not, the code will not be executed
    print("the user is a short male") #this is a code under the elif statement, it will only be executed if the condition in the elif statement is true
elif not(is_male) and is_tall: #this is an elif statement, it is used to check if a condition is true, and to make decision in our code. if the condition is true, the code under the elif statement will be executed, if not, the code will not be executed
    print("you are not a male, but you are tall") #this is a code under the elif statement, it will only be executed if the condition in the elif statement is true
else: 
    print("The user is neither a male nor tall") #this is an else statement, it is used to execute a code if the condition in the if statement is false 



def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else: 
        return num3

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

max_num(num1, num2, num3)
print("The maximum number is " + str(max_num(num1, num2, num3))) #str() is used to convert the integer to a string, because you cannot concatenate a string and an integer