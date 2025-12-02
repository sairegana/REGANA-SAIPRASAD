
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

result = {}

for n in range(1, 10):
    count = 0
    for value in numbers:
        if value % n == 0:
            count += 1
    result[n] = count

print(result)
