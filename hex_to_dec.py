
hexNumber = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15

}

def hexToDec(num):
    for char in num:
        if char not in hexNumber:
            return None
    
    if len(num) == 3:
        return hexNumber[num[0]] * 16 ** 2 + hexNumber[num[1]] * 16 + hexNumber[num[2]]

    if len(num) == 2:
        return hexNumber[num[0]] * 16 + hexNumber[num[1]]

    if len(num) == 1:
        return hexNumber[num[0]]


#another solution
def hexToDec2(num):
    for char in num:
        if char not in hexNumber:
            return None
    
    exponent = 0
    decimalValue = 0

    for char in hexNumber[::-1]:
        decimalValue += hexNumber[char] * (16 ** exponent)
        exponent += 1
    
    return decimalValue

