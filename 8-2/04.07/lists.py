students = ["Անի", "Գոռ", "Մանե", "Դավիթ"]

# Ավելացնում ենք նոր աշակերտ
students.append("Լևոն")

# Պարզվում է՝ Գոռը տեղափոխվել է (նա 1-ին համարն է)
students.pop(1)

print(f"Դասարանում մնացին {len(students)} աշակերտ. {students}")


import random
random_list = []
for _ in range(10):
    random_list.append(random.randint(1, 100))

print(random_list)

even_numbers = []
for num in random_list:
    if num % 2 == 0:
        even_numbers.append(num)

print(f'Even numbers: {even_numbers}')