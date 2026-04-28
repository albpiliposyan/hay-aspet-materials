numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
unique_numbers = []

for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)

print(f"Մինչև. {numbers}")
print(f"Հետո. {unique_numbers}")
