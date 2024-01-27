def is_palindrome(string):
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]


user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("It is a palindrome")
else:
    print("It is not a palindrome")