# O(n^2)
# def count_ways(bits):
#     n = len(bits)
#     result = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             if bits[i] == '0' and bits[j] == '1':
#                 result += 1
#     return result


# O(n)
def count_ways(bits):
    n = len(bits)
    result = 0
    zeros = 0
    for i in range(len(bits)):
        if bits[i] == '0':
            zeros += 1
        if bits[i] == '1':
            result += zeros
    return result

print(count_ways("0010001"))