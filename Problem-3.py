
a = int(input("Enter a number: "))

result = []

limit = a if a % 2 != 0 else a - 1

for i in range(1, limit + 1, 2):
    result.append(i)

print(result)
