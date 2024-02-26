import random
import time

servicesAreUp = True

def getData50():
    if servicesAreUp and random.random() < 0.5:
        return 'You got the data, this only happens 50% of the time'

def getData25():
    if servicesAreUp and random.random() < 0.25:
        return 'You got the data, this only happens 25% of the time'

def getData10():
    if servicesAreUp and random.random() < 0.1:
        return 'You got the data, this only happens 10% of the time'

def getWithRetry(dataFunc):
    max_retries = 20
    for _ in range (0, max_retries):
        response = dataFunc()
        if response:
            return response