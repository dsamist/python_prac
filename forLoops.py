#using forLoops

animalLookup = {
    'a' : ['antelope', 'aardvark', 'alpaca'],
    'b' : ['bear'],
    'c' : ['cat'],
    'd' : ['dog']
}

#using pass to skip the execution of the for loop
for letters, animals in animalLookup.items():
    pass

#using continue to skip the execution of the for loop
for letters, animals in animalLookup.items():
    if len(animals) > 1:
        continue
    print(f'only one animal found {animals[0]}')

#using break to exit the for loop
for letters, animals in animalLookup.items():
    if len(animals) > 1:
        print(f'found {len(animals)} animals: {animals}')
        break
    
    
#using for/else, 

for number in range(2, 100):
    for factor in range(2, int(number ** 0.5) + 1):
        if number % factor == 0:
            break
    else:
        print(f'{number} is a prime number')

            