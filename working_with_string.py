print("This is a program to work with string") #original text


print("This is a program \n to work with string") # \n is a new line character that makes the second part of the code print out in a new line

print("This is a program \"to work with string\"" ) # \" is a escape character that allows you to use a quote inside a string

phrase = "This is a program to work with string" #assigning a variable to a string
print(phrase)

#concatenation
print(phrase + " and also concatenation") #concatenation is when you add two strings together

print(phrase.lower()) #lowercase all the letters in the string
print(phrase.upper()) #uppercase all the letters in the string
print(phrase.isupper()) #check if all the letters in the string are uppercase
print(phrase.upper().isupper()) #check if all the letters in the string are uppercase
print(len(phrase)) #print the length of the string (i.e the number of characters in the string and inclusive of spaces)
print(phrase[0]) #print the first character of the string, changing the number will print the character at that index
print(phrase.index("p")) #print the index of the character in the string, changing the character will print the index of that character
print(phrase.replace("program", "code")) #replace a word in the string with another word