# This is a program to find the max number in a list

# Ask the user how many numbers they want to input
while True:
    user_input_str = input("How many numbers do you want to input? ")

    # Check if the input is a digit
    if user_input_str.isdigit():
        user_input = int(user_input_str)

        # Check if the integer is greater than or equal to 1
        if user_input >= 1:
            break  # Exit the loop if the input is valid
        else:
            print("Please enter an integer greater than or equal to 1.")
    else:
        print("Please enter a valid integer.")

list_of_numbers = []
while user_input:
    num = float(input("Enter a number: "))
    user_input -= 1
    list_of_numbers.append(num)

max_number = max(list_of_numbers)

print("The maximum number is " + str(max_number))
