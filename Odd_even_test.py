# Read the input from the user
n = int(input("Enter a positive integer: "))

# Check if n is odd
if n % 2 != 0:
    print("Weird")
# Check if n is even and in the range of 2 to 5
elif n >= 2 and n <= 5:
    print("Not Weird")
# Check if n is even and in the range of 6 to 20
elif n >= 6 and n <= 20:
    print("Weird")
# Check if n is even and greater than 20
elif n > 20:
    print("Not Weird")


try:
    print(x)
except:
    print("An exception occurred")