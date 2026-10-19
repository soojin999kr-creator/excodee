numbers = [1, 2, 2, 5, 3, 4, 3, 5, 1, 6]
unique_numbers = []

for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)

print(unique_numbers)
