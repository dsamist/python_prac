#find prime number up to a given number

#solution 1


def allPrimesUpTo(num):
    primes = []
    for number in range(2, num):
        for factor in range(2, int(number ** 0.5) + 1):
            if number % factor == 0:
                break
        else:
            primes.append(number)
    return primes

print(allPrimesUpTo(100))


#solution 2
def allPrimesUpTo2(num):
    primes = [2]
    for number in range (3, num):
        sqrt = number ** 0.5
        for factor in primes:
            if number % factor == 0:
                break
            if factor > sqrt:
                primes.append(number)
                break
    return primes