#This python program is to use if statement.
#it iterates through 1 to 100.
#if it is divisible by the number 3, it prints Fizz.
#if it is divisible by the number 5, it prints Buzz.
#If it is divisible by both 3 and 5 (or i5), it prints FizzBuzz.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

#another solution
#using itenarary operator, which is a short form of if statement (i.e a single line if statement)

for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
    '''The above code is equivalent to the following:'''

    'FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n 

    #using the above in a list comprehension
    print(['FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n for n in range(1, 101)])