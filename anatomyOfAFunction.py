import math

def performOperation (num1, num2, operation):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2

performOperation(2, 3, 'sum') # 5

#named parameters helps to make the code more readable and not having to provide the operations all the time
def performOperation2 (num1, num2, operation = 'sum'):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2

#you can also provide a value when calling the function to overide the default value of the operation

performOperation2 (2, 3, operation = 'multiply') # 6

#also, you don't have to assign the value to the operation parameter, you can just provide the value
performOperation2 (2, 3, 'multiply') # 6

#what if we want the user to pass in any number of arguements they want
#we can use the *args parameter, which is a tuple of all the arguements passed in

def performOperation3 (*args): #*args tells python to expect any number of arguements, and not just a variable name. This works for positional arguements and not keyword arguements.
#positiona arguements are arguements that are not assigned to a variable name, while keyword arguements are assigned to a variable name
    print(args)

print(performOperation3(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


#for keyword arguements, we can use the **kwargs parameter, which is a dictionary of all the keyword arguements passed in
def performOperation4 (**kwargs):
    print(kwargs)

performOperation4(num1 = 1, num2 = 2, num3 = 3, num4 = 4, num5 = 5)

#NB: keyword arguements are outputted as tuples, while keyword arguements are outputted as dictionaries



#with the above, we can now write a function that can take any number of arguements and perform any operation on them and with the help of the maths module, we can perform any operation on the numbers

def performOperation5 (*args, operation='sum'):
    if operation == 'sum':
        return sum(args)
    if operation == 'multiply':
        return math.prod(*args)

print(performOperation5(1, 2, 3, 4, 5, operation='sum')) # 55