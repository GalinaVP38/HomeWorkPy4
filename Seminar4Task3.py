# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности. Пример: 47756688399943 -> [5] 1113384455229 -> [8,9]
# 1115566773322 -> []
from random import randint

def forming_list(size, m, n):
    return [randint(m, n) for i in range(size)]
def get_unic_num(list):
    return [i for i in set(list)]
size = 10
m = 1
n = 10
lst = forming_list(size, m, n)
print(lst)
print(get_unic_num(lst))