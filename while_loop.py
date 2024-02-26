#while loops are used to execute a set of statements as long as a condition is true.

# i = 1

# while i <= 10:
#     print(i)
#     i += 1

# print("Done with loop") #this will be printed after the loop is done

#----------------------------------------------------------------------------------------------------------

#antoher example
from datetime import datetime

datetime.now() #to get the current date and time
datetime.now().year #to get the current year
datetime.now().month #to get the current month
datetime.now().day #to get the current day
datetime.now().hour #to get the current hour
datetime.now().minute #to get the current minute
datetime.now().second #to get the current second

#a while loop that waits for two seconds and then prints a message

wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
    print('still waiting...')

print(f'we are wating at {wait_until} seconds')

#for the example above, the while loop will keep running until the current second is equal to the wait_until variable. And because the print statement
#will fill up the console, we can use the pass statement to avoid that and just wait for the time to elapse. The program above can then be written as:
#as:

wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
    pass

print(f'we are wating at {wait_until} seconds')

#other statements that can be used in the while loop to control the flow of the program are continue and break statements.
#the continue statement is used to skip the current block and return to the while statement. The break statement is used to exit the loop.
#however, note that the break statement can only break out of the innermost loop.