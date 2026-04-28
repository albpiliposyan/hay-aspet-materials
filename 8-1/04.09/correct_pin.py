correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input(f"Մուտքագրեք PIN-ը (մնաց {attempts} փորձ). ")
    if pin == correct_pin:
        print("Մուտքը հաջողվեց:")
        break
    else:
        attempts -= 1
        print("Սխալ PIN:")

if attempts == 0:
    print("Քարտը բլոկավորված է:")