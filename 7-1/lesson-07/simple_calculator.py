
a = int(input("Մուտքագրեք առաջին թիվը: "))
b = int(input("Մուտքագրեք երկրորդ թիվը: "))
operator = input("Մուտքագրեք գործողությունը (+, -, *, /): ")

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b != 0:
        result = a / b
    else:
        result = "Սխալ: Չի կարելի բաժանել զրոյով"
else:    result = "Սխալ: Անհայտ գործողություն"

print("Արդյունքը:", result)
 