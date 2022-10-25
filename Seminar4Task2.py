# Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.
m = int(input("Введите натуральное число: "))
def get_dividers(n):
    dividers = []
    i = 2
    while 1 < n:
        if n % i == 0:
            dividers.append(i)
            n = n // i
        else:
            i += 1
    return dividers

print(get_dividers(m))

