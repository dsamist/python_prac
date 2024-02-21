def encodeString(stringVal):
    # Function to encode a string by counting consecutive characters
    
    # Initialize an empty list to store encoded pairs (character, count)
    encodedList = []
    # Initialize variables to track the previous character and its count
    prevChar = stringVal[0]
    count = 0
    
    # Iterate through each character in the input string
    for char in stringVal:
        # Check if the current character is different from the previous one
        if prevChar != char:
            # If different, append the encoded pair to the list
            encodedList.append((prevChar, count))
            # Reset the count for the new character
            count = 0
        # Update the previous character
        prevChar = char
        # Increment the count for the current character
        count += 1
    
    # Append the last encoded pair to the list
    encodedList.append((prevChar, count))
    # Return the final list of encoded pairs
    return encodedList


def decodeString(encodedList):
    # Function to decode a list of encoded pairs into the original string
    
    # Initialize an empty string to store the decoded result
    decodedString = ''
    
    # Iterate through each encoded pair in the list
    for item in encodedList:
        # Repeat the character according to its count and append to the decoded string
        decodedString += item[0] * item[1]
    
    # Return the final decoded string
    return decodedString
