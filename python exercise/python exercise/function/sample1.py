def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= total
    return total


print(multiply(2,3,4,5,6,7))
