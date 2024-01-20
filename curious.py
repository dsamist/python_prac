fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

def check_fruit(item):
    if item == "banana":
        return "orange"
    else:
        return item

result = [check_fruit(fruit) for fruit in fruits]
print(result)

