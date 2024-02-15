# For this challenge, your task is to read a text file containing lists of filenames with extensions and determine which names are unique per row, ignoring the file extensions.

# For example, consider the following text file:

# foo.mp3|bar.txt|baz.mp3
# wub.mp3|wub.mp3|wub.mp3|wub.txt|wub.png
# quux.mp3|quux.txt|thud.mp3
# The expected output for this file is

# foo.mp3|bar.txt|baz.mp3
# thud.mp3
# After removing extensions, all three names are unique on line 1 so the entire line is unchanged.


def find_unique_filenames(filename: str) -> str:
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Initialize an empty string to store the result
        result = ""
        
        # Read the file line by line
        for line in file:
            # Split the line into filenames
            filenames = line.strip().split('|')
            
            # Remove the extensions from the filenames
            names = [name.split('.')[0] for name in filenames]
            
            # Check for uniqueness and add the unique filenames to the result
            unique_names = [filenames[i] for i in range(len(names)) if names.count(names[i]) == 1]
            if unique_names:
              result += '|'.join(unique_names) + '\n'
        
        return result.strip()


