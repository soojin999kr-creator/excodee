a = [1, 0, 1]
b = [1, 1, 2]

total = 0
for i in range(len(a)):
    total += a[i] * b[i]

print(f"{a} * {b} = {total}")