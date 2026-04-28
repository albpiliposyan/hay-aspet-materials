grades = []

while True:
    value = input("Մուտքագրեք գնահատականը (կամ 'stop'՝ ավարտելու համար). ")
    if value.lower() == 'stop':
        break
    
    grade = int(value)
    grades.append(grade)

if grades:
    grades_sum = 0
    for grade in grades:
        grades_sum += grade
    average = grades_sum / len(grades)
    print(f"Միջին գնահատականը՝ {average:.2f}")
    print(f"Ամենաբարձրը՝ {max(grades)}")
    print(f"Ամենացածրը՝ {min(grades)}")
else:
    print("Ցուցակը դատարկ է:")
