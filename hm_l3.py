print("I love Python"*42)

age_in_month = 25*12
age_in_years = int(age_in_month/12)
name = "Andrii"
my_age = f"Му name is {name} I’m {age_in_years} years old"

n = 1

if n > 0:
    print(f"{n} > 0")
elif n < 0:
    print(f"{n} < 0")
elif n == 0:
    print(f"{n} = 0")
elif n != 2:
    print(f"{n} не равно 2")
elif n >= 1:
    print(f"{n} больше или равно 1")
else:
    print(n)

a = 2
b = 5
c = 6

d = f"{a}{b}{c}"
print(d)


