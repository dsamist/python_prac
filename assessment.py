###HENNGE TECHNICAL CHALLENGE###

# Define a function to calculate the sum of squares of non-negative integers in a list
def sum_of_squares(numbers):
    # Base case: If the list is empty, return 0
    if len(numbers) == 0:
        return 0
    else:
        x = numbers[0]  # Get the first number in the list
        # If the number is non-negative, calculate its square and add to the sum of squares of the rest of the list
        if x >= 0:
            return x * x + sum_of_squares(numbers[1:])
        else:  # If the number is negative, skip it and calculate the sum of squares of the rest of the list
            return sum_of_squares(numbers[1:])

# Define a function to handle multiple test cases
def handle_test_cases(test_cases):
    # Base case: If there are no more test cases, stop
    if test_cases == 0:
        return
    else:
        x = int(input())  # Get the number of integers in the test case
        numbers = list(map(int, input().split()))  # Get the list of integers
        result = sum_of_squares(numbers)  # Calculate the sum of squares of non-negative integers
        print(result)  # Print the calculated result
        handle_test_cases(test_cases - 1)  # Recursively handle the next test case

# Define the main function to handle input and initiate the test cases handling
def main():
    num_test_cases = int(input())  # Get the number of test cases
    handle_test_cases(num_test_cases)  # Handle the test cases

# Run the main function
if __name__ == "__main__":
    main()

# End of file
    ##https://gist.github.com/dsamist/3d4d1b458482a816c9fd6872fe9ab57d
    ##https://medium.com/henngeblog/a-japanese-company-like-no-other-1915a990c419