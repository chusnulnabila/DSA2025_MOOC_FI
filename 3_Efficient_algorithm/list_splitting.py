
def count_splits(numbers, vel):
    if vel == 1:
        n = len(numbers)
        result = 0
        for i in range(n-1):
            left_sum = sum(numbers[0:i+1])
            right_sum = sum(numbers[i+1:])
            if left_sum == right_sum:
                result += 1
        return result
    elif vel == 2:
        n = len(numbers)
        result = 0
        left_sum = 0
        for i in range(n-1):
            left_sum += numbers[i]
            right_sum = sum(numbers[i+1:])
            if left_sum == right_sum:
                result += 1
        return result
    elif vel == 3:
        n = len(numbers)
        result = 0
        left_sum = 0
        total_sum = sum(numbers)
        for i in range(n-1):
            left_sum += numbers[i]
            right_sum = total_sum - left_sum
            if left_sum == right_sum:
                result += 1
        return result