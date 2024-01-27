#this is a simple calculator
#create two variables and assign them to numbers that will be used for the artimethic operations
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")


#convert the numbers to integers, this is because the input function takes in strings, so it has to be converted to integers
# result = int(num1) + int(num2) #addition
# print(result)

#int() converts the number to an integer, hence if you want to do decimal numbers, you have to use float(). float() converts the number to a float
result2 = float(num1) + float(num2) #addition
print(result2)