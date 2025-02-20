def double(numbers):
    result = numbers.copy()
    for i in range(len(result)):
        result[i] *= 2
    return result

numbers = [1, 2, 3, 4]
print(double(numbers))
print(numbers)


first = [12, 14]
second = [45, 8, 19]
print(first + second)