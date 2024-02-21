def factorial (num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1
    i = 0
    f = 1

    while i < num:
        i += 1
        f *= i

    return f


print(factorial(5))# 120

print(factorial('samuel'))# 1