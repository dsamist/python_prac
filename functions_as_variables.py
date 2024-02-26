text = '''testing functions as variables
This is to signify that functions aren't really special in python, 
they are just variables that can be passed around and used as arguements in other functions
'''
def lowercase(text):
    return text.lower()

def removePunctuation(text):
    punctuations = ['.', ',', '!', '?', ':', ';', '-', '(', ')', '[', ']', '{', '}', '"', "'"]
    for punctuation in punctuations:
        text = text.replace(punctuation, '')
    return text

def removeNewLines(text):
    text = text.replace('\n', ' ')
    return text

def removeShortWords(text):
    words = text.split()
    longWords = [word for word in words if len(word) > 3]
    return ' '.join(longWords)

def removeLongWords(text):
    words = text.split()
    shortWords = [word for word in words if len(word) < 5]
    return ' '.join(shortWords)

processingFunctions = [lowercase, removePunctuation, removeNewLines, removeShortWords, removeLongWords]

#the following code will apply all the functions in the processingFunctions list to the text
for func in processingFunctions:
    text = func(text)
